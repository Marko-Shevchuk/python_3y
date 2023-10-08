import socket
import time


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)
server_socket.listen(1)
print("Server listening to {}:{}".format(server_address[0], server_address[1]))
print("CONNECT ALREADY")

client_socket, client_address = server_socket.accept()
print("Connected with client {}".format(client_address))
received_data = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    received_data += data

time.sleep(5)

if received_data:
    received_text = received_data.decode('utf-8')
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print("Client says: {}".format(received_text))
    print("at time: {}".format(current_time))
    response = "Server received your message: '{}'".format(received_text)
    client_socket.send(response.encode('utf-8'))

client_socket.close()
server_socket.close()
