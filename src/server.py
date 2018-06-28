import socket, threading, colorama
from handlers import connection, message

def acceptingConnections():
    while True:
        client, client_address = server.accept()
        print("new connection: %s:%s" % client_address)
        client.send(bytes("Hello! Please type your usename below:", "utf8"))

        addresses[client] = client_address

        handleConnection = threading.Thread(target = handlingConnections, args = (client,))
        handleConnection.start()


def handlingConnections(client):
    connection.handle(client, broadcast, users, connected_clients)


def broadcast(msg, sender = "", client = ""):
    message.handle(msg, sender, client, connected_clients)

#client informations
users = []
connected_clients = {}
addresses = {}

#running server
host = "127.0.0.1"
port = 9000
address = (host, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)

if __name__ == "__main__":
    server.listen(5)
    print("server is ready | waiting for connections")

    acceptingConnectionsThread = threading.Thread(target = acceptingConnections)
    acceptingConnectionsThread.start()
    acceptingConnectionsThread.join()

    server.close()
