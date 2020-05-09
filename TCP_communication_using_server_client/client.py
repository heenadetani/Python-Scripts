import socket

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# specifying the port on which client wants to connect
sock_.connect((socket.gethostname(), 9337))
# receiving message from server i.e. first 1024 bytes
msg = sock_.recv(1024)
sock_.close()
# decoding message
print msg.decode("ascii")
