import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting...')
client.connect(('localhost', 2401))
print('connected.')

recevied = client.recv(1024)
print(f'Received:{recevied}')
client.close()