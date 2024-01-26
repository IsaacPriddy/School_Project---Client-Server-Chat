# Python program to implement SERVER side of chat room.
import socket


def run_server():
    # Create the socket, all the info needed for the socket
    my_socket = socket.socket()
    host_name = socket.gethostname()
    the_ip = socket.gethostbyname(host_name)
    port = 8080

    # Bind the Host and Port, print out info for assignment/useful to see (Could change the server and port to be specific, made it auto here)
    my_socket.bind((host_name, port))
    print("Server listening on: local host on port: %s" % port)
    print("Connected by ('%s', %s)" % (the_ip, port))

    # Listening for Connections, also declaring who you are (I like using a name instead of the arrows)
    name = input('Enter your name: ')
    my_socket.listen(1)
    print("Name accepted, waiting for client to join...\n") # Wanted something that worked as feedback to the server user

    # Accepting incoming connections
    conn, add = my_socket.accept()

    # Storing incoming connection data, also printing the results of the connection
    client = (conn.recv(1024)).decode()
    print(client + " has joined.")
    conn.send(name.encode())
    print("Waiting for message...")

    # Delivering Packets/Messages
    while True:
        message = conn.recv(1024).decode()
        # If the user sends a quitting message, exit the program peacefully
        if message == "/q":
            print("Client has disconnected...")
            print("Quitting...")
            break
        # Otherwise, continue on as normal
        print(client, ":", message)
        message = input("%s(Me): " % name)
        conn.send(message.encode())


# Where it actually runs the above function
run_server()
