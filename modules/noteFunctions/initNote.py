import os
from colorama import Fore

def initNote(noteName):
    os.system(f"cd storage && touch {noteName}.txt")
    print(Fore.RED+'NoteMan Write Note > Note file created...')
    print(Fore.RED+'NoteMan Write Note > "ENDNOTE" To Exit Writing')

