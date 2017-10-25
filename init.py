"""
Helper to handle global constant reading from settings.conf, since that info
needs to be read by main, classes, and prettyCLI.
"""

import os

# Constants (default values)
PROGRAM_WIDTH = 80
BORDER_SYM = "="
ALERT_SYM = "*"

version = "1.00"


def read_settings():
    """Reads settings from settings.conf and sets global constants."""
    global PROGRAM_WIDTH, BORDER_SYM, ALERT_SYM
    for (cdir, sdirs, fs) in os.walk(os.getcwd()):
        if "settings.conf" not in fs:
            print("Configuration file not found... creating now.")
            with open("settings.conf", "w") as f:
                f.write("# Set program attributes such as width in window, and symbols used for styling.\n")
                f.write("# The demarcation between settings and their values are a single space, so to\n")
                f.write("# avoid breaking the program, do not use spaces in setting any values. Also,\n")
                f.write("# for BORDER_SYM and ALERT_SYM, set only single characters to avoid a nasty soup.\n\n")
                f.write("PROGRAM_WIDTH 120\n")
                f.write("BORDER_SYM =\n")
                f.write("ALERT_SYM *\n")
        break
    try:
        config = {}
        with open("settings.conf", "r") as f:
            data = f.readlines()
            for line in data:
                if line[0] == "#" or line[0] == "\n":
                    continue
                setting = line.strip().split()
                config[setting[0]] = setting[1]
        # Set values
        PROGRAM_WIDTH = int(config["PROGRAM_WIDTH"])
        BORDER_SYM = config["BORDER_SYM"]
        ALERT_SYM = config["ALERT_SYM"]
        print("Settings loaded successfully.")
    except:
        print("Configuration file not in readable state: delete settings.conf and allow program to rebuild.")
        raise SystemExit


read_settings()
