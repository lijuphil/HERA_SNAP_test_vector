import socket
import struct
import pylab as plt
import numpy as np

#host = 'acme1.digilab.pvt'
host = socket.gethostbyname(socket.gethostname())
port = 5555
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host,port))

while True:
        print 'Waiting for connection...'

# Receiving header+payload
        data, addr = sock.recvfrom(1032)	
	header = struct.unpack('>Q',data[0:8])[0]
	payload = struct.unpack('>1024B',data[8:1032])

	ts_mask = 0xfffffffff8000000 
        timestamp = header & ts_mask
	timestamp = timestamp >> 27
        print 'timestamp =', timestamp
        f_mask = 0x0000000007ff0000 
        freq = header & f_mask
	freq = freq >> 16
        print 'frequency =', freq
        a_mask = 0xffff
        ant = header & a_mask
        print 'antenna =', ant

	print payload
