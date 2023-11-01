import websockets
import asyncio

# Set to keep track of connected clients
connected = set()

async def chatting_s(websocket):
    # Add the connected client to the set
    connected.add(websocket)
    print("A client has connected!")

    try:
        async for message in websocket:  # Iterate over messages received from this client

            for user in connected:  # Iterate over all connected clients

                if user != websocket:  # Avoid sending the message back to the sender

                    print(f"server received: '{message}'")

                    # Prepare a message to send to other clients
                    mess = f"someone said: {message}"
                    
                    # Send the message to the target client
                    await user.send(mess)
                    
                    print(f"server sent to client '{mess}'")

    except websockets.ConnectionClosedError as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Remove the client from the set when they disconnect
        connected.remove(websocket)
        await websocket.close()

# Print a message when the server starts
print("Server has started!")

# Set up the WebSocket server
starting_server = websockets.serve(chatting_s, "localhost", 8765)

# Run the event loop to start the server
asyncio.get_event_loop().run_until_complete(starting_server)
asyncio.get_event_loop().run_forever()
