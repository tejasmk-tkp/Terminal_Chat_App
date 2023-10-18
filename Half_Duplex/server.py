import socket

def main():
    host = '0.0.0.0'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    print("Server started on port {}".format(port))
    s.listen(1)

    conn, addr = s.accept()
    print("Connection from: {}".format(addr))
    
    while True:
        data = input("You: ")
        conn.send(data.encode())
        
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Friend: {}".format(data))

    conn.close()

if __name__ == '__main__':
    main()

