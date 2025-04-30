#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="192.168.1.10", dst="192.168.1.20")
tcp = TCP(sport=1234, dport=80, flags="S", seq=1000)
pkt = ip/tcp
ls(pkt)
send(pkt, verbose=0)
