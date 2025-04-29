import os
import time
from colorama import Fore

from modules.banner.getBanner import getBanner

from modules.commands.setup import setupNoteMan
from modules.commands.panic import panic

from modules.noteFunctions.noteWrite import noteWrite
from modules.noteFunctions.noteList import noteList
from modules.noteFunctions.noteView import noteView
from modules.noteFunctions.noteDelete import noteDelete
from modules.noteFunctions.noteEdit import noteEdit

while True:
    os.system('clear')
    getBanner()

    action = input(Fore.RED+'NoteMan Command Line > ')

    if action == 'setup':
        setupNoteMan()
    elif action == 'note write':
        noteWrite()
    elif action == 'note list':
        noteList()
    elif action == 'note view':
        noteView()
    elif action == 'note delete':
        noteDelete()
    elif action == 'note edit':
        noteEdit()
    elif action == 'panic':
        panic()
    elif action == 'exit':
        print('NoteMan Exiting...')
        time.sleep(1)
        break
    else:
        print('NoteMan: Unknown command entered!')
        time.sleep(1)
        

