import socket
import threading

HOST = 'server'  
PORT = 5000      

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

username = input('Digite seu nome de usuário: ')
client_socket.send(username.encode('utf-8'))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            break

def send_messages():
    while True:
        message = input()
        if message.lower() == '/sair':
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()