import os
import time
from colorama import Fore

def setupNoteMan():
    print(Fore.RED+'NoteMan > Setup started...')
    time.sleep(1)

    os.system('mkdir storage')
    print(Fore.RED+'NoteMan > Created storage dir...')
    time.sleep(1)

    os.system('python3 -m pip install colorama')
    print(Fore.RED+'NoteMan > Installed colorama...')
    time.sleep(1)

    os.system('sudo apt install git -y')
    print(Fore.RED+'NoteMan > Installed git...')
    time.sleep(1)
    print(Fore.RED+'NoteMan > Finished setup!')
    
    input(Fore.RED+'NoteMan > Press any key to continue...')