# TChat

> "Just like AIM!"
> 
> -- CEO of AOL


A simple terminal-based chat application built with Python and WebSockets.

## Features

- Real-time messaging
- Colorful username display
- Join/leave notifications
- Simple and intuitive interface

## Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

## Client Setup

1. Clone the repository:
   ```
   git clone https://github.com/makors/tchat.git
   cd tchat
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install client dependencies:
   ```
   pip install websockets colorama aioconsole
   ```

4. Run the client:
   ```
   python client/app.py
   ```

5. When prompted, enter the server URL (without protocol or port) and your username.

## Server Setup

1. Create and activate a virtual environment for the server:
   ```
   cd server
   python -m venv .env-server
   # On Windows
   .env-server\Scripts\activate
   # On macOS/Linux
   source .env-server/bin/activate
   ```

2. Install server dependencies:
   ```
   pip install websockets
   ```

3. Run the server:
   ```
   python server.py
   ```

The server will start on `localhost:8765`.

## Usage

- Type messages and press Enter to send
- Type `/exit` to leave the chat