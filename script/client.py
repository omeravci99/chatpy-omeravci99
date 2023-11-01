import asyncio
import websockets
import aioconsole

# Function to receive messages over WebSocket and print them to the console.
async def message_receiver(websocket):
    while True:
        message = await websocket.recv()
        await aioconsole.aprint(message)

# Function to get user input from the console and send it to the server over WebSocket.
async def message_sender(websocket):
    while True:
        message = await aioconsole.ainput(">>>")
        await websocket.send(message)

async def main():
    # Connect to the WebSocket server
    async with websockets.connect("ws://localhost:8765") as ws:
        # Create tasks for sender and receiver to run concurrently
        sender = asyncio.create_task(message_sender(ws))
        receiver = asyncio.create_task(message_receiver(ws))
        
        # Wait for the sender and receiver tasks to complete
        await sender
        await receiver

if __name__ == "__main__":
    # Get the event loop and run the main function
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
