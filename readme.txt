Lab5 Simple FTP
code written by: Indiana Hooser

data file tested "data"

Client:
The client will be receiving data from a file in changeable byte sections. It is up to the user. This data will then be  sent to the Server bytes at a time. When it is done it will receive a reply form the server stateing it is done.
-arguments
	Server_IP-adress Server-port_Number data_file_reading #_Bytes_read_at_a_time
	(example and tested)
	10.1.225.29 5005 data 10
-notes
	1) The data file with the original data must be in same folder as the script
	2) If the client is rejected have another client run. this will reset the client and it will be able to send again
	3) this client can run as many times as it wants to. when it is done you can run it again
Server:
The server will receive data from a client. This data will contain a section of the file being sent. The server will then save that information and build up a string untill all of the file is sent. then it will send an acknolegment back to the client
-arguments
	Server_port_number
	(example and tested)
	5005
	(note) this port number must be the same Server port number stated in the client.
-notes
	1) if a client is regected, another client must be sent befor it can be read from again
	2) if the output file is alarady used there will be the option to over write or to chose a differnt file name
	3) when the client has sent all the data it will save that data to a file and send an acknolegement to the client
	4) This server only works with 2 clients at a time