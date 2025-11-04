# CS531_Misty_Code — Misty WoZ

This repository contains the Misty Wizard-of-Zoom (WoZ) GUI and comment/behavior assets used for the CS531 project.

This README explains how to run the GUI reliably on Windows using the provided Conda environment or the project's venv, and documents a couple of small fixes and helpers included in the repository.

## Quick start (recommended — Conda)

1. Ensure you have Conda (Anaconda or Miniconda) installed and on PATH.
2. From a PowerShell prompt (you do not need to `conda activate` manually), run:

```powershell
# from repository root
conda run -n cs531_py311 python "Misty WoZ\main.py" 192.168.0.41
```

This uses the `cs531_py311` Conda environment (the repo author used this). The environment contains binary-friendly builds for packages like numpy which avoid compilation issues on Windows.

If you prefer an activated shell you can also run:

```powershell
conda init powershell   # only once, then restart shell
conda activate cs531_py311
cd "Misty WoZ"
python main.py 192.168.0.41
```

## Alternative: Use the included `.venv`

You can also use the project virtualenv `.venv` created in `Misty WoZ`.

```powershell
# Activate the venv
& "Misty WoZ\.venv\Scripts\Activate.ps1"
cd "Misty WoZ"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py 192.168.0.41
```

Notes:

- On Windows `pip install` may attempt to build binary packages (numpy) and fail; Conda is recommended for those.
- If you installed packages into the venv earlier, you can run directly with the venv's python without activating:
  `& "Misty WoZ\.venv\Scripts\python.exe" "Misty WoZ\main.py" 192.168.0.41`

## Helper script

A helper PowerShell script `run_misty.ps1` was added to the repo root. It prefers `conda run -n cs531_py311` and falls back to `.venv` if conda is not available. Example:

```powershell
.\run_misty.ps1 -ip 192.168.0.41
```

## What I changed (small, safe fixes)

- `Misty WoZ/misty.py`: added `import threading` and made `sendAndPlayAudio` produce a JSON-serializable payload (base64 string + `os.path.basename`) and used a context manager to read files.
- `run_misty.ps1`: helper to run the GUI with the correct interpreter.
- `.gitignore`: added to ignore `.venv`, IDE files, build artifacts, and OS files.

These changes are minimal and intended to make runtime behavior more predictable on Windows.

## Troubleshooting

- `ModuleNotFoundError: No module named 'mutagen'` — this happens when the `python` on your PATH is the system Python instead of the Conda env or `.venv` python. Use `conda run -n cs531_py311` or activate your environment before running.

  Verify the interpreter and package location:

  ```powershell
  python --version
  python -c "import sys; print(sys.executable)"
  python -c "import mutagen; print(mutagen.__file__)"
  ```

- `numpy` or other binary packages failing to install with pip — use Conda to install prebuilt binaries (recommended):

  ```powershell
  conda create -n cs531_py311 python=3.11.13 -y
  conda install -n cs531_py311 numpy requests -y
  conda install -n cs531_py311 -c conda-forge mutagen -y
  ```

## Editor / LSP

- If your editor (e.g., VS Code) reports missing imports, make sure the editor's selected Python interpreter matches the environment you use to run the program (either the Conda env `cs531_py311` or the project's `.venv`). Reload the editor window after switching the interpreter.

## Running without hardware

If you want to exercise the GUI without contacting a real Misty robot, you can add small guards or a dry-run mode in `main.py`/`misty.py`. I can add a `--dry-run` flag if you'd like.

## Files of interest

- `Misty WoZ/main.py` — GUI entry point
- `Misty WoZ/misty.py` — Misty API wrapper (audio, blink, arms, head, drive)
- `Misty WoZ/requirements.txt` — pip requirements (note: numpy pinned to 1.20.0 in the file may not support Python 3.11)
- `run_misty.ps1` — helpful runner at repo root

If you'd like, I can also commit an `environment.yml` for Conda reproducibility or add a `--dry-run` mode to the GUI for testing without the robot.

Enjoy — run:

```powershell
.\run_misty.ps1 -ip 192.168.0.41
```
