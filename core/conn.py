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
 __   __  ___   __          ___      __       ___      ___ 
|"  |/  \|  "| |" \        |"  |    /""\     |"  \    /"  |
|'  /    \:  | ||  |       ||  |   /    \     \   \  //   |
|: /'        | |:  |       |:  |  /' /\  \    /\\  \/.    |
 \//  /\'    | |.  |    ___|  /  //  __'  \  |: \.        |
 /   /  \\   | /\  |\  /  :|_/ )/   /  \\  \ |.  \    /:  |
|___/    \___|(__\_|_)(_______/(___/    \___)|___|\__/|___|

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
command = 'airodump-ng ' + nm 
os.system(command)

time.sleep(15)
def end():
    foo=raw_input()
    sys.exit()
end()