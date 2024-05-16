import os
import json

wallpapers = {}
filename = "wallpaper.json"


def save_wallpapers():
    with open(filename, "w") as f:
        json.dump(wallpapers, f)


def load_dir():
    files_in_dir = os.listdir("/home/leon/Pictures/wallpapers")
    for i in range(0, len(files_in_dir)):
        wallpapers[str(i)] = files_in_dir[i] #typecast key to string to match json format

    if not os.path.exists(filename):
        save_wallpapers()
    else:
        with open(filename, "r") as f:
            saved_walls = json.load(f)
            if saved_walls != wallpapers:
                print("Files in directory have changed.")
                save_wallpapers()


if __name__ == "__main__":
    load_dir()