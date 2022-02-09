import os
import sys
from sys import flags, platform
from colorama import Fore
import time
import datetime
from halo import Halo

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

if platform == "linux":
    exe_str = "BINARY"
elif platform == "darwin":
    exe_str = "APP"
elif platform == "win32":
    exe_str = "EXE"


def create_executeable(compiler="", src="", output="", flags=""):
    print(color.GREEN + color.BOLD +  f"C Target: " + color.END + f"{src}")
    print(color.PURPLE + color.BOLD +  f"C Flags: " + color.END + f"{flags}")
    print(color.CYAN + color.BOLD + f"{exe_str} Target: " + color.END + f"{output}")
    time.sleep(0.5)
    spinner = Halo(text=f'{color.YELLOW + color.BOLD}Compiling {color.END}', spinner='bouncing')
    spinner.start()
    os.system(f"{compiler} {src} -o {output}")
    print(f"\n{color.YELLOW + color.BOLD}✔ Compiled")
    
    