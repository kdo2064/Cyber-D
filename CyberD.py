from termcolor import colored
import os
#import requests
from logo import logo
from logo import social_media
from logo import tools
from function import about, update
from logo import toolsop
from logo import startedup
from function import exit
from function import about
#import openfunction
from openfunction import zphisherop
from openfunction import Red_Hawkop
from openfunction import ngrokop
from openfunction import MaskPhishop
from openfunction import infectop
from openfunction import AndroRatop
from openfunction import IPTrackerop
from openfunction import PyPhisherop
from openfunction import kalimuxop
from openfunction import PhoneInfogaop
from openfunction import T_Bomberop
from openfunction import metasploitop
from openfunction import mrphishop
from openfunction import IpHackop
from openfunction import tunnelop
from openfunction import Slowlorisop
from openfunction import exitop

# import function
from function import zphisher
from function import Red_Hawk
from function import ngrok
from function import MaskPhish
from function import infect
from function import AndroRat
from function import IPTracker
from function import PyPhisher
from function import kalimux
from function import PhoneInfoga
from function import T_Bomber
from function import metasploit
from function import mrphish
from function import IpHack
from function import tunnel
from function import Slowloris

os.system("clear")
print(colored(logo,'blue') + colored(social_media,'red') +colored(startedup,"green"))
open=input(colored("Choose a Option:","yellow"))
if open=="1":
    os.system("clear")  
    print(colored(logo,'blue') + colored(social_media,'red') + colored(toolsop,'green'))
    choose=input(colored("Choose a Option:",'yellow'))
    if choose == "1":
        zphisherop() 
    elif choose == "2":
        Red_Hawkop()
    elif choose == "3":
        ngrokop()
    elif choose == "4":
        MaskPhishop()
    elif choose == "5":
        infectop()
    elif choose == "6":
        AndroRatop()
    elif choose == "7":
        IPTrackerop()
    elif choose == "8":
        PyPhisherop()
    elif choose == "9":
        kalimuxop()
    elif choose == "10":
        PhoneInfogaop()
    elif choose == "11":
        T_Bomberop()
    elif choose == "12":
        metasploitop()
    elif choose == "13":
        mrphishop()
    elif choose == "14":
        IpHackop()
    elif choose== "15":
        tunnelop()
    elif choose== "16":
        Slowlorisop()
    elif choose == "0":
        update()
    elif choose== "999":
        exitop()
    else:
        print(colored("[!] Invalid Option, Try Again...","red"))
        os.system("clear")
        os.system("python3 CyberD.py")
    
elif open=="2":
    os.system("clear")  
    print(colored(logo,'blue') + colored(social_media,'red') + colored(tools,'green'))
    choose=input(colored("Choose a Option:",'yellow'))
    if choose == "1":
        zphisher() 
    elif choose == "2":
        Red_Hawk()
    elif choose == "3":
        ngrok()
    elif choose == "4":
        MaskPhish()
    elif choose == "5":
        infect()
    elif choose == "6":
        AndroRat()
    elif choose == "7":
        IPTracker()
    elif choose == "8":
        PyPhisher()
    elif choose == "9":
        kalimux()
    elif choose == "10":
        PhoneInfoga()
    elif choose == "11":
        T_Bomber()
    elif choose == "12":
        metasploit()
    elif choose == "13":
        mrphish()
    elif choose == "14":
        IpHack()
    elif choose== "15":
        tunnel()
    elif choose== "16":
        Slowloris()
    elif choose == "0":
        update()
    elif choose== "999":
        exitop()
    else:
        print(colored("[!] Invalid Option, Try Again...","red"))
        os.system("clear")
        os.system("python3 CyberD.py")

elif open=="00":
    exit()

elif open=="0":
    about()
else:
        print(colored("[!] Invalid Option, Try Again...","red"))
        os.system("clear")
        os.system("python3 CyberD.py")