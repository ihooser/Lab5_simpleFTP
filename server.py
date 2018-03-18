'''
Created on Mar 17, 2018

@author: SYSTEM
'''

import re
import socket
import sys
if __name__ == '__main__':
    pass
data = ""
UDP_PORT_NO = int(sys.argv[1])
datafile = sys.argv[2]
print " the server port is: ", UDP_PORT_NO

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#getting the ip of the Server
sock = socket.gethostbyname(socket.gethostname())
UDP_IP_ADDRESS = sock
print sock
#binding together the ip and the port for this server
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
while True:
    serverSock.listen(2)
    print "_______________________________"
    print "WAITING for client"
    connection, addr = serverSock.accept()
    while 1:
        datain = connection.recv(1024)

        data = data + str(datain)
        print data
        date = open(datafile,'w')
        date.write(data)
        date.close
        if not datain:
            break
    

