import socket
from SortingAlgorithms import *

steps = []

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your IP: ", s_ip)

new_socket.listen(1)
conn, add = new_socket.accept()

print("Received connection from ", add[0])
print('Connection Established.\n Connected to', add[0])

# Send list of algorithms
algo = "1.Selection Sort\n 2.Bubble Sort\n 3.Heap Sort"
conn.send(algo.encode())

# Receive chosen algorithm from client
choice = int(conn.recv(1024).decode())

# Receive list from client
A = conn.recv(1024).decode()
print(A)
list = []
for i in A.split():
    list.append(int(i))

if choice == 1:  # Selection Sort
    selection_sort(list, steps)
elif choice == 2:  # Bubble sort
    bubble_sort(list, steps)
else:
    heap_sort(list, steps)

for i in steps:
    conn.send(i.encode())
    status = conn.recv(1024).decode()
    print(status)
