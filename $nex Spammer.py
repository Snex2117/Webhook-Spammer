
import time
from time import sleep
import sys
import os
import requests
import colorama
from colorama import Fore, init
os.system(f'cls & mode 125,30 & title $nex#2117 SPAMMER ┃ https://discord.gg/3PJAQn94FZ')
os.system('cls' if os.name == 'nt' else 'clear')
init(convert=True)
colorama.init(autoreset=True)
print(f"{Fore.LIGHTYELLOW_EX}                                                                                                       Credits:TheSoap1#6666")
print(f"{Fore.LIGHTRED_EX}                                                                                              ")
print(f"{Fore.LIGHTRED_EX}                                                                                              ")
print(f"{Fore.LIGHTRED_EX}                                                                                              ")
sleep(0.01)
print(f"{Fore.LIGHTRED_EX}                                                                                                     ")
print(f"{Fore.LIGHTRED_EX}                                                                                              ")
sleep(0.00)
print(f"{Fore.LIGHTRED_EX}                              ______________________________________________________________                                                                ")
print(f"{Fore.LIGHTGREEN_EX}                              ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░")
sleep(0.00)
print(f"{Fore.LIGHTGREEN_EX}                              ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗")
sleep(0.00)
print(f"{Fore.LIGHTGREEN_EX}                              ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝")
sleep(0.01) 
print(f"{Fore.LIGHTGREEN_EX}                              ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗")
sleep(0.01)
print(f"{Fore.LIGHTGREEN_EX}                              ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║")
sleep(0.01)
print(f"{Fore.LIGHTGREEN_EX}                              ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝")
print(f"{Fore.LIGHTRED_EX}                              ______________________________________________________________                                                                ")
sleep(0.1)
print(f"{Fore.LIGHTYELLOW_EX}        ")
sleep(0.0)
print(f"{Fore.LIGHTYELLOW_EX}        ")
sleep(0.0)
print(f"{Fore.LIGHTYELLOW_EX}        ")
sleep(0.0)
sleep(0.2)
print(f'{Fore.BLUE}\n               {Fore.MAGENTA}[{Fore.MAGENTA}1{Fore.MAGENTA}] {Fore.RED}Webhook Spammer{Fore.RESET}           		{Fore.YELLOW}\n')
print(f'{Fore.MAGENTA}\n               [{Fore.MAGENTA}2{Fore.MAGENTA}] {Fore.RED}Webhook Deleter		{Fore.RED}\n')         
print(f"{Fore.LIGHTYELLOW_EX}        ")
sleep(0.0)
print(f"{Fore.LIGHTYELLOW_EX}        ")
sleep(0.0)
print(f'     {Fore.LIGHTGREEN_EX}[>] {Fore.MAGENTA}', end='')
choice = int(input(''))

if choice not in [1, 2]:
    print(f'{Fore.LIGHTGREEN_EX}--------------------------------------------------------\n{Fore.MAGENTA}Option{Fore.RESET} = {Fore.RED}Error{Fore.RESET} : Invalid Choice!')
    time.sleep(1)
    print(f"{Fore.BLUE}Exiting...")
    time.sleep(3)

if choice == 1:
    print(f"{Fore.MAGENTA} \n{Fore.RESET} {Fore.MAGENTA}[1]{Fore.RESET}{Fore.LIGHTGREEN_EX} Webhook URL:{Fore.RESET}")
    webhook = str(input(f"{Fore.LIGHTRED_EX}\n {Fore.RESET} "))
    sleep(0.0)
    print(f"{Fore.LIGHTGREEN_EX}           ")
    sleep(0.0)
    print(f"{Fore.LIGHTGREEN_EX}           ")
    print(f"{Fore.LIGHTGREEN_EX}           ")
    sleep(0.0)
    sleep(0.0)
    print(f"{Fore.MAGENTA} [2] {Fore.LIGHTGREEN_EX}Message ")
    message = str(input(f"{Fore.LIGHTGREEN_EX}\n {Fore.RESET} "))
    while True:
        _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
        if _data.status_code == 204:
            print(f'[{Fore.LIGHTGREEN_EX} $nex SPAMMER {Fore.RESET}] [{Fore.LIGHTGREEN_EX} Message Sent!')

if choice == 2:
  print(f"{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.LIGHTGREEN_EX} Webhook URL:{Fore.RESET}")
  webhook = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
  requests.delete(webhook)
  print(f"{Fore.LIGHTGREEN_EX}Done! {Fore.RED}\nExiting now...")
  sleep(300)
  exit()
 