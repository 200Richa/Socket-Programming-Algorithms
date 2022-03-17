import socket

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

print('This is your IP address: ', ip)
server_host = input('Enter server IP address: ')

socket_server.connect((server_host, sport))


while(True):
    # Display available algorithms from server
    algo = socket_server.recv(1024)
    algo = algo.decode()
    print("Choose an algorithm:\n", algo)

    # Send chosen option to server
    choice = input("Enter option number: ")
    socket_server.send(choice.encode())

    # Input list
    size = int(input("Enter size: "))
    input_list = input()
    socket_server.send(input_list.encode())

    count = 0

    # Loop to display steps
    while True:
        step = (socket_server.recv(1024)).decode()
        if(step=="All steps sent"):
            print("\n")
            break
        print(step)
        socket_server.send("ok".encode())

    e = input("Would you like to try another algorithm?(y/n) ")
    if(e == 'n'):
        socket_server.send("exit".encode())
        exit(0)
    else:
        socket_server.send("continue".encode())
        continue
