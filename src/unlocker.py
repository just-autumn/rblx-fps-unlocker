# imports

import os
import platform
import sys
import json
import time

# custom import.
import selection

os.system("title Roblox FPS Unlocker")

choice = str(selection.Selection("Roblox FPS Unlocker. V1.2, © Autumn 2022 - present", ["Unlock FPS", "Set frame cap", "Uninstall", "Abort"], "-> "))

if choice == "Unlock FPS":
    json_data = {
            "DFIntTaskSchedulerTargetFps": 200000000
    }
elif choice == "Set frame cap":
    while True:
        try:
            validFR = True
            frameRate = int(input("Enter frame cap (going below 60 is not advised.)\n-> "))
            if 0 < frameRate <= 15:
                print("A frame rate below 15 will make the game unplayable.")
                input("[ Press RETURN to ignore warning . . . ]")
            elif 15 < frameRate < 60:
                print("A frame rate below 60 may cause issues in some games and will lead to an unpleasant playing experience.")
                input("[ Press RETURN to ignore warning . . . ]")
            elif frameRate <= 0:
                print("A frame rate below 0 is impossible, try again.\n")
                validFR = False
            
            json_data = {
                "DFIntTaskSchedulerTargetFps": frameRate
            }

            if validFR:
                break
        except TypeError:
            print("Value must be an integer!\n")
        except KeyboardInterrupt:
            print("Aborted.")
            time.sleep(7)
            exit(0)

elif choice == "Uninstall":
    json_data = {
            "DFIntTaskSchedulerTargetFps": 60
    }

elif choice == "Abort":
    print("Aborted.")
    time.sleep(7)
    exit(0)

else:
    os.system("color 20")
    print("[! FATAL !] Selection not found. Has the script been modified?")
    time.sleep(7)
    os.system("color")
    exit(1)

try:
    # check if we're on windows, if not: quit
    if platform.uname().system.lower() != "windows":
        print("[ERROR] this script only works on windows, soz")
        input("[ press ENTER to exit ]")
        sys.exit("only windows is supported, sorry")

    # go to our app data for roblox
    RBLXAPPDATA = rf"{os.getenv('APPDATA')}\..\Local\Roblox\Versions"

    # cd into it.
    os.chdir(RBLXAPPDATA)
    # get every entry in it.
    rblxFileData = os.listdir()
    
    for i in range(len(rblxFileData)):
        # let's iterate through every roblox install and patch it!
        os.chdir(RBLXAPPDATA)
        # check if the entry is actually a directory lol...
        if os.path.isdir(rblxFileData[i]):
            # cd into it.
            os.chdir(rblxFileData[i])
            # check if it has a client settings folder, just to prevent duplicate folders (not that that can happen...)
            if os.path.isdir("ClientSettings"):
                print(f"[✓] \"{rblxFileData[i]}\" has a client settings folder!")
                # cd into it
                os.chdir("ClientSettings")

                # create a new settings file and dump our json data.
                with open("ClientAppSettings.json", "w") as fp:
                    json.dump(json_data, fp, indent=4)
                
                print(f"[✓] patched {rblxFileData[i]}")
            else:
                # create client settings folder
                print(f"[!] \"{rblxFileData[i]}\" does not contain client settings, fixing...")
                os.mkdir("ClientSettings")

                # cd into it
                os.chdir("ClientSettings")
                # create a new settings file and dump our json data.
                with open("ClientAppSettings.json", "w") as fp:
                    json.dump(json_data, fp, indent=4)
                
                print(f"[✓] patched {rblxFileData[i]}")
        else:
            # that entry isnt a directory, so we ignore it and print a note.
            print(f"[!] \"{rblxFileData[i]}\" is not a directory!")

    # we successfully did it! (colour the window green to make it obvious)
    print(r"""

 ____                   _
|  _ \  ___  _ __   ___| |
| | | |/ _ \| '_ \ / _ \ |
| |_| | (_) | | | |  __/_|
|____/ \___/|_| |_|\___(_)
""")
    print("Finished with 0 errors.\n(every time roblox updates you will need to re-run this script...)")

except Exception as err:
    # oops, something went wrong.
    os.system("color 47")
    # prints the error to console
    print(f"[! FATAL !] Uncaught exception: {err}.")
    # reset the colour, because it's nice.

print(rf"""
a script by...
      .o.                       .                                                Roblox FPS Unlocker   V1.2
     .888.                    .o8                                                © 2022 - present,     Autumn
    .8"888.     oooo  oooo  .o888oo oooo  oooo  ooo. .oo.  .oo.   ooo. .oo.      written in:           Python 3.11.3
   .8' `888.    `888  `888    888   `888  `888  `888P"Y88bP"Y88b  `888P"Y88b     running on:           {platform.uname().machine} {platform.uname().system} {platform.uname().release}
  .88ooo8888.    888   888    888    888   888   888   888   888   888   888     installed at:         <** REDACTED **>
 .8'     `888.   888   888    888 .  888   888   888   888   888   888   888     documentation:        <unavailable>
o88o     o8888o  `V88V"V8P'   "888"  `V88V"V8P' o888o o888o o888o o888o o888o    supprt:               <unavailable>
""")

print("\nChanges require Roblox to be restarted.")
input("[ press ENTER to exit ]")
os.system("color")