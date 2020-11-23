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
________              ______      ___       ____________________ 
___  __ \_____ __________  /__    __ |     / /__(_)__  ____/__(_)
__  / / /  __ `/_  ___/_  //_/    __ | /| / /__  /__  /_   __  / 
_  /_/ // /_/ /_  /   _  ,<       __ |/ |/ / _  / _  __/   _  /  
/_____/ \__,_/ /_/    /_/|_|      ____/|__/  /_/  /_/      /_/   
                                                                 
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

if monitro[-3:] == 'mon' :
    mon = monitro.replace('mon','')
else:
    mon= monitro
os.system(f'sudo airmon-ng stop  {monitro}')
os.system(f'sudo macchanger -p {mon}')
print("\n" , line)
print("\nNow Everything is Normal ")
input("Please Enter To Exit : ")
