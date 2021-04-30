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
        target_command = target_file.read()
        target_file.close()
        if len(target_command) >= 0:
            send_response(target_command, client)
        else:
            send_response("NONE", client)
    except Exception as e:
        send_response("NONE", client)
        print(e)

    client.close()

