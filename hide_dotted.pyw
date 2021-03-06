"""
The program runs in infinite while loop and hides all files 
and directories in given directory which name starts with dot (.). 
Written for and tested on Windows 10.
"""

import subprocess
from os.path import expanduser, join
from time import sleep


def hide_dotted(dir_path): 
    """
    Hides all files and directories in given path which name starts with dot.

    :dir_path: path to parent directory
    """
    command = r'ATTRIB +H /d ' + join(dir_path, '.*')
    subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)


if __name__ == '__main__':
    
    DIRECTORY = expanduser("~")  # User's dir
    SLEEP_TIME = 10

    while True:
        hide_dotted(DIRECTORY)
        sleep(SLEEP_TIME)
