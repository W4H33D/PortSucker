#!/usr/bin/python3
import socket
import sys
from IPy import IP
import argparse
import time

# < -------------------------------------- Get Arguments ------------------------------------------------------------>
parser = argparse.ArgumentParser()
parser.add_argument('--target', '-t', type=str, required=True, help="Enter the Target IP Address or URL.You can "
                                                                    "specify multiple target simultaneously but "
                                                                    "separate them by comma(,)")
parser.add_argument('--port', '-p', type=int, required=True, help="Target Port Range to scan i.e '-p 1 100'", nargs=2)
args = parser.parse_args()

# ---------------------------------------------------------------------------------------------------------------------


# <------------------------------------------- Arguments Checker ----------------------------------------------->
if args.port[0] <= 0 or args.port[1] > 65535:
    print("[!!] Port Number Selection is Incorrect.\n"
          "[**] Port Number will not less then 0 and greater then 65535")
    sys.exit()
# -----------------------------------------------------------------------------------------------------------------


# <--------------------------------------------- PortSucker Banner ---------------------------------------------->
print(
    '''  
    @@@@@@@    @@@@@@   @@@@@@@   @@@@@@@   @@@@@@   @@@  @@@   @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@   
    @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@   @@@  @@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
    @@!  @@@  @@!  @@@  @@!  @@@    @@!    !@@       @@!  @@@  !@@       @@!  !@@  @@!       @@!  @@@  
    !@!  @!@  !@!  @!@  !@!  @!@    !@!    !@!       !@!  @!@  !@!       !@!  @!!  !@!       !@!  @!@  
    @!@@!@!   @!@  !@!  @!@!!@!     @!!    !!@@!!    @!@  !@!  !@!       @!@@!@!   @!!!:!    @!@!!@!   
    !!@!!!    !@!  !!!  !!@!@!      !!!     !!@!!!   !@!  !!!  !!!       !!@!!!    !!!!!:    !!@!@!    
    !!:       !!:  !!!  !!: :!!     !!:         !:!  !!:  !!!  :!!       !!: :!!   !!:       !!: :!!   
    :!:       :!:  !:!  :!:  !:!    :!:        !:!   :!:  !:!  :!:       :!:  !:!  :!:       :!:  !:!  
     ::       ::::: ::  ::   :::     ::    :::: ::   ::::: ::   ::: :::   ::  :::   :: ::::  ::   :::  
     :         : :  :    :   : :     :     :: : :     : :  :    :: :: :   :   :::  : :: ::    :   : :  
                                                                                                       
                                                                                          (By W4H33D)
    '''
    )
# ----------------------------------------------------------------------------------------------------------------

start_time = time.time()


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
        try:
            return socket.gethostbyname(ip)
        except:
            print("[!!] Name Resolution Failed. Check The Target ("+ip+")")
            sys.exit()
# ------------------------------------------------------------------------


# <-------------Multiple Target Scanner-----------------------------------
def multi_scanner(targets):
    multi_ip = resolve_ip(targets)
    print("\n[Scanning Target] " + str(targets) + "(" + str(multi_ip) + ")")
    print('Ports\t' + 'Status\t' + 'service')
    for multi_port in range(range_port_1, range_port_2 + 1):
        scanner(multi_ip, multi_port)
# ----------------------------------------------------------------------->



# <--------------------------- Main Working ------------------------------->
ipaddress = args.target
range_port_1 = int(args.port[0])
range_port_2 = int(args.port[1])

if ',' in ipaddress:
    for ip_add in ipaddress.split(','):
        multi_scanner(ip_add)
else:
    resolved_ip = resolve_ip(ipaddress)
    print("[Scanning Target] " + str(ipaddress) + "(" + str(resolved_ip) + ")\n")
    print('Ports\t' + 'Status\t' + 'service')
    for port in range(range_port_1, range_port_2 + 1):
        scanner(resolved_ip, port)
# ----------------------------------------------------------------------------
        
end_time = time.time()
total_time = end_time - start_time

print("Scan Complete in " + str(round(total_time)) + " sec")
