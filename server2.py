import socket, time

HOST = '127.0.0.1'
PORT_A = 234
PORT_1 = 0
PORT_2 = 2345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT_2))

print('Socket is listening..')
server.listen(5)

annuaire = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
annuaire.connect((HOST, PORT_A))

message = bytes("Ping", 'utf-8')


connexion, adresse = server.accept()

annuaire.send(PORT_2.to_bytes(2, byteorder="big"))
while PORT_1 == 0:
    msgClient = connexion.recv(1024)
    if msgClient != "":
        PORT_1 = int.from_bytes(msgClient, "big")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT_1))
        connexion.close()

connexion, adresse = server.accept()
client.send(message)

while True:
    msgClient = connexion.recv(1024)
    if msgClient:
        print(msgClient)
        time.sleep(0.5)
        client.send(message)

