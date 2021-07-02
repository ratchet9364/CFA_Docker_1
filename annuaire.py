import socket

HOST = '127.0.0.1'
PORT_A = 234

PORT_1 = 345
PORT_2 = 2345

annuaire = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
annuaire.bind((HOST, PORT_A))

print('Socket is listening..')
annuaire.listen(5)

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect((HOST,PORT_1))

client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect((HOST,PORT_2))

 

while True:
    connexion, address = annuaire.accept()

    print('Connected to: ' + address[0] + ':' + str(address[1]))
    msgClient = connexion.recv(1024)
    int_val = int.from_bytes(msgClient, "big")
    if int_val == PORT_1:
        client1.send(PORT_2.to_bytes(2, byteorder="big"))
        client1.close()
    if int_val == PORT_2:
        client2.send(PORT_1.to_bytes(2, byteorder="big"))
        client2.close()
annuaire.close()
    
