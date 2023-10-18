import socket
import threading

connected_clients = []

def handle_client(client_socket):
    
    connected_clients.append(client_socket)

    try:
        while True:
            data = client_socket.recv(1024)
            
            if not data:
                print("Client disconnected")
                break

            message = data.decode('utf-8')

            print(f"Received from client: {message}")

            response = "Message received: " + message
            client_socket.send(response.encode('utf-8'))

            for other_client in connected_clients:
                if other_client != client_socket:
                    try:
                        other_client.send(message.encode('utf-8'))
                    except Exception as e:
                        print(f"Error sending message: {e}")

    except Exception as e:
        print(f"Client error: {e}")

    finally:
        connected_clients.remove(client_socket)
        client_socket.close()

server_ip = '127.0.0.1'
server_port = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_ip, server_port))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    client_thread = threading.Thread(target = handle_client, args = (client_socket,))
    client_thread.start()

