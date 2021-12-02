import socket

target_host = '0.0.0.0' # Change this to the IP/URL you want to hit
target_port = 9998      # ''

# create a socket
# AF_INET means we are going to use a standard IPv4 connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client
client.connect((target_host,target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: ToxSec.com\r\n\r\n")

# receive data
response = client.recv(4096)

print(response.decode())
client.close()