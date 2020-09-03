import sys

ICMP_MS_SYNC_REQ_TYPE = 0xa5
#ICMP_MS_SYNC_RSP_TYPE = 0xa6
try:
    from scapy.all import *
except Exception as e:
    print ("[*] You need install scapy first:\n[*] sudo pip install scapy ")
if __name__ == '__main__':
    try:
        check_ip = sys.argv[1]
        i = 0
        print ("[*] Trying Check for" + check_ip)
        send(IP(dst=check_ip)/ICMP(type=ICMP_MS_SYNC_REQ_TYPE),inter=2,count=3)     
        print ("[*] Check Over!! ")
    except Exception as e:
        print "[*] usage: sudo python exp.py " + check_ip
