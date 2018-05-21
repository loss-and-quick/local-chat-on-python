import socket, select, pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 4000))
server.listen(5)
nickname=input("Никнейм:"),"(admin)"
clients = []
while True:
    Connections, wlist, xlist = select.select([server], [], [], 0.05)

    for Connection in Connections:
        client, Informations = Connection.accept()
        clients.append(client)

    clientsList = []
    try:
        clientsList, wlist, xlist = select.select(clients, [], [], 0.05)
    except select.error:
        pass
    else:
        for clientInList in clientsList:
            data = clientInList.recv(1024)
            data = pickle.loads(data)
            print(data[0],data[1],data[2])
            data = nickname,":",input("Напишите сообщение:")
            data = pickle.dumps(data)
            clientInList.send(data)

clientInList.close()
server.close()