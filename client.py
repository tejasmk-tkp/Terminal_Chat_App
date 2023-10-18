import socket
import threading

def send_message():
    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))

def receive_message():
    while True:
        data = client_socket.recv(1024)
        
        if not data:
            #print("Server dissconnected")
            break
        
        message = data.decode('utf-8')
        print(f"Other: {message}")

server_ip = '127.0.0.1'
server_port = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

send_thread = threading.Thread(target = send_message)
receive_thread = threading.Thread(target = receive_message)

send_thread.start()
receive_thread.start()
