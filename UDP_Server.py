import socket 
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
udp_server.bind(('127.0.0.1', 9090)) 
print("UDP Server is ready to receive data...") 
data, addr = udp_server.recvfrom(1024) 
print(f"Received: {data.decode()} from {addr}") 
udp_server.sendto("UDP Server got your packet!".encode(), addr) 
udp_server.close()
