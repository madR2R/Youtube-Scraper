import colorama
import time
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#import other functions
import main

#Main Menu Display
print(Fore.CYAN+"""
████████████████████████████████████████████████████████████████████████████████████████
█▄─█─▄█─▄▄─█▄─██─▄█─▄─▄─█▄─██─▄█▄─▄─▀█▄─▄▄─███─▄▄▄▄█─▄▄▄─█▄─▄▄▀██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀█
██▄─▄██─██─██─██─████─████─██─███─▄─▀██─▄█▀███▄▄▄▄─█─███▀██─▄─▄██─▀─███─▄▄▄██─▄█▀██─▄─▄█
▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀""")

print("-----------------------------------------------------------------------------------------")
menu = {}
menu['[1]']="Get Youtube Video Links (30 video maximum)" 
menu['[2]']="Play Youtube Video"
menu['[3]']="Exit"

while True: 
    options=menu.keys()
    for entry in options: 
        print(entry, menu[entry])

    selection=input("Please Select: ") 
    if selection =='1': 
        main.scrapeYoutubeChannel()
        print('Youtube links saved to .txt file! \n')
    elif selection == '2': 
        main.playVideo()
    elif selection == '3':
        print(Fore.YELLOW+"Thank you for using our script!")
        time.sleep(3) 
        break
    else: 
        print(Fore.RED+"Invalid Keyword!")