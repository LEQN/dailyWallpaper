import os
import json
import schedule
import time
import random
import subprocess
from datetime import date

imgs_path = "/home/leon/Pictures/wallpapers/"
filename = "wallpapers.json"
data = {}


def save_data():
  with open(filename, "w") as f:
      json.dump(data, f)


def load_data():
  global data
  try:
      with open(filename, "r") as f:
          data = json.load(f)
  except json.JSONDecodeError:
      data = {"wallpapers": {}, "used_wallpapers": [], "date": None}


def initialize():
  wallpapers = {}
  files_in_dir = os.listdir(imgs_path)
  for i in range(0, len(files_in_dir)):
      wallpapers[str(i)] = files_in_dir[i] #typecast key to string to match json format

  load_data()
  if wallpapers != data.get("wallpapers"):
      data["wallpapers"] = wallpapers
      data["used_wallpapers"] = []
      data["date"] = None


def get_random_wallpaper():
  wallpapers = data.get("wallpapers")
  used_wallpapers = data.get("used_wallpapers")
  available_wallpapers = [x for x in wallpapers.keys() if x not in used_wallpapers]

  if len(available_wallpapers) == 0:
      available_wallpapers = list(wallpapers.keys())
      used_wallpapers = []

  chosen_wallpaper_key = random.choice(available_wallpapers)
  used_wallpapers.append(chosen_wallpaper_key)
  data["used_wallpapers"] = used_wallpapers
  chosen_wallpaper = wallpapers.get(chosen_wallpaper_key)
  return chosen_wallpaper


def set_wallpaper(wallpaper):
  chosen_wallpaper_path = imgs_path+wallpaper
  if not os.path.exists(chosen_wallpaper_path):
      print(f"Error: path to wallpaper does not exist")
      return

  command = ["feh", "--bg-scale", chosen_wallpaper_path]
  subprocess.Popen(command)


def update_wallpaper(date_today):
  chosen_wallpaper = get_random_wallpaper()
  set_wallpaper(chosen_wallpaper)
  data["date"] = date_today
  save_data()


def current_wallpaper():
  wallpapers = data.get("wallpapers")
  current_wallpaper_key = data.get("used_wallpapers")[-1]
  current_wallpaper = wallpapers.get(str(current_wallpaper_key))
  set_wallpaper(current_wallpaper)


def date_check():
  saved_date = data.get("date")
  today = str(date.today())
  if saved_date != today:
      update_wallpaper(today)
  else:
      current_wallpaper()


def scheduled_checks():
  schedule.every().hour.do(date_check)
  while True:
      schedule.run_pending()
      time.sleep(1)


if __name__ == "__main__":
  initialize()
  date_check()
  scheduled_checks()