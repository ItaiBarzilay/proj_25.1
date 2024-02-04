import threading
import socket

from Card import create_deck

host = 'localhost' #this comp ip
port = 55555

cards = create_deck()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(3)

clients = [] #containing all server clients
nicknames = [] #containing all server nicknames

def deal(card):
    for client in clients:
        client.send(card)

def brodcast(message):#send message to al connected clients
    for client in clients:
        client.send(message)

def handle(client):# remove offline clients
    while True:
        try:
            message = client.recv(1024)
            brodcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            brodcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    client, address = server.accept()
    print(f"Connected with {str(address)}")

    client.send('NICK'.encode('ascii'))
    nickname = client.recv(1024).decode('ascii')
    nicknames.append(nickname)
    clients.append(client)
    deal(cards.pop())
    # while True:
        # client, address = server.accept()
        # print(f"Connected with {str(address)}")
        #
        # client.send('NICK'.encode('ascii'))
        # nickname = client.recv(1024).decode('ascii')
        # nicknames.append(nickname)
        # clients.append(client)

        # print(f'Nickname of the client is {nickname}!')
        # brodcast(f'{nickname} joined the chat!'.encode('ascii'))
        # client.send((str(len(clients)) + 'Connected to the server!').encode('ascii'))
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()
print("Server is running.....")
receive()