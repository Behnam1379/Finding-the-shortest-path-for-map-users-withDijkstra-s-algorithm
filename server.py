from vertex import Vertex
from router import Router
import socket, threading
class Server:

    def __init__(self):
        self.__address_map = "Maps"
        self.router_object = Router(self.__address_map)

    def threaded(self, client : socket.socket, addr):
        while True:
            data = client.recv(2048)
            if data == b'exit':
                print('Conncetion to', addr[0], ':', addr[1], 'lost.')
                break

            data = data.decode().split()
            data = self.router_object.find_shortest_path(int(data[0]), int(data[1]))
            # print(b''.join([str(i).encode() for i in data]))
            client.sendall(b' '.join([str(i).encode() for i in data]))
        client.close()


    def start(self):
        host = '0.0.0.0'
        port = 1234
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.bind((host, port))
            print('socket binded to post', port)
            soc.listen(10)
            print('socket is listening...')

            while True:
                client, addr = soc.accept()
                threading.Thread(target=self.threaded, args=(client, addr)).start()




server__ = Server()
server__.start()