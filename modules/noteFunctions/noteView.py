from colorama import Fore
import os

def noteView():
    noteName = input(Fore.RED+'NoteMan Command Line > Enter note name > ')

    print(Fore.RESET)
    os.system(f"cat storage/{noteName}.txt")

    input(Fore.RED+'Press any key to contine')