import socket
# this method connect s to localhost
host = socket.gethostname()
# port on which we want to listen on
port = 9337


# creating a socket object in which we define address family(AF) and type of socket
# socket.SOCK_STREAM is used for TCP connection
# socket.SOCK_DGRAM is used for UDP connection
sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_.bind((host, port))
# listen for incoming connections
# 1 here denotes unaccepted connections before the server starts refusing new connections
sock_.listen(1)

print "\n Server started...\n"

# accepting connections
# means we accept connections from client socket con and it's address addr once connection is established
conn, addr = sock_.accept()

print "Connection established with: ", str(addr)

# sending a message
message = "\nThank you for connecting"+str(addr)
# encoding the msg in ascii because we are in python
conn.send(message.encode("ascii"))
conn.close()
