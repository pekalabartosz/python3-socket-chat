import socket, threading, colorama

with open("server_commands.txt", "r") as f:
    for content in f:
        server_commands = content

        print("server_commands.txt loaded")


def acceptingConnections():
    while True:
        client, client_address = server.accept()
        print("new connection: %s:%s" % client_address)
        client.send(bytes("Hello! Please type your usename below:", "utf8"))

        addresses[client] = client_address

        handleConnection = threading.Thread(target = handlingConnections, args = (client,))
        handleConnection.start()


def handlingConnections(client):
    username = client.recv(1024).decode("utf8")
    users.append(username)
    client.send(bytes("| Successfully joined to the server |\n-users connected: %s\n" % len(users), "utf8"))
    broadcast(bytes("- %s has joined" % username, "utf8"))

    connected_clients[client] = username

    while True:
        msg = client.recv(1024)

        if msg.lower() == bytes("/help", "utf8"):
            client.send(bytes(server_commands, "utf8"))

        elif msg.lower() == bytes("/users", "utf8"):
            client.send(bytes("CONNECTED USERS({}): {}\n".format(len(users), users), "utf8"))

        elif msg.lower() == bytes("/leave", "utf8"):
            client.close()
            del connected_clients[client]
            broadcast(bytes("%s has left" % username))
            break

        else:
            broadcast(msg, colorama.Fore.CYAN + username + colorama.Style.RESET_ALL + ": ", client)


def broadcast(msg, sender = "", client = ""):
    x = {}
    author = sender[5:-6].strip()

    for key, value in connected_clients.items():
        print(key, value)
        if value != author:
            x[key] = value

    for sock in x:
        sock.send(bytes(sender, "utf8") + msg)

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
