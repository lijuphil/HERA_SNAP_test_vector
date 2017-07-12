import struct
import time
import os, sys
import socket
import numpy as np

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = socket.gethostbyname(socket.gethostname())
#ip = "acme1.digilab.pvt"
port = 5555
print 'Host at %s waiting for a connection on port %s...' %(ip,port)

#create 8-bytes header
ts = 0x64
ts = ts << 27
freq = 0x64
freq = freq << 16
ant = 0x64
h = ts + freq + ant

#create 1024-bytes payload
multi = []
all_chan = []

for i in range(16):
    x = np.arange(32)
    y = np.arange(32)
    interleave = np.ravel(np.column_stack((x,y)))
    multi.append(interleave) 
map(all_chan.extend, multi)
payload = struct.pack('>Q1024B' , h, *all_chan)

while True:
	try:
                sock.sendto(payload,(ip,port))
                print "Data sent to %s on port %s" %(ip, port)

        except ValueError:
                print "No data sent.  Try again..."
        time.sleep(5)

	
	
