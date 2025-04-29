from colorama import Fore, Style, init

init(autoreset=True)

def getBanner():
    banner = """
 ____________________________________________________________________________
|                     _   _       _       __  __                             |
|                    | \ | | ___ | |_ ___|  \/  | __ _ _ __                  |
|                    |  \| |/ _ \| __/ _ \ |\/| |/ _` | '_ \                 |
|                    | |\  | (_) | ||  __/ |  | | (_| | | | |                |
|                    |_| \_|\___/ \__\___|_|  |_|\__,_|_| |_|                |
|                                 ___________                                |
|_________________________.______/   By Mar  \______.________________________|
|                          \_____   v 1.0.0   _____/                         |
|                                \_____._____/                               |
|                                      |                                     |
|       setup                          |      note write                     |
|       Sets up required packages      |      Writes a note of your choice   |
\______________________________________|_____________________________________/
|                                      |                                     |
|       note list                      |      note delete                    |
|       Displays available notes       |      Deletes a note of your choice  |
\______________________________________|_____________________________________/
|                                      |                                     |
|       note view                      |      note edit                      |
|       Displays contents of a note    |      Edits already existing note    |
\______________________________________|_____________________________________/
|                                      |                                     |
|       exit                           |      panic                          |
|       Exits NoteMan                  |      Deletes all notes              |
\______________________________________|_____________________________________/
"""
    print(Fore.RED+banner)