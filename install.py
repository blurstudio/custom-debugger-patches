
print("Copying files...", end=" ")

import platform
from os.path import dirname, join
from shutil import copyfile
import os

patches = join(dirname(__file__), "patches")

plat = platform.system()

if plat == 'Windows':
    debugger = join(os.getenv('APPDATA'), "Roaming", "Sublime Text 3", "Packages", "Debugger")

# The list of patches as filename: path from Debugger root
patches = {
    "variables.py": join("modules", "debugger")
}

for f, path in patches:
    copyfile(join(patches, f), join(debugger, path, f))  # Replaces the destination file by default

print("Done.\n\nPlease restart Sublime Text if it is currently open.")
