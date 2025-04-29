from colorama import Fore
import time

def noteEdit():
    
    noteName = input(Fore.RED+'NoteMan Edit Note > Enter Note Name > ')
    print(Fore.RED+'NoteMan Edit Note > "ENDNOTE" To Exit Editing')

    while True:
        noteInput = input(Fore.RED+f"NoteMan Edit Note > {noteName} > ")+"\n"
        noteLines = []
        
        if noteInput == 'ENDNOTE\n':
            noteFile = open(f"storage/{noteName}.txt", 'a')
            noteFile.close()
            
            print(Fore.RED+'NoteMan Edit Note > Note Edited!')
            time.sleep(1)
            break
        else:
            noteLines.append(noteInput)
            noteFile = open(f"storage/{noteName}.txt", 'a')
            noteFile.writelines(noteLines)

        