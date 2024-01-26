# This is a sample Python script.
import server
import client
from threading import Thread

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Thread(target = server.run_server()).start()
    Thread(target = client.run_client()).start()
    print("")
    # Link to website that seems to have everything already created for this project
        # https://www.geeksforgeeks.org/simple-chat-room-using-python/
        # https://www.geeksforgeeks.org/simple-chat-room-using-python/

