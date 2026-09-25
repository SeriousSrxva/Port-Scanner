#port scanner script
#SeriousSrxva
import socket

target= str(input("Enter Target IP: "))
port= int(input("Please enter target port : "))

def port_scanner(target, x):
    scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scan.settimeout(5)
    if scan.connect_ex((target, x)):
        print("Port is closed")
    else:
        print("Port is open")

port_scanner(target, port)
