'''
Created on Mar 17, 2018

@author: SYSTEM
'''



import sys
import socket
import os

if __name__ == '__main__':
    pass

# WHAT THE CRAP INDY
#s=socket.socket (socket.AF_INET, socket.SOCK_DGRAM,0)
#reading in all the imputs
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
datafile = sys.argv[3]
byte_reading= int(sys.argv[4])
#choosing if data is from keyboard or file

print "The server IP is:", serverIP
print "The server Port is:", serverPort


count = 0
#this is the file reading form
date = open(datafile,'rb')
#getting the size of the file in bytes
imformation = os.stat(datafile)
Size_of_file = imformation.st_size
print "The size of the file is: ", Size_of_file
#to know how many times to send the data chunks
counter_size = Size_of_file/byte_reading
remain = Size_of_file%byte_reading
print "the counter should go to: ",counter_size
#setting up the socket
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((serverIP, serverPort))
while date: 
    datain =date.read(byte_reading)
    clientSock.send(datain)
#     print datain
    count = count + 1
    if count == counter_size:
        datain =date.read(remain)
        clientSock.send(datain)
#         print datain
#         print "sent all data"
        
#        data_back = clientSock.recv(1024)
#        print data_back
        
        break

clientSock.close()
