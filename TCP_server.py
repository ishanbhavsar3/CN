import socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind(('127.0.0.1', 8080)) 
server_socket.listen(1) 
print("TCP Server is running and waiting for connection...") 
client_conn, client_addr = server_socket.accept() 
print(f"Connected to: {client_addr}") 
message = client_conn.recv(1024).decode() 
print(f"Message from Client: {message}") 
response = "Hello Client, I received your message!" 
client_conn.send(response.encode()) 
client_conn.close() 
server_socket.close() 
