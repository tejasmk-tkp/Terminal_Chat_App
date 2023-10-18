import socket

def main():
    host = input("Enter server IP: ")
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        data = s.recv(1024).decode()
        if not data:
            break
        print("Friend: {}".format(data))
        
        data = input("You: ")
        s.send(data.encode())

    s.close()

if __name__ == '__main__':
    main()

