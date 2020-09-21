from threading import Lock, Thread

lock = Lock()


def write(data):
    lock.acquire()
    with open('filename.txt', 'a') as file:
        for i in range(10):
            file.write(f'{data}\n')
    lock.release()

t1 = Thread(target=write, args=(str(1), ))
t2 = Thread(target=write, args=(str(2), ))
t3 = Thread(target=write, args=(str(3), ))

t1.start(), t2.start(), t3.start()