import os, glob, platform
# Display all SOURCE directories
os_name = platform.system()

if os_name =="Darwin":
    print("You're on a Macbook.")
    print("Your Source directories: ", glob.glob('/*'))

if os_name =="Linux":
    print("You're on a Linux or Container.")
    print("Your Source directories: ", glob.glob('/*'))


if os_name =="Windows":
    print("You're on Windows.")
    print("Your Source directories: ", glob.glob('c:\*'))

# Select which SOURCE directory to copy

# Display of DESTINATION directories

# Select which DESTINATION directory to paste

# back up 

input("Press ENTER to STOP.")