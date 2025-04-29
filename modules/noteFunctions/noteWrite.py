from colorama import Fore
from modules.noteFunctions.initNote import initNote
import time

def noteWrite():
    print(Fore.RED+'NoteMan Write Note > No Spaces Allowed.')
    
    noteName = input(Fore.RED+'NoteMan Write Note > Enter Note Name > ')
    initNote(noteName)

    while True:
        noteInput = input(Fore.RED+f"NoteMan Write Note > {noteName} > ")+"\n"
        noteLines = []
        
        if noteInput == 'ENDNOTE\n':
            noteFile = open(f"storage/{noteName}.txt", 'a')
            noteFile.close()
            
            print(Fore.RED+'NoteMan Write Note > Note Saved!')
            time.sleep(1)
            break
        else:
            noteLines.append(noteInput)
            noteFile = open(f"storage/{noteName}.txt", 'a')
            noteFile.writelines(noteLines)

        