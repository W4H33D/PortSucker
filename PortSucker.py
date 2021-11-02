#!/usr/bin/python3
import socket
import sys
from IPy import IP

usage = "PortSucker.py [Target IP Address] [Starting Port Range No] [Ending Port Range No]"
if (len(sys.argv) !=4):
	print(usage)
	sys.exit()

#<------Scanner ---------->

def scanner(address,port):
	try:
		s = socket.socket()
		s.settimeout(0.5)
		s.connect((address, port))
		print('Port '+str(port)+' is Open')
	except:
		pass

#<---------------------------------------------->


#<--------checking IP and also resolve the Ip address------------------->
def resolve_ip(ip):
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip)
	except:
		Print("Name Resolution Failed Check the Target Address Address")
		sys.exit()

#------------------------------------------------------------------------

#<-------------Multiple Target Scanner-----------------------------------
def multi_scanner(targets):
	resolved_ip = resolve_ip(targets)
	print("\n[Scanning Target] "+str(targets)+"("+str(resolved_ip)+")")
	for port in range(range_port_1,range_port_2 +1 ):
		scanner(resolved_ip, port)




#----------------------------------------------------------------------->


ipaddress = sys.argv[1]
range_port_1 = int(sys.argv[2])
range_port_2 = int(sys.argv[3])

if ',' in ipaddress:
	for ip_add in ipaddress.split(','):
		multi_scanner(ip_add)
else:
	resolved_ip = resolve_ip(ipaddress)
	for port in range(range_port_1,range_port_2 +1 ):
		scanner(resolved_ip, port)