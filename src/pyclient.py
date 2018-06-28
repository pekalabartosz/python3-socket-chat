logo = """
 ██████╗██╗  ██╗ █████╗ ████████╗
██╔════╝██║  ██║██╔══██╗╚══██╔══╝
██║     ███████║███████║   ██║
██║     ██╔══██║██╔══██║   ██║
╚██████╗██║  ██║██║  ██║   ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
---------------------------client

"""

import socket, threading, os, colorama, getpass
colorama.init(convert = True)

class Task:
    def receiveData():
        while True:
            try:
                msg = clientSocket.recv(1024).decode("utf8")
                print(msg)
            except OSError:
                break


    def sendData():
        msg = input()
        if bool(msg) == True:
            clientSocket.send(bytes(msg, "utf8"))
        else:
            print("message content can't be empty.")


#setting-up client
print(logo)
host = input(">>IP: ")
port = input(">>PORT: ")

if not host:
    host = "127.0.0.1"
else:
    pass

if not port:
    port = 9000
else:
    port = int(port)

if bool(host) == True and bool(port) == True:
    try:
        os.system("cls")
        os.system("clear")
    except Exception as err:
        pass


    address = (host, port)

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(address)

    receiveThread = threading.Thread(target = Task.receiveData)
    receiveThread.daemon = False
    receiveThread.start()

    while True:
        Task.sendData()
