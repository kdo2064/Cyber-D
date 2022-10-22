import os
from termcolor import colored
from logo import cont


def zphisherop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && cd zphisher && bash zphisher.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("cd .tools && git clone https://github.com/htr-tech/zphisher.git")
            os.system("cd .tools && cd zphisher && bash zphisher.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")

    
        
def Red_Hawkop():
    user=input(colored("Do you have install Red Hawk?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && cd RED_HAWK && php rhawk.php")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pkg install php && pkg install php-curl && pkg install php-xml ")
            os.system("cd .tools && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system(" cd .tools && cd RED_HAWK && php rhawk.php")
        elif ask=="n":
            os.system("python3 CyberD.py")

    
def ngrokop():
    print("Hash_Cat")

def MaskPhishop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && cd maskphish && bash maskphish.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pkg install php")
            os.system("cd .tools && git clone https://github.com/jaykali/maskphish")
            os.system("cd .tools && cd maskphish && bash maskphish.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def infectop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
       os.system("cd .tools && cd infect && bash infect.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pkg install python -y &&  pkg install python2 -y && pip install lolcat")
            os.system("cd .tools && git clone https://github.com/noob-hackers/infect")
            os.system("cd .tools && cd infect && bash infect.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def AndroRatop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y": 
        p=input(colored("port:","yellow"))
        a=input(colored("apk name:","yellow"))
        os.system("cd .tools && cd AndroRAT &&  python3 androRAT.py -h")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pkg install wget && wget && https://raw.githubusercontent.com/MasterDevX/java/master/installjava && bash installjava")
            os.system("cd .tools && git clone https://github.com/karma9874/AndroRAT.git")
            os.system("cd .tools && cd AndroRAT && pip install -r requirements.txt")
        elif ask=="n":
            os.system("python3 CyberD.py")


def IPTrackerop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        ip=input(colored("Input the Ip:","red"))
        os.system("cd .tools && cd ip-tracker && python iptracker.py "+ ip)
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            ip=input(colored("Input the Ip:","red"))
            os.system("cd .tools && git clone https://github.com/lucasfarre/ip-tracker.git")
            os.system("cd .tools && cd ip-tracker && python iptracker.py "+ ip)
        elif ask=="n":
            os.system("python3 CyberD.py")


def PyPhisherop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && cd PyPhisher && python3 pyphisher.py")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pkg install git python3 php openssh -y")
            os.system("cd .tools && git clone https://github.com/KasRoudra/PyPhisher")
            os.system("cd .tools && cd PyPhisher && pip3 install -r files/requirements.txt && python3 pyphisher.py")
        elif ask=="n":
            os.system("python3 CyberD.py")


def kalimuxop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && cd kalimux && sh kalimux.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pip install lolcat")
            os.system("cd .tools && git clone https://github.com/noob-hackers/kalimux")
            os.system("cd .tools && cd kalimux && sh kalimux.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def PhoneInfogaop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && cd PhoneInfoga && phoneinfoga.py -h")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("cd .tools && git clone https://github.com/sundowndev/PhoneInfoga")
            os.system("cd .tools && cd PhoneInfoga && python3 -m pip install -r requirements.txt && phoneinfoga.py -h")
        elif ask=="n":
            os.system("python3 CyberD.py")



def T_Bomberop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && cd TBomb && ./TBomb.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pkg install python -y  && cd .tools && git clone https://github.com/TheSpeedX/TBomb.git ")
            os.system("cd .tools && cd TBomb && ./TBomb.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def metasploitop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        os.system("msfconsole")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pkg install wget  && wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh ")
            os.system("chmod +x metasploit.sh && ./metasploit.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")

def mrphishop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && cd mrphish && bash setup && bash mrphish")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
           os.system("pip install lolcat  && cd .tools && git clone https://github.com/noob-hackers/mrphish ")
           os.system("cd .tools && cd mrphish && bash setup && bash mrphish")
        elif ask=="n":
            os.system("python3 CyberD.py")


def IpHackop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && bash install.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pip install pyproxify && pip install ua-headers && pip install requests && pip install torpy==1.1.6 && pip install eventlet==0.33.1")
            os.system("cd .tools && wget --no-check-certificate https://raw.githubusercontent.com/mishakorzik/IpHack/main/install.sh")
            os.system("cd .tools && bash install.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def tunnelop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        os.system("cd .tools && cd tunnel && bash tunnel.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pip install lolcat  && cd .tools && git clone https://github.com/noob-hackers/tunnel")
            os.system("cd .tools && cd tunnel && bash tunnel.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def Slowlorisop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        web=input(colored("example.com:","red"))
        os.system("cd .tools && cd slowloris && python3 slowloris.py " + web)
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            web=input(colored("example.com:","red"))
            os.system("cd .tools && git clone https://github.com/gkbrk/slowloris.git")
            os.system("cd .tools && cd slowloris && python3 slowloris.py " + web)
        elif ask=="n":
            os.system("python3 CyberD.py")


def exitop():
    print(colored("Thanks","red") + colored(" For","green") + colored(" Using","blue"))
    os.system("python3 CyberD.py")
