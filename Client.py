import socket
 
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080
 
print('This is your IP address: ',ip)
server_host = input('Enter server IP address:')
 
socket_server.connect((server_host, sport))
 
#Display available algorithms from server
algo = socket_server.recv(1024)
algo = algo.decode()
print("Choose an algorithm: \n",algo)

#Send chosen option to server
choice = input("Enter option number: ")
socket_server.send(choice.encode())

#Input list
size = int(input("size "))
list=input()
socket_server.send(list.encode())

#Loop to display steps
#while True:
    #step = (socket_server.recv(1024)).decode()
    #print(step)