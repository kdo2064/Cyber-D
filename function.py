import os
from termcolor import colored
import webbrowser
from logo import cont


def zphisher():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("git clone https://github.com/htr-tech/zphisher.git")
        os.system("cd zphisher && bash zphisher.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")
        
    
        
def Red_Hawk():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install php && pkg install php-curl && pkg install php-xml ")
        os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd RED_HAWK && php rhawk.php")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")
    
def ngrok():
    print("Hash_Cat")

def MaskPhish():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install php")
        os.system("git clone https://github.com/jaykali/maskphish")
        os.system("cd maskphish && bash maskphish.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def infect():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install python -y &&  pkg install python2 -y && pip install lolcat")
        os.system("git clone https://github.com/noob-hackers/infect")
        os.system("cd infect && bash infect.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def AndroRat():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install wget && wget && https://raw.githubusercontent.com/MasterDevX/java/master/installjava && bash installjava")
        os.system("git clone https://github.com/karma9874/AndroRAT.git")
        os.system("cd AndroRAT && pip install -r requirements.txt")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def IPTracker():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        ip=input(colored("Input the Ip:","red"))
        os.system("git clone https://github.com/lucasfarre/ip-tracker.git")
        os.system("cd ip-tracker")
        os.system("python iptracker.py"+ ip)
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def PyPhisher():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install git python3 php openssh -y")
        os.system("git clone https://github.com/KasRoudra/PyPhisher")
        os.system("cd PyPhisher && pip3 install -r files/requirements.txt && python3 pyphisher.py")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def kalimux():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install lolcat")
        os.system("git clone https://github.com/noob-hackers/kalimux")
        os.system("cd kalimux && sh kalimux.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def PhoneInfoga():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("git clone https://github.com/sundowndev/PhoneInfoga")
        os.system("cd PhoneInfoga && python3 -m pip install -r requirements.txt && phoneinfoga.py -h")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def T_Bomber():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install python -y  && git clone https://github.com/TheSpeedX/TBomb.git ")
        os.system("cd TBomb && ./TBomb.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def metasploit():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pkg install wget  && wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh ")
        os.system("chmod +x metasploit.sh && ./metasploit.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def mrphish():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install lolcat  && git clone https://github.com/noob-hackers/mrphish ")
        os.system("cd mrphish && bash setup && bash mrphish")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def IpHack():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install pyproxify && pip install ua-headers && pip install requests && pip install torpy==1.1.6 && pip install eventlet==0.33.1")
        os.system("wget --no-check-certificate https://raw.githubusercontent.com/mishakorzik/IpHack/main/install.sh")
        os.system("bash install.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def tunnel():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install lolcat  && git clone https://github.com/noob-hackers/tunnel")
        os.system("cd tunnel && bash tunnel.sh")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def Slowloris():
    user=input(colored("   Do you want to install it?(y/n):", "red"))
    if user=="y":
        web=input(colored(" example.com:","red"))
        os.system("git clone https://github.com/gkbrk/slowloris.git")
        os.system("cd slowloris")
        os.system("python3 slowloris.py" + web)
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def update():
    user=input(colored("   Do you want to Update Cyber-D?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME")
        os.system("git clone ")
        os.system("cd Cyber_D && pip3 install -r req.txt && python3 CyberD.py")
    elif user=="n":
        os.system("clear")
        os.system("python3 CyberD.py")

def contact():
    print(colored(cont,"green"))
    contacts=input(colored("Choose contact medium:","red"))
    if contacts==1:
        webbrowser.open("https://wa.me/+9779746554757")
    elif contacts==2:
        webbrowser.open("https://t.me/kdobhai")
    elif contacts==3:
        webbrowser.open("https://instagram.com/kdo_shashank")
    elif contacts==4:
        print("Coming Soon")

def exit():
    print(colored("Thanks","red") + colored(" For","green") + colored(" Using","blue"))
    os.system("exit")