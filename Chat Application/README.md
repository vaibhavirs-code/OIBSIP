# Chat Application
This project is a simple client-server chat application developed using Python sockets. The application allows a client and server to communicate with each other in real time using a local connection.

## Features
* Client-server communication
* Real-time message exchange
* Python socket programming
* Timestamps for messages
* Works on localhost
* Graceful disconnection
* Simple and beginner-friendly

## Technologies Used
* Python 3
* Socket Programming
* datetime module

## Project Structure
```text
Chat Application
│
├── server.py
├── client.py
└── README.md
```

## How to Run

### Step 1: Start the Server
Open a terminal in the Chat Application folder.

Run:

```bash
python server.py
```

You should see:

```text
Chat Server Started
Waiting for a client to connect...
```
### Step 2: Start the Client
Open a second terminal in the same Chat Application folder.

Run:

```bash
python client.py
```

You should see:

```text
Connected to the chat server!
You can start chatting!
```
### Step 3: Chat
Type a message in the client terminal.

The server will receive the message and can send a reply.

To end the chat, type:

```text
bye
```

## Sample Output
Connected to the chat server!
You can start chatting!

You: Hello
[22:07:49] Server: Hello! How r u?
You: Fine. What about you?
[22:08:36] Server: Good
You: Ok
[22:08:59] Server: Yes. Bye
You: Bye
Chat ended.

## Learning Outcome
This project demonstrates:
* Python socket programming
* Client-server architecture
* Sending and receiving messages
* Real-time communication
* Basic connection handling

## Internship
Developed as part of the Oasis Infobyte Python Programming Internship.
