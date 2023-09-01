
class LogSocket:
    def __init__(self, socket):
        self.socket = socket
        
    def send(self, data):
        print(f"sending {data} to {self.socket.getpeername()[0]}")
        self.socket.send(data)
    
    def close(self):
        self.socket.close()