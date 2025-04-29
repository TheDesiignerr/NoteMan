from colorama import Fore
import os
import time

def noteDelete():
    noteName = input(Fore.RED+'NoteMan Note Delete > Enter Note Name > ')
    os.system(f"rm storage/{noteName}.txt")
    print(Fore.RED+f"Deleted {noteName}")
    time.sleep(1)
