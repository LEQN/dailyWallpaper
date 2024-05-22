import os
import json
import schedule
import time
import random
import subprocess
from datetime import date

wallpapers = {}
filename = "wallpaper.json"
img_path = "/home/leon/Pictures/wallpapers/"


def save_wallpapers():
    with open(filename, "w") as f:
        data = {"wallpapers": wallpapers}
        json.dump(data, f)


def load_dir():
    files_in_dir = os.listdir(img_path)
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


def load_used_wallpapers(wallpaper_key):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        used_wallpapers = data.get("used", [])
    except:
        return False
    if not str(wallpaper_key) in used_wallpapers:
        return False
    else:
        return True


def save_used_wallpapers(wallpaper):
    try:
        with open(filename) as f:
            data = json.load(f)
    except json.JSONDecodeError:
        data = {"wallpapers": wallpapers}

    used_wallpapers = data.get("used", [])
    used_wallpapers.append(str(wallpaper))
    data["used"] = used_wallpapers
    json.dump(data, open(filename, "w"))


def random_wallpaper():
    last_img_key = len(wallpapers) - 1
    random_img_key = random.randint(0, last_img_key)
    while True:
        if load_used_wallpapers(random_img_key):
            random_img_key = random.randint(0, last_img_key)
        else:
            break
    save_used_wallpapers(random_img_key)
    chosen_wallpaper = wallpapers.get(str(random_img_key))
    return chosen_wallpaper


def set_wallpaper(wallpaper):
    chosen_wallpaper_path = img_path+wallpaper
    if not os.path.exists(chosen_wallpaper_path):
        print("Error: path to wallpaper does not exist")
        return
    command = ["feh", "--bg-scale", chosen_wallpaper_path]
    try:
        subprocess.Popen(command)
    except:
        print("Failed to set wallpaper.")


def update_wallpaper(date_today):
    chosen_wallpaper = random_wallpaper()
    set_wallpaper(chosen_wallpaper)
    try:
        with open(filename) as f:
            data = json.load(f)
    except json.JSONDecodeError:
        data = {"wallpapers" : wallpapers}
    data["date"] = date_today
    json.dump(data, open(filename, "w"))


def load_last_update():
    print("Loading last update")
    try:
        data = json.load(open(filename, "r"))
        return data.get("date", None)
    except json.JSONDecodeError:
        return None


def date_check():
    print("checking date.")
    last_update = load_last_update()
    today = str(date.today())
    if last_update != today:
        update_wallpaper(today)


def scheduled_checks():
    schedule.every().hour.do(date_check)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    load_dir()
    date_check()
    scheduled_checks()