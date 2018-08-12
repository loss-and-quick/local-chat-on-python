import socket, pickle
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((input("Введите Ip сервера:"), 4000))
nickname=input("Никнейм:")
while True:
    data = nickname,"> ",input("Напишите сообшение:")
    data = pickle.dumps(data)
    server.send(data)
    data = server.recv(1024)
    data = pickle.loads(data)
    print(data[0][0],data[0][1],data[1],data[2])

server.close()