
from os.path import dirname, join, exists
from shutil import copyfile
import sublime

version = "0.2"

def plugin_loaded():
    lock = join(dirname(__file__), 'lock.txt')
    update = False
    if exists(lock):
        with open(lock, 'r') as f:
            v = f.readline()
            update = True
        if v == version:
            return
        
    with open(lock, 'w') as f:
        f.write(version)

    patch_dir = join(dirname(__file__), "patches")

    debugger = join(sublime.packages_path(), "Debugger")

    # The list of patches as filename: path from Debugger root
    patches = {
        "variables.py": join("modules", "debugger"),
    }

    for f, path in patches.items():
        src = join(patch_dir, f)
        dst = join(debugger, path, f)
        copyfile(src, dst)  # Replaces the destination file by default

    msg = "Successfully installed patches." if not update else "Successfully updated patches."
    print(msg)
    sublime.message_dialog(msg)

