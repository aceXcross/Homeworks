import socket


clients = []
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.bind(('localhost', 8080))


close_program = False
print('server start')

while not close_program:
    try:
        data, addr = my_socket.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        print(data, addr)
        for client in clients:
            print(data)
            if addr != client:
                print("Hey-Hey!")
                my_socket.sendto(data, client)

    except Exception as e:
        print(e)
        print('Server stopped')
        close_program = True

my_socket.close()

