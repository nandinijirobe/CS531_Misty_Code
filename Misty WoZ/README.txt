Installing Python (Windows):
1) Visit: https://www.python.org/downloads/ and download the latest version of Python3
2) Follow the installation process normally, but be sure to check the box that install Python to the path

To setup:
1) Install python3
2) Open cmd or powershell and navigate to where you unzipped the file. 
	2.a) Example for Windows: "cd C:\Users\Nathan\Documents\Misty_WoZ"
	2.b) Example for Ubuntu: "cd /home/nathan/Documents/Misty_WoZ"
3) If you're using an older version of Python (Python 3 older than 3.4) pip may not be installed. Verify pip is installed by running: "pip -V" and you should see something like: "pip XX.X.X from..."
	3.a) If pip isn't installed follow this guide: https://pip.pypa.io/en/stable/installing/
	3.b) You may need to run pip3 if pip is an unrecognized command
4) In the installed directory (ex: C:\Users\Nathan\Documents\Misty_WoZ) run the command "pip install -r requirements.txt"
	4.a) You may need to run pip3 if pip is an unrecognized command
	4.b) If the install fails, you might try installing each required library individually. Open the requirements.txt document and install each line.
	4.c) You might need to try slightly different versions of these libraries. e.g. numpy 1.20.0 has some issue installing and you may need to try 1.21 instead.
	4.d) other known issues with fixes: 
		i) ModuleNotFoundError: No module named 'urllib3.packages.six'"

		# Remove Package
		pip uninstall urllib3

		# Install Package
		pip install urllib3
		
		ii) ImportError: No module named 'setuptools.build_meta'
		pip install setuptools==58.0.4
	4.e) other known issues without fix:
		i)  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
			- Exception in thread Thread-1 (speakCommentAndWait):.
			- TypeError: Object of type bytes is not JSON serializable
	
Running the program:
1) Open cmd or powershell and navigate to where you unzipped the file. 
	1.a) Example for Windows: "cd C:\Users\Nathan\Documents\Misty_WoZ"
	1.b) Example for Ubuntu: "cd /home/nathan/Documents/Misty_WoZ"
2) Run the command: "python main.py <robot_ip>". Replace <robot_ip> with the IP address of the Misty robot.
	2.a) example: "python main.py 192.168.1.25"
	2.b) If python is an unrecognized command, you may need to run using python3 (ex: "python3 main.py 192.168.1.25")


The GUI is just a bunch of buttons that are each tied to comments in the Misty_Comments folder. In order for Misty to give a comment and display the associated emotion, you first need to select one of the buttons for robot names, intro, or pages. 
The robot names on top introduce the robot.
The "Intro X" are for the tutorial booklet
"PageX" are for the social commentary for the pages
"PageX_Y" are for the responses to children's comments.
The three buttons on the bottom (None, None & Forward, None & Back) reset the robot to the Neutral emotion and move the robot (usually didn't work in the study).

Once a comment has been selected, click the "Send Commands" button on the bottom. Misty will then act out the emotion and say the comment.

Blinking Issues:
1) You may have issues with Misty not blinking while showing the different facial expressions. To fix this, click the "Setup Maps" button in the GUI.