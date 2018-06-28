import colorama

def handle(client, broadcast, users, connected_clients, server_commands):
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
