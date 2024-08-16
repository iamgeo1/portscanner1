import socket
import pyfiglet 
import sys 
import socket 
from colorama import Fore, Style, init

# Initialize colorama
init()

# Define your ASCII art
ascii_art =(""" ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
|  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
| |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
|  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
|_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\

""")

# Print ASCII art in different colors
print(Fore.CYAN + ascii_art + Style.RESET_ALL)  # Cyan text


from datetime import datetime
print("made by iamgeo1")
print("only use this for secruity reasons")
print("for any advice add @geo1ge on snapchat.com")
# Input the target IP address
target_ip = (input("Target IP:"))
#Input port range
start_port = int(input("Start Port:"))
end_port = int(input("End Port:"))

def port_scanner(target_ip, start_port, end_port):

    for port in range(start_port, end_port+1):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)

        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        sock.close()
        
port_scanner(target_ip, start_port, end_port)