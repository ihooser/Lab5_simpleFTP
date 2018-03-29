'''
Created on Mar 17, 2018

@author: SYSTEM
'''


def outfile(data):
    datafile = raw_input('Enter the file to write to:') 
    if os.path.isfile(datafile):
        print 'this file already exists'
        choose = raw_input('would you like to over write (Y/N):')
        if choose == "y" or choose== "Y":
            date = open(datafile,'w')
            date.write(data)
            date.close
            return  
        else:
            outfile(data)
    else:
        date = open(datafile,'w')
        date.write(data)
        date.close
        return


import re
import socket
import sys
import os
if __name__ == '__main__':
    pass

UDP_PORT_NO = int(sys.argv[1])
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
    print "Would you like to recive a file from"
    print addr
    choose = raw_input("(Y/N):")
    if choose == "y" or choose== "Y":
        data = ""
        while 1:
            datain = connection.recv(1024)
    
            data = data + str(datain)
            print data
    #        return_message = "The data has fully been sent"
    #        connection.send(return_message)
            if not datain:
                outfile(data)
    #             serverSock.connect(connection)
    #             return_message = "The data has fully been sent"
    #             serverSock.send(return_message)
                print "Recived all data"
    #             return_message = "The data has fully been sent"
    #             connection.send(return_message)
                break
        else: break
       
    

