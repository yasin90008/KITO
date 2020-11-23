import os
import netifaces
import random
import time
import subprocess

Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'

line = "----------------------------------------------------------"

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def main():
    clr()
    logo="""
________              ______      ___       ____________________ 
___  __ \_____ __________  /__    __ |     / /__(_)__  ____/__(_)
__  / / /  __ `/_  ___/_  //_/    __ | /| / /__  /__  /_   __  / 
_  /_/ // /_/ /_  /   _  ,<       __ |/ |/ / _  / _  __/   _  /  
/_____/ \__,_/ /_/    /_/|_|      ____/|__/  /_/  /_/      /_/   
                                                                 
   ""","""
----------------------       ------------------------------
|      SecAnon       |       |     Version :  1.0Beta     |
----------------------       ------------------------------

\t        Created by Honey Pots...

---------------------------------------------------------- 
"""
    print(Red+logo[0]+Blue+logo[1])

main()
import sys
print(Blue)
list_argv = list(sys.argv)
nm = list_argv[1]+'mon'
command = 'sudo airodump-ng ' + nm 
os.system(command)

time.sleep(15)
def end():
    foo=raw_input()
    sys.exit()
end()
