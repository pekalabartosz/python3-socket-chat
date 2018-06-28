import colorama
def handle(client, broadcast, users, connected_clients):
    username = client.recv(1024).decode("utf8")

    while username in users:
        client.send(bytes("!!!username is already in use by another user. choose another one.", "utf8"))
        username = client.recv(1024).decode("utf8")
        print(username)

    users.append(username)
    connected_clients[client] = username
    print(username)

    client.send(bytes("| Successfully joined to the server |\n-users connected: %s\n" % len(users), "utf8"))
    broadcast(bytes("- %s has joined" % username, "utf8"))


    while True:
        msg = client.recv(1024)

        if msg.lower() == bytes("/help", "utf8"):
            COMMANDS = ["/help", "/leave", "/users"]
            client.send(bytes("AVAILABLE COMMANDS: {}\n".format(COMMANDS), "utf8"))

        elif msg.lower() == bytes("/users", "utf8"):
            client.send(bytes("CONNECTED USERS({}): {}\n".format(len(users), users), "utf8"))

        elif msg.lower() == bytes("/leave", "utf8"):
            client.close()
            broadcast(bytes("%s has left" % username))
            del connected_clients[client]
            break

        else:
            broadcast(msg, colorama.Fore.CYAN + username + colorama.Style.RESET_ALL + ": ", client)
