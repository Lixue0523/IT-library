import socket

client = socket.socket()
host = socket.gethostname()
port = 12345

client.connect((host, port))
print client.recv(1024)
msg="message from client!"
client.send(msg.encode('utf-8'))
client.close()