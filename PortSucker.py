#!/usr/bin/python3
import socket
import sys
from IPy import IP

usage = "usage: \n" \
        "PortSucker.py [Target IP Address] [Starting Port Range] [Ending Port Range]\n" \
        "PortSucker.py [Target IP1,TargetIP2,...] [Starting Port Range] [Ending Port Range]\n" \
        "Examples:\n" \
        "PortSucker.py 192.168.10.1 1 100\n" \
        "PortSucker.py 192.168.10.1,www.example.com,10.10.10.1 1 100"
if len(sys.argv) != 4:
    print(usage)
    sys.exit()
elif len(sys.argv) >= 5:
    print("[-] Invelid Parameters!")
    print(usage)

if int(sys.argv[2]) <= 0 or int(sys.argv[3]) > 65535:
    print("[-] Port Number must be in Between 1-65535")
    sys.exit()


# <---------------Banner Grabbing----------
def get_banner(s):
    return s.recv(1024)


# <--------------------------------------->

# <------Scanner ---------->
def scanner(address, scan_port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((address, scan_port))
        try:
            banner = get_banner(s)
            print(str(scan_port) + '\t' + 'Open\t' + str(banner.decode().strip('\n')))
        except:
            print(str(scan_port) + '\tOpen')
    except:
        pass


# <---------------------------------------------->


# <--------checking IP and also resolve the Ip address------------------->
def resolve_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


# ------------------------------------------------------------------------
# <-------------Multiple Target Scanner-----------------------------------
def multi_scanner(targets):
    multi_ip = resolve_ip(targets)
    print("\n[Scanning Target] " + str(targets) + "(" + str(multi_ip) + ")")
    print('Ports\t' + 'Status\t' + 'service')
    for multi_port in range(range_port_1, range_port_2 + 1):
        scanner(multi_ip, multi_port)


# ----------------------------------------------------------------------->


ipaddress = sys.argv[1]
range_port_1 = int(sys.argv[2])
range_port_2 = int(sys.argv[3])

if ',' in ipaddress:
    for ip_add in ipaddress.split(','):
        multi_scanner(ip_add)
else:
    resolved_ip = resolve_ip(ipaddress)
    print("[Scanning Target] " + str(ipaddress) + "(" + str(resolved_ip) + ")\n")
    print('Ports\t' + 'Status\t' + 'service')
    for port in range(range_port_1, range_port_2 + 1):
        scanner(resolved_ip, port)
