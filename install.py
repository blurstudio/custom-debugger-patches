
from os.path import dirname, join, exists
from shutil import copyfile
import sublime

version = "0.1"

def plugin_loaded():
    lock = join(dirname(__file__), 'lock.txt')
    if exists(lock):
        with open(lock, 'r') as f:
            v = f.readline()
        if v == version:
            return
        
    with open(lock, 'w') as f:
        f.write(version)

    patch_dir = join(dirname(__file__), "patches")

    debugger = join(sublime.packages_path(), "Debugger")

    # The list of patches as filename: path from Debugger root
    patches = {
        "variables.py": join("modules", "debugger")
    }

    for f, path in patches.items():
        src = join(patch_dir, f)
        dst = join(debugger, path, f)
        copyfile(src, dst)  # Replaces the destination file by default

    msg = "Finished installing patches. Please restart Sublime for them to take effect."
    print(msg)
    sublime.message_dialog(msg)

