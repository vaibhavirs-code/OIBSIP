# Chat Application - Client
# Oasis Infobyte Python Programming Internship

import socket
from datetime import datetime

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address
host = "127.0.0.1"
port = 12345

# Connect to server
client.connect((host, port))

print("Connected to the chat server!")
print("You can start chatting!\n")

while True:

    # Send message
    message = input("You: ")

    client.send(message.encode())

    if message.lower() == "bye":
        print("Chat ended.")
        break

    # Receive response
    reply = client.recv(1024).decode()

    current_time = datetime.now().strftime("%H:%M:%S")

    print(f"[{current_time}] Server: {reply}")

    if reply.lower() == "bye":
        print("Chat ended.")
        break

client.close()