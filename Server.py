from secrets import choice
import time, socket, sys

def selectionSort(A):
    print(A)
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
        print(A)
 
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
print('Connection Established.\n Connected to',add[0])
 
#Send list of algorithms
algo = "1.Selection Sort \n2.Bubble Sort\n"
conn.send(algo.encode())

#Recieve chosen algorithm from client
choice = int(conn.recv(1024).decode())

#Recieve list from client
A = conn.recv(1024).decode()
print(A)
list=[]
#for i in range(len(A)):
    #if(i%2!=0):
        #list.append(int(A[i]))

if(choice==1):   #Selection Sort
    selectionSort(list)
