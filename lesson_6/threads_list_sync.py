import time
from threading import Lock, Thread
common_resource = [10]
lock = Lock()


def f1():

    global common_resource
    lock.acquire()
    if common_resource[0] == 10:
        time.sleep(2)
        print(common_resource[0])
    lock.release()


def f2():
    global common_resource
    time.sleep(1)
    lock.acquire()
    common_resource[0] = 20
    lock.release()

t1 = Thread(target=f1)
t2 = Thread(target=f2)

t1.start(), t2.start()