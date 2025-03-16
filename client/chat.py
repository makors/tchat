import aioconsole
import colorama
import asyncio
import shutil
from sockets import receive_messages, send_message

async def receive_messages_loop():
    async for message in receive_messages():
        print('\r' + ' ' * shutil.get_terminal_size().columns, end='\r')
        
        if "has left the chat" in message or "has joined the chat" in message:
            print(f"{colorama.Style.DIM}{message}{colorama.Style.RESET_ALL}")
        else:
            if ": " in message:
                username, content = message.split(": ", 1)
                color_index = sum(ord(c) for c in username) % 6
                colors = [colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, 
                          colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN]
                username_color = colors[color_index]
                print(f"{username_color}{username}{colorama.Fore.RESET}: {content}{colorama.Style.RESET_ALL}")
            else:
                print(f"{colorama.Fore.CYAN}{message}{colorama.Style.RESET_ALL}")
        
        print(f"{colorama.Style.BRIGHT}> {colorama.Style.RESET_ALL}", end='', flush=True)

async def handle_chat():
    receive_task = asyncio.create_task(receive_messages_loop())
    
    try:
        while True:
            message = await aioconsole.ainput(f"{colorama.Style.BRIGHT}> {colorama.Style.RESET_ALL}")
            print('\r' + ' ' * shutil.get_terminal_size().columns, end='\r')
            
            if message.strip():
                if message == "/exit":
                    print("\nExiting chat...")
                    break

                await send_message(message)                
    except KeyboardInterrupt:
        print("\nExiting chat...")
    finally:
        receive_task.cancel()