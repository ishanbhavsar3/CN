TCP Client 

import socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(('127.0.0.1', 8080)) 
client_socket.send("Hello Server, I am the TCP Client!".encode()) 
data = client_socket.recv(1024).decode() 
print(f"Server response: {data}") 
client_socket.close() 