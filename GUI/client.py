import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

# You can move this to a function for a cleaner code
def connect_to_server():
    global client_socket
    server_ip = simpledialog.askstring("Input", "Enter Server IP Address:")
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    receive_thread = threading.Thread(target=receive_message)
    receive_thread.start()

def send_message():
    message = message_entry.get()
    if message:  # Check if message is not empty
        client_socket.send(message.encode('utf-8'))
        chat_display.insert(tk.END, "You: " + message + "\n")
        chat_display.yview(tk.END)  # Auto-scroll
        message_entry.delete(0, tk.END)  # Clear input field

def receive_message():
    while True:
        try:
            data = client_socket.recv(1024)

            if not data:
                break

            message = data.decode('utf-8')
            chat_display.insert(tk.END, message + "\n")
            chat_display.yview(tk.END)  # Auto-scroll
        except:
            messagebox.showerror("Error", "Connection lost!")
            root.quit()
            break

root = tk.Tk()
root.title("Chat Client")

# Chat display
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=50, height=20)
chat_display.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Message entry
message_entry = tk.Entry(root, width=40)
message_entry.grid(row=1, column=0, padx=10, pady=10)
message_entry.bind("<Return>", lambda event=None: send_message())

# Send button
send_button = tk.Button(root, text="Send", command=send_message, width=10)
send_button.grid(row=1, column=1, padx=10, pady=10)

connect_to_server()  # Connect to server upon start
root.mainloop()

