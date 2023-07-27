# Undertale PC/(Switch or Mobile) Save File Converter V2.1
Inspired by JonyLuke's Undertale Save Converter (https://github.com/jonyluke/Undertale-save-converter).
This version is a complete re-write, and features full bi-directional conversion functionality.

[Project page on the GBATemp Forum](https://gbatemp.net/threads/undertale-save-game-converter-v2-with-full-bi-directional-pc-switch-conversion-ability.542897/)


## Requirements 
- Undertale for both platforms
- Python 3

## Installation and Usage
1. Download the latest release from https://github.com/tomchapin/undertale-save-converter/releases
2. Save it to a folder on your local computer.
3. Copy your game save files to the same folder.


### Converting from PC to Switch/Mobile
1. Make sure you have copied your game's file0, file9, and undertale.ini files into the folder with the undertale_save_converter.exe file.
   (These files are typically located in your system's %LocalAppData%\UNDERTALE\ folder)
2. Use your command prompt to browse to the folder, then execute `undertale_save_converter.exe` and select the first menu option.
3. Alternately (if you want to run the script via python), execute `python undertale_save_converter.py` (requires Python 3 to be installed).


### Converting from Switch/Mobile to PC
1. Make sure you have the undertale.sav file copied from your Nintendo Switch placed in the folder with the undertale_save_converter.exe file.
   This file can be obtained from a modded switch by using tools such as Checkpoint or JKSM.
   - Checkpoint: https://gbatemp.net/threads/checkpoint-a-simple-and-fast-save-manager.485591
   - JKSM: https://github.com/J-D-K/JKSM
2. Use your command prompt to browse to the folder, then execute `undertale_save_converter.exe` and select the second menu option.
3. Alternately (if you want to run the script via python), execute `python undertale_save_converter.py` (requires Python 3 to be installed).


### Compiling the executable (if you don't want to download and use the supplied undertale_save_converter.exe file)
figure out how to use pyinstaller. 
