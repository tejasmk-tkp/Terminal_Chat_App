import socket
import threading

def send_message():
    while True:

        try:
            message = input("You: ")
            client_socket.send(message.encode('utf-8'))

        except KeyboardInterrupt:
            print("You left the chat!")
            break

def receive_message():
    while True:

        try:
            data = client_socket.recv(1024)
            
            if not data:
                break
            
            message = data.decode('utf-8')
            print(f'\n{message}')

        except KeyboardInterrupt:
            print("You left the chat!")
            break

server_ip = input("Enter Server IP Address: ")
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

send_thread = threading.Thread(target = send_message)
receive_thread = threading.Thread(target = receive_message)

send_thread.start()
receive_thread.start()

