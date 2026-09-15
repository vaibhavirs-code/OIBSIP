# Chat Application - Server
# Oasis Infobyte Python Programming Internship

import socket
from datetime import datetime

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address
host = "127.0.0.1"
port = 12345

server.bind((host, port))
server.listen(2)

print("Chat Server Started")
print("Waiting for a client to connect...")

# Accept client connection
client, address = server.accept()

print("Client connected:", address)
print("You can start chatting!\n")

while True:

    # Receive message
    message = client.recv(1024).decode()

    if not message:
        print("Client disconnected.")
        break

    current_time = datetime.now().strftime("%H:%M:%S")

    print(f"[{current_time}] Client: {message}")

    # Exit if client says bye
    if message.lower() == "bye":
        print("Chat ended.")
        break

    # Send response
    reply = input("You: ")

    client.send(reply.encode())

    if reply.lower() == "bye":
        print("Chat ended.")
        break

client.close()
server.close()