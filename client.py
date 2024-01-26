# Python program to implement CLIENT side of chat room.
import socket


def run_client():
    # Create the socket
    socket_server = socket.socket()
    server_host = socket.gethostname()
    ip = socket.gethostbyname(server_host)
    sport = 8080

    # Connect to the server, also declaring who you are (I like using a name instead of the arrows)
    name = input('Enter your name: ')
    socket_server.connect((ip, sport))

    # Receive packets from server
    socket_server.send(name.encode())
    server_name = socket_server.recv(1024).decode()

    # Print the results of the connection
    print(server_name, 'has joined...')
    print("Type /q to quit")
    print("Enter a message to send...")

    while True:
        message = input("%s(Me): " % name)
        socket_server.send(message.encode())
        # If the user is quitting, send it to the server so that they know as well
        if message == "/q":
            print("Quitting...")
            break
        # Not quitting, then wait for a response from the server
        message = (socket_server.recv(1024)).decode()
        print(server_name, ":", message)


# Where it actually runs the above function
run_client()
