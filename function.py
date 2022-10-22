import os
from termcolor import colored
import webbrowser
from logo import about1
from logo import about2
from logo import about3
from logo import about4
from logo import logo
from logo import social_media

def zphisher():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && git clone https://github.com/htr-tech/zphisher.git")
        os.system("cd .tools && cd zphisher && bash zphisher.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")
        
    
        
def Red_Hawk():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install php && pkg install php-curl && pkg install php-xml ")
        os.system("cd .tools && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system(" cd .tools && cd RED_HAWK && php rhawk.php")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")
    
def ngrok():
    print("Hash_Cat")

def MaskPhish():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install php")
        os.system("cd .tools && git clone https://github.com/jaykali/maskphish")
        os.system("cd .tools && cd maskphish && bash maskphish.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def infect():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install python -y &&  pkg install python2 -y && pip install lolcat")
        os.system("cd .tools && git clone https://github.com/noob-hackers/infect")
        os.system("cd .tools && cd infect && bash infect.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def AndroRat():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install wget && wget && https://raw.githubusercontent.com/MasterDevX/java/master/installjava && bash installjava")
        os.system("cd .tools && git clone https://github.com/karma9874/AndroRAT.git")
        os.system("cd .tools && cd AndroRAT && pip install -r requirements.txt")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def IPTracker():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        ip=input(colored("Input the Ip:","red"))
        os.system("cd .tools && git clone https://github.com/lucasfarre/ip-tracker.git")
        os.system("cd .tools && cd ip-tracker")
        os.system("python iptracker.py "+ ip)
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def PyPhisher():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install git python3 php openssh -y")
        os.system("cd .tools && git clone https://github.com/KasRoudra/PyPhisher")
        os.system("cd .tools && cd PyPhisher && pip3 install -r files/requirements.txt && python3 pyphisher.py")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def kalimux():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install lolcat")
        os.system("cd .tools && git clone https://github.com/noob-hackers/kalimux")
        os.system("cd .tools && cd kalimux && sh kalimux.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def PhoneInfoga():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && git clone https://github.com/sundowndev/PhoneInfoga")
        os.system("cd .tools && cd PhoneInfoga && python3 -m pip install -r requirements.txt && phoneinfoga.py -h")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def T_Bomber():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install python -y  && cd .tools && git clone https://github.com/TheSpeedX/TBomb.git ")
        os.system("cd .tools && cd TBomb && ./TBomb.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def metasploit():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install wget  && wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh ")
        os.system("chmod +x metasploit.sh && ./metasploit.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def mrphish():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install lolcat  && cd .tools && git clone https://github.com/noob-hackers/mrphish ")
        os.system("cd .tools && cd mrphish && bash setup && bash mrphish")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def IpHack():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install pyproxify && pip install ua-headers && pip install requests && pip install torpy==1.1.6 && pip install eventlet==0.33.1")
        os.system("wget --no-check-certificate https://raw.githubusercontent.com/mishakorzik/IpHack/main/install.sh")
        os.system("bash install.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def tunnel():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install lolcat  && cd .tools && git clone https://github.com/noob-hackers/tunnel")
        os.system("cd .tools && cd tunnel && bash tunnel.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def Slowloris():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        web=input(colored("example.com:","red"))
        os.system("cd .tools && git clone https://github.com/gkbrk/slowloris.git")
        os.system("cd slowloris")
        os.system("python3 slowloris.py " + web)
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def social_box():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && git clone https://github.com/samsesh/SocialBox-Termux.git")
        os.system("cd .tools && cd SocialBox-Termux && chmod +x install-sb.sh")
        os.system("./install-sb.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def update():
    user=input(colored("Do you want to Update Cyber-D?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && rm -rf Cyber-D && git clone https://github.com/kdo2064/Cyber-D.git")
        os.system("cd $HOME/Cyber-D && python3 setup.py")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")
def exit():
    print(colored("Thanks","red") + colored(" For","green") + colored(" Using the Tool","blue"))
    os.system("exit")

def about():
    os.system("clear")
    print(colored(logo,'blue') + colored(social_media,'red'))
    print(colored(about1,"green",attrs=['reverse', 'blink']) + (colored(about2,"yellow")) + (colored(about3,"red",attrs=['reverse', 'blink'])) + (colored(about4,"blue")))
    what=input(colored("{0}--exit:","yellow"))
    if what=="0":
        os.system("python3 CyberD.py")
    else:
        print(colored("[!] Invalid Option, Try Again...","red"))
        os.system("clear")
        os.system("python3 CyberD.py")
