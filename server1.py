import socket
import time

# сокет для сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)

# прослуховування порту
server_socket.listen(1)

print("Server listening to {}:{}".format(server_address[0], server_address[1]))
print("CONNECT ALREADY")
client_socket, client_address = server_socket.accept()
print("Connected with client {}".format(client_address))
data = client_socket.recv(1024)  # Отримання даних від клієнта
received_text = data.decode('utf-8')  # розкодування
current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print("Client says: {}".format(received_text))
print("at time: {}".format(current_time))

client_socket.close()
server_socket.close()