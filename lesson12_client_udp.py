import socket
import threading
import time


shutdown = False
join = False


def receiving(sock):
    global shutdown
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except Exception as e:
            print(e)
            print('Server off')
            shutdown = True


server = ('localhost', 8080)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_port = input("port: ")
s.bind(("localhost", int(my_port)))


name = input('enter name ')
rT = threading.Thread(target=receiving, args=(s, ))
rT.start()

while not shutdown:
    if not join:
        s.sendto(f"{name} -> joined".encode(), server)
        join = True
    else:
        try:
            message = input("message: ")
            if message != "":
                s.sendto(f"{name} :: {message}".encode(), server)
            time.sleep(0.2)
        except Exception as e:
            print(e)
            s.sendto(f"{name} <- left".encode(), server)
            shutdown = True

s.close()
