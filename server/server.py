import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

TCHAT_VERSION = "1.0.0"
USERS = set()

async def broadcast(users, message, exclude=None):
    """Broadcast a message to all connected users"""
    if users:
        websockets_to_remove = set()
        for user in users:
            if user == exclude:
                continue
            try:
                await user.send(message)
            except ConnectionClosed:
                websockets_to_remove.add(user)
        
        for user in websockets_to_remove:
            users.remove(user)

async def handle_message(websocket):
    global USERS

    try:
        async for message in websocket:
            if message == "identify":
                await websocket.send(f"TChat {TCHAT_VERSION}")
            elif message.startswith("username:"):
                username = message[9:]
                websocket.username = username
                USERS.add(websocket)
                await websocket.send(str(len(USERS)))
                await broadcast(USERS, f"{username} has joined the chat.")
            else:
                await broadcast(USERS, f"{websocket.username}: {message}", websocket)
    finally:
        if websocket in USERS:
            if hasattr(websocket, 'username'):
                await broadcast(USERS, f"{websocket.username} has left the chat.")
            USERS.remove(websocket)

async def main():
    async with serve(handle_message, "localhost", 8765) as server:
        print("TChat Server is running on ws://localhost:8765")
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())