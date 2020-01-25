import socket
import subprocess
import sys,os
from datetime import datetime
from arg_pars import parse_arg

def _scan_remote_ip(ip):
    remoteServerIP  = socket.gethostbyname(ip)

    # Print a nice banner with information on which host we are about to scan
    print ("-" * 60)
    print ("Please wait, scanning remote host", remoteServerIP)
    print ("-" * 60)
    try:
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print ("Port {}: 	 Open".format(port))
                nmapR = (os.popen('nmap -sC -sV -p '+str(port)+" "+remoteServerIP).read()).split("\n")[5]
                print(nmapR)
                sock.close()
            
    except KeyboardInterrupt:
        print ("exited!")
        sys.exit()
        
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()


def run(args):
    farg, link= parse_arg(args)
    start_ip = raw_input("Enter Start ip address")
    range_ip = int(raw_input("Enter Range"))
    rmip_start = int(start_ip.split('.')[3])
    current_ip = start_ip.split('.')
    if farg is not None:
            sys.stdout = open(farg, 'w')
    for rmip in range(rmip_start, rmip_start + range_ip):
        current_ip[3] = str(rmip)
        _scan_remote_ip(".".join(current_ip))
    sys.stdout = sys.__stdout__


def help(args):
    print("Help Page")
    print("No parms input are taken from the module")



