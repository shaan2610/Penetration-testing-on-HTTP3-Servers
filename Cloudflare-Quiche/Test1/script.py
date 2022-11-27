# Server : aioquic
# Link : https://pgjones.dev/

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

# Set Version number to zero (2nd, 3rd, 4th and 5th bytes in payload represent Version number)
listx[8] = '0'
listx[9] = '0'

# Join the list into str format again
x = ''.join(listx)

# Create a bytes object from str
bytesX = codecs.decode(x, 'hex_codec') 

# Modifying the packet load to new changed load
packet[Raw].load = bytesX

# Write the modified packet to a pcapng file
wrpcap('version_zero.pcapng', packet)

# Send the packet cnt number of times
cnt=1
while cnt > 0:
    sendp(packet)
    cnt -= 1