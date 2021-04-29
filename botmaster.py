import socket

def send_response(message, client):
    data = "{:<64}".format(message)
    client.send(data.encode("utf-8"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 7323))

server.listen(10)

while True:
    (client, address) = server.accept()

    target_file = open("target.txt", "r")
    target_data = target_file.read().split(" ")
    target_file.close()

    send_response(f'SEND TCP-SYN {target_data[0]} {target_data[1]} {target_data[2]}', client)

    client.close()

