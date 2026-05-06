import socket 
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
server_address = ('127.0.0.1', 9090) 
udp_client.sendto("Hello UDP Server!".encode(), server_address) 
data, server = udp_client.recvfrom(1024) 
print(f"Server says: {data.decode()}") 
udp_client.close()
