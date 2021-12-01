import socket

target_host = "www.ToxSec.com"
target_port = 80

# create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client
client.connect((target_host,target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: ToxSec.com\r\n\r\n")

# receive data
response = client.recv(4096)

print(response.decode())
client.close()