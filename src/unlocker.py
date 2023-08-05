# imports

import os
import platform
import sys
import json

# warnings and allow aborts.
try:
    input("HOLD UP! dont use any other fps unlockers with this code or you might break something lmao\n\nif you're ready, hit ENTER, else hold CONTROL and TAP C")
    input("\nalso please ensure roblox is NOT running, weird right? ik. same instructions to continue or cancel as before btw")
except KeyboardInterrupt:
    print("\naborted")
    os.system("color 47")
    input("[ press ENTER to exit ]")
    os.system("color")
    sys.exit()

try:
    # check if we're on windows, if not: quit
    if platform.uname().system.lower() != "windows":
        print("[ERROR] this script only works on windows, soz")
        input("[ press ENTER to exit ]")
        sys.exit("only windows is supported, sorry")

    # we're not unlocking the fps, that's impossible, so we're just setting it so INSANELY HIGH that it's basically unlocked.
    JSON_DATA = {
        "DFIntTaskSchedulerTargetFps": 200000000
    }

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
                    json.dump(JSON_DATA, fp, indent=4)
                
                print(f"[✓] patched {rblxFileData[i]}")
            else:
                # create client settings folder
                print(f"[!] \"{rblxFileData[i]}\" does not contain client settings, fixing...")
                os.mkdir("ClientSettings")

                # cd into it
                os.chdir("ClientSettings")
                # create a new settings file and dump our json data.
                with open("ClientAppSettings.json", "w") as fp:
                    json.dump(JSON_DATA, fp, indent=4)
                
                print(f"[✓] patched {rblxFileData[i]}")
        else:
            # that entry isnt a directory, so we ignore it and print a note.
            print(f"[!] \"{rblxFileData[i]}\" is not a directory!")

    # we successfully did it! (colour the window green to make it obvious)
    os.system("color 20")
    print("\nDONE'D!\n(every time roblox updates you will need to re-run this script...)")
    input("[ press ENTER to exit ]")
    # reset the colour, because it's nice.
    os.system("color")

except Exception as err:
    # oops, something went wrong.
    os.system("color 47")
    # prints the error to console
    print(f"[! FATAL !] Uncaught exception: {err}.")
    input("[ press ENTER to exit ]")
    # reset the colour, because it's nice.
    os.system("color")