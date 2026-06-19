import os
import sys
import time
import math
import signal

RED = '\u001B[31m'
GREEN = '\u001B[32m'
ORANGE = '\u001B[33m'
MAGENTA = '\u001B[35m'
CYAN = '\u001B[36m'

def banner():
    print(f"\n{CYAN}°|================{GREEN} Temperature Unit Converter{CYAN}================|°")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def exit_on_signal(signum, frame):
    if signum == signal.SIGINT:
        print(f"\n\n{RED}[{RED}!{RED}] {RED} Program Interrupted!")
        
    elif signum == signal.SIGTERM:
        print(f"\n\n{RED}[{RED}!{RED}]{RED} Program Terminated!")
        
    sys.exit(0)
    
# setup signal handlers 
signal.signal(signal.SIGINT, exit_on_signal)
signal.signal(signal.SIGTERM, exit_on_signal)

def Tc_to_Tf():
    clear_console()
    banner()
    print(f"\n{CYAN} Ctrl + C {ORANGE} To exit...")
    while True:
        try:
            Tc = float(input(f"\n{ORANGE}Enter °C: {GREEN}"))
            Tf = 9 / 5 * Tc +32
            print(f"\n{ORANGE}  °F = {CYAN}{Tf}°F")
            print()
        except ValueError:
            print(f"\n{RED}[!]{MAGENTA} Invalid input! Try again....")
            time.sleep(1)
            clear_console()
            Tc_to_Tf()

def Tc_to_Tk():
    clear_console()
    banner()
    print(f"\n{CYAN} Ctrl + C {ORANGE} To exit...")
    while True:
        try:
            Tc = float(input(f"\n{ORANGE} Enter °C: "))
            Tk = Tc + 273
            print(f"\n{ORANGE}  K: {CYAN}{Tk}K")
            
        except ValueError:
             print(f"\n{RED}[!]{MAGENTA} Invalid input! Try again....")
             time.sleep(1)
             clear_console()
             Tc_to_Tk()
def Tf_to_Tc():
    clear_console()
    banner()
    print(f"\n{CYAN} Ctrl + C {ORANGE} To exit...")
    while True:
        try:
            Tf = float(input(f"\n{ORANGE} Enter °F: "))
            Tf = Tf -32
            Tc = Tf * 5 / 9
            print(f"\n{ORANGE}  °C: {CYAN}{Tc}°C")
            
        except ValueError:
             print(f"\n{RED}[!]{MAGENTA} Invalid input! Try again....")
             time.sleep(1)
             clear_console()
             Tf_to_Tc()
def Tf_to_Tk():
    clear_console()
    banner()
    print(f"\n{CYAN} Ctrl + C {ORANGE} To exit...")
    while True:
        try:
            Tf = float(input(f"\n{ORANGE} Enter °F: "))
            Tf = Tf -32
            Tf = Tf * 5 / 9
            Tk = Tf + 273
            print(f"\n{ORANGE}  K: {CYAN}{Tk}K")
            
        except ValueError:
             print(f"\n{RED}[!]{MAGENTA} Invalid input! Try again....")
             time.sleep(1)
             clear_console()
             Tf_to_Tk()
def Tk_to_Tc():
    clear_console()
    banner()
    print(f"\n{CYAN} Ctrl + C {ORANGE} To exit...")
    while True:
        try:
            Tk = float(input(f"\n{ORANGE} Enter K: "))
            Tc = Tk - 273
            print(f"\n{ORANGE}  °C: {CYAN}{Tc}°C")
            
        except ValueError:
             print(f"\n{RED}[!]{MAGENTA} Invalid input! Try again....")
             time.sleep(1)
             clear_console()
             Tk_to_Tc()
    
def Tk_to_Tf():
    clear_console()
    banner()
    print(f"\n{CYAN} Ctrl + C {ORANGE} To exit...")
    while True:
        try:
            Tk = float(input(f"\n{ORANGE} Enter K: "))
            Tk = Tk - 273
            Tk = 9 / 5 * Tk
            Tf = Tk + 32
            print(f"\n{ORANGE}  °F: {CYAN}{Tf}°F")
            
        except ValueError:
             print(f"\n{RED}[!]{MAGENTA} Invalid input! Try again....")
             time.sleep(1)
             clear_console()
             Tk_to_Tf()
             
def follow():
    print(f"""\n  {ORANGE}GitHub: {CYAN}https://github.com/Bereket635
""")
    
    
def type_writer(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    
def about():
    clear_console()
    banner()
    type_writer(f"\n{GREEN}I'm highschool student, who's curious about programming, cyber security 😁 .....")
    
def main():
    clear_console()
    banner()
    
    main_menu = [
        ("Temperature Units Converter", "01"),
        ("Follow me on social media", "02"),
        ("About me", "03")
    ]
    
    for i, (name1, code1) in enumerate(main_menu, 1):
        print(f"{RED}[{ORANGE}{code1}{RED}]{ORANGE} {name1}", end="")
        if i % 1 == 0:
            print()
        else:
            print("   ", end="")
            
    reply = input(f"\n{RED}>>> {ORANGE}Select an option: {GREEN}").strip()
    reply = reply.lstrip("0")
    if reply == '1':
        menu()
    elif reply == '2':
        follow()
    elif reply == '3':
        about()
    else:
        print(f"\n{RED}[!]{MAGENTA} Invalid option! try again...")
        time.sleep(1)
        clear_console()
        main()
    

def menu():
    clear_console()
    print()
    banner()
    
    menu_options = [
       ("T°C to T°F", "01"),
       ("T°C to TK", "02"),
       ("T°F to T°C", "03"),
       ("T°F to TK", "04"),
       ("TK  to T°C", "05"),
       ("TK  to T°F", "06")
    ]
    
    for i, (name, code) in enumerate(menu_options, 1):
        print(f"{RED}[{ORANGE}{code}{RED}]{ORANGE} {name}")
        
    reply = input(f"{RED}>>> {ORANGE}Select an option: {GREEN}")
    reply = reply.lstrip("0")
    if reply == '1':
        Tc_to_Tf()
    elif reply == '2':
        Tc_to_Tk()
    elif reply == '3':
        Tf_to_Tc()
    elif reply == '4':
        Tf_to_Tk()
    elif reply == '5':
        Tk_to_Tc()
    elif reply == '6':
        Tk_to_Tf()
    else:
        print(f"{RED}[!] {MAGENTA} Invalid option! try again...")
        time.sleep(1)
        clear_console()
        menu()
        
main()