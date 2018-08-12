import socket, select, pickle
from termcolor import colored
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((input("Введите Ip для сервера:"), 4000))
server.listen(int(input("Введите скольок максимально пользователей на сервере> ")))

nickname=input("Никнейм:"),"(admin)"
clients = []
while True:
    Connections, wlist, xlist = select.select([server], [], [], 0.05)
    for Connection in Connections:
        client, Informations = Connection.accept()
        clients.append(client)
        print("Новый пользователь зашел")
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
            data = nickname,"> ",input("Напишите сообщение:")
            print(colored("-----------------------", "green"))
            print(colored("в чате", len(clients) + 1, "green"))
            print(colored("-----------------------", "green"))
            data = pickle.dumps(data)
            clientInList.send(data)

clientInList.close()
server.close()
