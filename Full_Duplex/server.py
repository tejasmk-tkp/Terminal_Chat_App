import socket
import threading

connected_clients = []
name = []

def broadcast(message, sender_name):
    for client in connected_clients:
        if client != client_socket:
        try:
            if client != client_socket:
                client.send(f"{sender_name}: {message}".encode('utf-8'))
        except Exception as e:
            print(f"Error sending message to {sender_name}: {e}")

def handle_client(client_socket):
    
    connected_clients.append(client_socket)

    try:

        client_socket.send("Please enter your name: ".encode('utf-8'))
        user_name = client_socket.recv(1024).decode('utf-8')

        broadcast(f"{user_name} has joined the chat", sender_name = user_name)

        while True:
            data = client_socket.recv(1024)
            
            if not data:
                print("Client disconnected")
                break

            message = data.decode('utf-8')

            print(f"{user_name}: {message}")

            broadcast(message, sender_name = user_name)

    except Exception as e:
        print(f"{user_name} error: {e}")

    finally:
        connected_clients.remove(client_socket)
        client_socket.close()

server_ip = '0.0.0.0' #input("Enter Server IP Address: ")
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_ip, server_port))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    client_thread = threading.Thread(target = handle_client, args = (client_socket,))
    client_thread.start()

