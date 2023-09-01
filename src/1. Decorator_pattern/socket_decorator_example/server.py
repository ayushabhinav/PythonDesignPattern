import socket
from logging_socket import LogSocket
from gzip_socket import GzipSocket


##### server code to send a number to client  - Core implementation #######
def respond(client):
    response = input('Enter a value:')
    print(response)
    response = int(response) * 2
    print(response)
    client.send(bytes(str(response), 'utf-8'))
    client.close()
    

#### binding the sever to a ip and port ######
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2401))
server.listen(1)


#### continuously listening and responding  
try:
    
    while True:
        print('listening...')
        client, addr = server.accept()
        # respond(client)    # original implementation
        
        # These will decorate the client with individual decorator
        respond(LogSocket(client)) # decorated with the logging decorator
        # respond(GzipSocket(client)) # decorated with the gzip decorator
        
        # This will create the chain operation where original client will be 
        # decorated by logsocket and then it will be decorated by gzipsocket if condition meets
        log_send = True
        compress_host = []
        
        if log_send:
            client = LogSocket(client)
        if client.getpeername()[0] in compress_host:
            client = GzipSocket(client)
        respond(client)
        
finally:
    server.close()