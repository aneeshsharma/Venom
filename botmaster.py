import socket

def send_response(message, client):
    data = "{:<64}".format(message)
    client.send(data.encode("utf-8"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 7323))

server.listen(10)

while True:
    (client, address) = server.accept()

    try:
        target_file = open("target.txt", "r")
        target_data = target_file.read().split(" ")
        target_file.close()
        if len(target_data) == 3:
            send_response(f'SEND HTTP {target_data[0]} {target_data[1]} {target_data[2]}', client)
        else:
            send_response("NONE", client)
    except Exception as e:
        send_response("NONE", client)
        print(e)

    client.close()

