import socket
import time


clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 8080))
quit = False
print("[Server Started]")


while not quit:
    try:
        data, addr = s.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        for client in clients:
            if addr != client:
                s.sendto(data,client)
    except Exception as e:
        print(e)
        print("server stoped")
        close_program = True


s.socket.close()

