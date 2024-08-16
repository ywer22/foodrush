import socket
from _thread import *
import sys

server = "192.168.1.156" 
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(4)
print("Server started. Waiting for connections...")

def threaded_client(conn):
    
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected.")
                break
            else:
                print(f"Received:{reply}")
                print(f"Sending:{reply}")

            conn.sendall(str.encode(reply))
        except:
            print("An error occurred")
            break

    print("Connection lost.")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))

