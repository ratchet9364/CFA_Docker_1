import socket, time

HOST_1 = '127.0.0.1'
PORT_1 = 234
HOST_2 = '127.0.0.2'
PORT_2 = 2345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST_2, PORT_2))
server.listen(5)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST_1, PORT_1))

message = bytes("Ping", 'utf-8')

connexion, adresse = server.accept()

client.send(message)
while True:

    msgClient = connexion.recv(1024)
    if msgClient: 
        print(msgClient)
        time.sleep(0.5)
        client.send(message)

