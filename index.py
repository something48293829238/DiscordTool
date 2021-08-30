import os
import time
import colorama
from colorama import Fore, Style

colorama.init()
print(Fore.RED)
print("""██╗██████╗      ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
██║██╔══██╗    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║██████╔╝    ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
██║██╔═══╝     ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
██║██║         ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
╚═╝╚═╝          ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                        """)
print(Fore.LIGHTRED_EX)
input = input("Enter Discord User: ")
print("Checking SQL...")
time.sleep(15)
print("Found SQL Table!")
time.sleep(1)
print("Searching User Info...")
time.sleep(10)
print("Found IP: 1.1.1.1")
os.system("pause >nul")
