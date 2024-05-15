import os
import json

wallpapers = {}
filename = "wallpaper.json"

def load_dir():
    files_in_dir = os.listdir("/home/leon/Pictures/wallpapers")
    for i in range(0, len(files_in_dir)):
        wallpapers[str(i)] = files_in_dir[i] #typecast key to string to match json format
    try:
        if os.path.exists(filename):
            with open(filename, "r") as f:
                saved_walls = json.load(f)
                if saved_walls != wallpapers:
                    print("dir has changed")
                    with open(filename, "w") as f:
                        json.dump(wallpapers, f)
        else:
            with open(filename, "w") as f:
                json.dump(wallpapers, f)
    except:
        print("Failed to load or write data")


load_dir()