import colorama
import asyncio
import shutil
from sockets import connect_to_server, set_username
from chat import handle_chat

colorama.init()

async def main():
    terminal_width = shutil.get_terminal_size().columns  # Assuming a standard terminal width
    ascii_art = """_____  ___ _           _   
/__   \/ __\ |__   __ _| |_ 
/ /\/ /  | '_ \ / _` | __|
/ / / /___| | | | (_| | |_ 
\/  \____/|_| |_|\__,_|\__|""".split("\n")
    slogan = "It's like AIM... but for the 21st Century!".center(terminal_width)

    print(colorama.Style.BRIGHT + colorama.Fore.BLUE)
    for line in ascii_art:
        print(line.center(terminal_width))
    print(colorama.Style.RESET_ALL + "\n")
    print(colorama.Style.BRIGHT + colorama.Fore.BLUE + slogan + colorama.Style.RESET_ALL + "\n\n")

    is_valid_url = False

    while not is_valid_url:
        server_url = input(colorama.Style.BRIGHT + "Enter Server URL (don't include url scheme or port): " + colorama.Style.RESET_ALL)

        try:
            server_version = await connect_to_server(server_url)

            print(colorama.Style.BRIGHT + colorama.Fore.GREEN + "Connected! Server Version: " + server_version + colorama.Style.RESET_ALL)

            is_valid_url = True
        except:
            print(colorama.Style.BRIGHT + colorama.Fore.RED + "Invalid URL. Please enter a valid URL." + colorama.Style.RESET_ALL)

    username = None

    while username is None:
        ui = input(colorama.Style.BRIGHT + "Enter Username: " + colorama.Style.RESET_ALL)
        if ui.strip() != "":
            username = ui
        else:
            print(colorama.Style.BRIGHT + colorama.Fore.RED + "Username cannot be empty." + colorama.Style.RESET_ALL)

    user_count = await set_username(username)

    print("\033[2J")

    print(colorama.Style.BRIGHT + colorama.Fore.GREEN + f"Welcome to the chatroom! There are currently {user_count} user(s) online. /exit to exit." + colorama.Style.RESET_ALL)
    
    # Start the chat handler
    await handle_chat()

if __name__ == "__main__":
    asyncio.run(main())