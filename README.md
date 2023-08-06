<h1 align="center"> rblx-fps-unlocker</h1>
<p align="center">A FPS unlocker for Roblox that doesn't change any system files.</p>

## About
This app unlocks the Roblox FPS in [an anticheat safe way](https://github.com/just-autumn/rblx-fps-unlocker#is-this-safe) and also allows you to set the FPS cap yourself, if you so choose.

## Is this safe?
Since this script just uses code that's already built into Roblox, just disabled by default, it doesn't trigger Byfron. We just add a file for advanced settings which activates the code. Think of loading custom audio files in studio, we add a file but don't modify anything.

## Download
### GitHub (Recommended)
You can download a release from the [GitHub releases page](https://github.com/just-autumn/rblx-fps-unlocker/releases)

### Building from source
This is a Python project so compilation *isn't required* but can be done. The tool I use it [PyInstaller](https://pypi.org/project/pyinstaller/) with the following command:
```bat
pyinstaller --clean -F unlocker.py -n "Roblox FPS Unlocker" -i "icon.png"
```

#### Source requirements:
Building from source requires the following package(s) to be installed with pip:
- *[WINDOWS]:* [windows-curses](https://pypi.org/project/windows-curses/) -- `pip install windows-curses`