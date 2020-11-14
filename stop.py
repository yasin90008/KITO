import os
import netifaces
import random
import time
import subprocess
import requests

Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'

line = "----------------------------------------------------------"
verl = open("core/.version", 'r').read()

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

   """,f"""
----------------------     -------------------------------
|      SecAnon       |     |   Version : {verl}     |
----------------------     -------------------------------

\t        Created by Honey Pots...

---------------------------------------------------------- 
"""
    print(Red+logo[0]+Blue+logo[1])

main()


interfaces = netifaces.interfaces()
lists = []
for i in interfaces:
    if i[-3:] == 'mon':
        lists.append(i)
    else:
        pass

monitro = lists[0] 


os.system(f'airmon-ng stop  {monitro}')
