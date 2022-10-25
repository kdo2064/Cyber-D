import os
from time import time
import time



# logos
logo= """
   ____      _                    ____  
  / ___|   _| |__   ___ _ __     |  _ \ 
 | |  | | | | '_ \ / _ \ '__|____| | | |
 | |__| |_| | |_) |  __/ | |_____| |_| |
  \____\__, |_.__/ \___|_|       |____/ 
       |___/                     [ ~v1.2] 
                                                                             
 """

social_media= """
 ~ Instagram: https://instagram.com/kdo_shashank
 ~ Whatsapp: https://wa.me/+9779746554757
 ~ Telegram: https://t.me/kdobhai
"""

tool="""
|_______________ Installing _________________|
 ============================================
"""

success="""
|__________installation successful____________|
 =============================================
"""
can="""
|__________installation Cancelled____________|
 =============================================
"""
bye="""

 ▄▄▄▄ ▓██   ██▓▓█████ 
▓█████▄▒██  ██▒▓█   ▀ 
▒██▒ ▄██▒██ ██░▒███   
▒██░█▀  ░ ▐██▓░▒▓█  ▄ 
░▓█  ▀█▓░ ██▒▓░░▒████▒
░▒▓███▀▒ ██▒▒▒ ░░ ▒░ ░
▒░▒   ░▓██ ░▒░  ░ ░  ░
 ░    ░▒ ▒ ░░     ░   
 ░     ░ ░        ░  ░
      ░░ ░            

"""
os.system("pip install -r req.txt")
from termcolor import colored
print(colored(logo,"blue") + colored(social_media,"red"))

install=input(colored("Do you want to install Cyber-D (y/n):","yellow"))
if install == "y":
    print(colored(tool,"green"))
    os.system("pkg update -y && pkg upgrade -y && pkg install python3")
    os.system("cd $HOME && rm -rf Cyber-D")
    os.system("cd $HOME && mkdir .tools")
    os.system("cd $HOME && git clone https://github.com/kdo2006/Cyber-D")
    os.system("cd $HOME && cd Cyber-D && cd fun && pip install -r fun/req.txt")
    print(colored(success,"green"))
    time.sleep(0.5)
    os.system("cd $HOME && cd Cyber-D && python3 CyberD.py")
elif install=="n":
    print(colored(can,"green"))
    time.sleep(0.5)
    print(colored(bye,"yellow"))
else:
    print(colored("[!] Invalid Option, Try Again...","red"))
    time.sleep(0.4)
    os.system("clear")
    os.system("python3 setup.py")



