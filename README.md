# Undertale PC/Switch Save File Converter V2.0
Inspired by JonyLuke's Undertale Save Converter (https://github.com/jonyluke/Undertale-save-converter).
This version is a complete re-write, and features full bi-directional conversion functionality.

[Project page on the GBATemp Forum](https://gbatemp.net/threads/undertale-save-game-converter-v2-with-full-bi-directional-pc-switch-conversion-ability.542897/)

## Requirements 
- Undertale
- A Modded Nintendo Switch
- Python3.4 (https://www.python.org/downloads/) - Optional
  (Note: This is only required if you want to compile the converter.exe file yourself, or if you want to run converter.py directly)


## Installation and Usage
1. Download the latest release from https://github.com/tomchapin/undertale-save-converter/releases
2. Save it to a folder on your local computer.
3. Copy your game save files to the same folder.
4. Make sure you have Python3 installed


### Converting from PC to Switch
1. Make sure you have copied your game's file0, file9, and undertale.ini files into the folder with the converter.py file.
   (These files are typically located in your system's %LocalAppData%\UNDERTALE\ folder)
2. Use your command prompt to browse to the folder, then execute `python converter.py` and select the first menu option.


### Converting from Switch to PC
1. Make sure you have the undertale.sav file copied from your Nintendo Switch placed in the folder with the converter.py file.
   This file can be obtained from a modded switch by using tools such as Checkpoint or JKSM.
   - Checkpoint: https://gbatemp.net/threads/checkpoint-a-simple-and-fast-save-manager.485591
   - JKSM: https://github.com/J-D-K/JKSM
2. Use your command prompt to browse to the folder, then execute `python converter.py` and select the second menu option.


### Compiling the executable (if you don't want to download and use the supplied converter.exe file)
1. Install Python 3.4 (x86) on a Windows computer, making sure you select the option to add Python to your path.
2. Install the Py2Exe utility (`pip install py2exe`) - https://pypi.org/project/py2exe/
3. Install pywin32-221.win32-py3.4.exe from https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/
4. Check out this git repo to a folder on your local computer.
5. Browse to the folder and execute `pip install -r requirements.txt` (to install dependencies).
6. Execute `py -3.4 -m py2exe.build_exe converter.py` to compile the converter.py file to an .exe file.
7. Look inside the `dist` folder for your newly created `converter.exe` file!
