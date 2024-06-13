# dailyWallpaper

This Python program automatically changes the desktop wallpaper daily on a Linux system using feh to set them. The wallpapers are stored in a specified directory, and the program ensures that a new wallpaper is set each day.

## Prerequisites
- Linux system.
- 'feh' installed for setting wallpapers.
- pip install the schedule module.


## Installation
1. **Clone the Repository** (or download the script):
  ```
  git clone https://github.com/LEQN/dailyWallpaper.git
  cd <repository-directory>
```

2. **Ensure feh is Installed**:
   e.g.
```
   sudo apt-get install feh
```

3. **Prepare wallpapers directory**:

   create a directory e.g. '/home/leon/Pictures/wallpapers/'  which will only contain the desired wallpapers.

4. **Make the Script Executable**:
```
   chmod +x wallpaper_changer.py
```

## Usage
Open the script and change the img path variable to the absolute path of your wallpapers directory e.g.
```
imgs_path = "/home/leon/Pictures/wallpapers/"
```

Run the script manually to test it:
```
python3 /path/to/wallpaper_changer.py
```

### Setting Up the Script to Run on Startup

You can configure the script to run on startup using various methods. Here, we provide instructions for using the i3 window manager as an example.

1. Open the `i3` Configuration File:
   
   Probably in (~/.config/i3/config or ~/.i3/config).
   
2. Add the following line:
   ```
   exec_always --no-startup-id /usr/bin/python3 /path/to/wallpaper_changer.py
   ```
   Replace /path/to/wallpaper_changer.py with the absolute path to your script.
