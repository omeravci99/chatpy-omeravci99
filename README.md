## Purpose
Server:
The server script sets up a WebSocket server that listens on localhost and port 8765. It allows multiple clients to connect and send and receive chat messages. The server maintains a set of connected clients to broadcast messages to all connected clients, except the sender.

Client:
The client script connects to the server using WebSocket and provides a simple console-based chat interface.
Users can enter chat messages, which are sent to the server and then broadcasted to all other connected clients.
Received messages from other clients are displayed in the console.

## Usage

Start the server by running chat_server.py. It will listen for incoming WebSocket connections on localhost:8765. Start multiple instances of the client by running chat_client.py. These clients can be run in different console windows. In each client console, you can enter messages after the >>> prompt and press Enter to send them. The messages will be sent to the server and broadcast to all other connected clients.

## Safety Concerns

Data Privacy: Without encryption, all messages transmitted between clients and the server are sent in plain text. This means that anyone with access to the network traffic can eavesdrop on the conversations.

No Access Control: Unauthenticated systems lack access control mechanisms. Any user can join the chat, which may not be desirable in situations where you want to restrict access to a specific group.