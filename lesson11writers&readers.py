import threading
import time


def writing(interval):
    while True:
        print("writer {} working. {}".format(interval, time.ctime()))
        time.sleep(interval)


def reading(seconds):
    while True:
        print("reader {} reading. {}".format(seconds, time.ctime()))
        time.sleep(seconds)

w1 = threading.Thread(target=writing, args=(1, ))
w2 = threading.Thread(target=writing, args=(5, ))
r1 = threading.Thread(target=reading, args=(1, ))
r2 = threading.Thread(target=reading, args=(2, ))
r3 = threading.Thread(target=reading, args=(3, ))
w1.start()
w2.start()
r1.start()
r2.start()
r3.start()
