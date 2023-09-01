import gzip
from io import BytesIO

class GzipSocket:
    def __init__(self, socket):
        self.socket = socket
        
    def send(self, data):
        buf = BytesIO()
        zip_file = gzip.GzipFile(fileobj=buf, mode='w')
        zip_file.write(data)
        zip_file.close()
        self.socket.send(buf.getvalue())
    
    def close(self):
        self.socket.close()
    