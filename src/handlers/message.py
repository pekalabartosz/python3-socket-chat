def handle(msg, sender, client, connected_clients):
    otherClients = {}
    author = sender[5:-6]

    for key, value in connected_clients.items():
        if value != author:
            otherClients[key] = value

    for sock in otherClients:
        sock.send(bytes(sender, "utf8") + msg)
