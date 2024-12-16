import socket
import select

HOST = '0.0.0.0' 
PORT = 5000 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

sockets_list = [server_socket]
clients = {}

print(f'Servidor ouvindo em {HOST}:{PORT}')

def receive_message(client_socket):
    try:
        message = client_socket.recv(1024)
        if not message:
            return False
        return message.decode('utf-8')
    except:
        return False

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(f'Nova conexão de {client_address[0]}:{client_address[1]} - Usuário: {user}')
        else:
            message = receive_message(notified_socket)
            if message is False:
                print(f'Conexão fechada de {clients[notified_socket]}')
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            print(f'Mensagem recebida de {user}: {message}')
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(f'{user}: {message}'.encode('utf-8'))

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]