import socket
import sys,os
import select
import Queue
import iptc
from arg_pars import parse_arg
import smtplib

known_ports = [1, 5, 7, 18, 20, 21, 22, 23, 25, 29, 37, 42, 43, 49, 53,
 69, 70, 79, 80, 103, 108, 109, 110, 115, 118, 119, 137, 139, 143,
 150, 156, 161, 179, 190, 194, 197, 389, 396, 443, 444, 445, 458, 546, 547, 563, 569, 1080]
def _scan_ports(ip):
    remoteServerIP  = socket.gethostbyname(ip)
    ports = []
    try:
        for port in range(1,65534):
            if port in known_ports: #skip port if known
                continue
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                ports.append(port)
                sock.close()
            
    except KeyboardInterrupt:
        print ("exited!")
        sys.exit()
        
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()
    return ports

def _open_socks(ports):
    socks = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setblocking(0)
            sock.bind(('localhost', port))
            sock.listen(5)
            socks.append(sock)
        except socket.error:
            print("Can't connect to port" + str(port) + " maybe already in used")
            continue
    return socks

def _block_ip(ip):
    rule = iptc.Rule()
    match = iptc.Match(rule, "tcp")
    target = iptc.Target(rule, "DROP")
    rule.add_match(match)
    rule.target = target
    rule.src = ip
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    chain.insert_rule(rule)

def _send_mail(ip):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.login("youremailusername", "password")
    msg = "ip " + ip + " is trying to connect I'll block the connection for you"
    server.sendmail("you@gmail.com", "mariamnofal16@gmail.com", msg)
    
def run(args):
    farg, _ = parse_arg(args)
    
    print("Scanning For all 65534 ports")
    ports = _scan_ports("127.0.0.1")
    print("Open Ports:")
    print(ports)
    socks = _open_socks(ports)
    print("Listening on ports")
    rsocks,_,_ = select.select(socks, [], [])
    for s in rsocks:
        _, client_address = s.accept()
        _block_ip(client_address[0])
        _send_mail(client_address[0])


def help():
    print("Help Page")
    print("No arguments needed for this module")
