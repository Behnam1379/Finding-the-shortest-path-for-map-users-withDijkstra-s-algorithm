import socket
from show_final import Show

host = '127.0.0.1'
port = 1234
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect((host, port))

while True:
    message = input("Enter start id and end_id by whit tuple : ")
    soc.sendall(message.encode('ascii'))
    if message == 'exit':
        break

    data = soc.recv(2048)
    array_shorter_path = data.decode()
    show_ = Show("Maps",  [int(i) for i in array_shorter_path.split()])
    show_.show()

    print('Received from the server :', str(data.decode('ascii')), '\n')

    ans = input('Do you want to continue(y/n) :')
    if ans == 'y':
        continue
    else:
        soc.sendall(b'exit')
        break

soc.close()