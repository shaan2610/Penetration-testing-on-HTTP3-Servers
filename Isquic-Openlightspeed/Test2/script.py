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

# Set Version number to two (2nd, 3rd, 4th and 5th bytes in payload represent Version number)
listx[8] = '0'
listx[9] = '2'

# Join the list into str format again
x = ''.join(listx)

# Create a bytes object from str
bytesX = codecs.decode(x, 'hex_codec') 

# Modifying the packet load to new changed load
packet[Raw].load = bytesX

# Write the modified packet to a pcapng file
wrpcap('version_two.pcapng', packet)

# Send the packet cnt number of times

cnt = 10000

for i in range(cnt):
    sendp(packet)