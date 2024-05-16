import os
import json
from datetime import date

wallpapers = {}
filename = "wallpaper.json"


def save_wallpapers():
    with open(filename, "w") as f:
        data = {"wallpapers": wallpapers}
        json.dump(data, f)


def load_dir():
    files_in_dir = os.listdir("/home/leon/Pictures/wallpapers")
    for i in range(0, len(files_in_dir)):
        wallpapers[str(i)] = files_in_dir[i] #typecast key to string to match json format

    if not os.path.exists(filename):
        save_wallpapers()
    else:
        with open(filename, "r") as f:
            saved_walls = json.load(f)
            if saved_walls["wallpapers"] != wallpapers:
                print("Files in directory have changed.")
                save_wallpapers()


def update_wallpaper():
    print("Updating wallpaper")
    date_dict = {"date" : str(date.today())}
    with open(filename) as f:
        data = json.load(f)
        data.update(date_dict)
    json.dump(data, open(filename, "w"))


def load_last_update():
    print("Loading last update")
    data = json.load(open(filename, "r"))
    return data.get("date", None)


def date_check():
    print("checking date.")
    last_update = load_last_update()
    today = str(date.today())
    if last_update != today:
        update_wallpaper()


if __name__ == "__main__":
    load_dir()
    date_check()