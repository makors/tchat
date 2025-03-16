from websockets.asyncio.client import connect

websocket = None

async def connect_to_server(server_url: str) -> str | ConnectionError:
    global websocket
    websocket = await connect(f"ws://{server_url}:8765")

    await websocket.send("identify")

    message = await websocket.recv()

    if not message.startswith("TChat"):
        raise ConnectionError(f"Invalid server response: {message}")
    
    return message

async def set_username(username: str) -> int:
    await websocket.send(f"username:{username}")
    user_count = await websocket.recv() # returns user count
    
    await websocket.recv()
    
    return int(user_count)

async def receive_messages():
    while True:
        message = await websocket.recv()
        yield message

async def send_message(message: str):
    await websocket.send(message)
