import sys
import os
import json
from pathlib import Path
import winattr

APPDATA_DIR = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming")) / "cli-tools"
STATE_FILE = APPDATA_DIR / "win_state.json"

APPDATA_DIR.mkdir(parents=True, exist_ok=True)
state = {}

def load_state():
    global state
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            state = json.load(f)
    else:
        state = {}

def save_state():
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def alias(name, hwnd):
    state[name] = {"hwnd": hwnd, "hidden": False}
    save_state()

def list_tracked_windows():
    print(f"{'NAME':<30} | {'ALIAS':<15} | HIDDEN")
    print("-" * 60)
    for name, data in state.items():
        real_name = winattr.get_name(data["hwnd"])
        if not real_name:
            real_name = "[Closed/Unknown]"
        
        if len(real_name) > 27:
            real_name = real_name[:24] + "..."
            
        print(f"{real_name:<30} | {name:<15} | {data['hidden']}")

def main():
    load_state()
    args = sys.argv[1:]
    
    if len(args) == 0:
        winattr.get_windows(pretty=True)
        return

    cmd = args[0].lower()

    if cmd == "list":
        list_tracked_windows()

    elif cmd == "hide":
        if len(args) < 2:
            print("Error: Missing target window name.")
            return
        target = args[1]
        if target in state:
            winattr.hide(state[target]["hwnd"])
            state[target]["hidden"] = True
            save_state()
        else:
            print(f"Error: Alias '{target}' does not exist.")

    elif cmd == "show":
        if len(args) < 2:
            print("Error: Missing target window name.")
            return
        target = args[1]
        if target in state:
            winattr.show(state[target]["hwnd"])
            state[target]["hidden"] = False
            save_state()
        else:
            print(f"Error: Alias '{target}' does not exist.")

    elif cmd == "alias":
        if len(args) < 3:
            print("Error: Usage is 'win alias <HWND> <name>'")
            return
        target = int(args[1], 16)
        name = args[2]
        print(f"Setting alias '{name}' for {hex(target)}")
        alias(name, target)

    else:
        print(f"Unknown command: '{cmd}'")

if __name__ == "__main__":
    main()
