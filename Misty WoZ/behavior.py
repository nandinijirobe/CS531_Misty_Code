#!/usr/bin/env python
from numpy import random
import threading
import time


LED_TRANSITION_BLINK = "blink"
LED_TRANSITION_BREATHE = "breathe"
LED_TRANSITION_TRANSIT_ONCE = "transitonce"
LED_TRANSITIONS = [LED_TRANSITION_BLINK, LED_TRANSITION_BREATHE, LED_TRANSITION_TRANSIT_ONCE]

class Behavior:
    def __init__(self, conn, path, filename):
        """Initialization of Behavior

        Keyword arguments:
        conn - Instance of MistyConnections
        path - Path to the folder containing all behaviors.
        filename - Filename of the behavior.
        """
        # Oopen and read the instructions
        f = open(path + '/' + filename, 'r')
        self.conn = conn
        self.instructions = f.readlines()
        f.close()

    def run(self):
        """Executes behavior."""
        for instruction in self.instructions:
            args = instruction.replace('\n','').split(' ')
            # Ignore blank lines and lines with no args
            if len(args) < 2:
                continue

            # Move Arms
            elif args[0] == 'MAS':
                deg = int(args[1])
                spd = int(args[2])
                deg2 = int(args[3])
                spd2 = int(args[4])
                msg = [deg, spd, deg2, spd2]
                self.conn.armsPub(msg)
            # Move Head
            elif args[0] == 'MH':
                roll = int(args[1])
                pitch = int(args[2])
                yaw = int(args[3])
                spd = int(args[4])
                msg = [roll, pitch, yaw, spd]
                self.conn.hdPub(msg)
            # Move the tracks of the robot
            elif args[0] == 'MT':
                linearMovement = int(args[1])
                angularMovement = int(args[2])
                timeInMS = int(args[3])
                msg = [linearMovement, angularMovement, timeInMS]
                self.conn.drvTimePub(msg)
            # Static LED Change
            elif args[0] == 'CL':
                red = int(args[1])
                green = int(args[2])
                blue = int(args[3])
                msg = [red, green, blue]
                self.conn.ledPub(msg)
            # Transition the LED between two colors
            elif args[0] == 'TL':
                from_red = int(args[1])
                from_green = int(args[2])
                from_blue = int(args[3])
                to_red = int(args[4])
                to_green = int(args[5])
                to_blue = int(args[6])
                transition = LED_TRANSITIONS.index(args[7].lower())
                timeInMS = int(args[8])
                msg = [from_red, from_green, from_blue, to_red, to_green, to_blue, transition, timeInMS]
                self.conn.transLEDPub(msg)
            # Sleep
            elif args[0] == 'SL':
                ms = int(args[1])
                self.conn.sleep(ms / 1000)
            # Change Facial Image
            elif args[0] == 'FI':
                imgName = args[1]
                msg = imgName
                x = threading.Thread(target=display_face, args=(self.conn.imgPub, msg))
                # imgPub.publish(msg)
                x.start()
            # Control Blink + Facial Image
            elif args[0] == 'FIB':
                imgName = args[1]
                blinkduration = float(args[2]) / 1000.0
                msg = imgName
                x = threading.Thread(target=control_face_and_blink, args=(self.conn.imgPub, msg, blinkduration))
                x.start()
            # Change Facial Image After Time
            elif args[0] == 'DFI':
                imgName = args[1]
                delay = float(args[2]) / 1000.0
                msg = imgName
                x = threading.Thread(target=delayed_display_face, args=(self.conn.imgPub, msg, delay, 0.0, 0.1))
                x.start()
            self.conn.sleep(0.5)

# Controls the time the blinking face is displayed before the new face
def control_face_and_blink(pub, msg, blink_duration):
    blink = "blinkMisty.png"
    blinkMsg = blink
    pub(blinkMsg)
    time.sleep(blink_duration)
    pub(msg)

# Blinks for a set amount of time before transitioning to the new face
def display_face(pub, msg):
    blink = "blinkMisty.png"
    blinkMsg = blink
    pub(blinkMsg)
    time.sleep(0.35)
    pub(msg)

# Wait for some time before displaying the new face
def delayed_display_face(pub, msg, mean, low, high):
    num = random.uniform(low, high)
    time.sleep(mean + num)
    blink = "blinkMisty.png"
    blinkMsg =  blink
    pub(blinkMsg)
    time.sleep(0.2)
    pub(msg)