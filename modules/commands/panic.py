import os
import time
from colorama import Fore

def panic():
    print(Fore.RED+'This action will delete all of your notes. Continue?')
    action = input('[Enter/Cancel]')
    
    if action == 'cancel':
        print('Canceling...')
        time.sleep(1)
    elif action == 'Cancel':
        print('Canceling...')
        time.sleep(1)
    elif action == 'n':
        print('Canceling...')
        time.sleep(1)
    elif action == 'no':
        print('Canceling...')
        time.sleep(1)
    elif action == 'stop':
        print('Canceling...')
        time.sleep(1)
    else:
        os.system('rm -r storage/*')
        print('all notes deleted!')
        time.sleep(1)