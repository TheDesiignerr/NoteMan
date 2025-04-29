from colorama import Fore
import os

def noteList():
    print(Fore.RED+'NoteMan Command Line > Scanning notes...')
    os.system('ls storage/')
    input(Fore.RED+'Press any key to continue')