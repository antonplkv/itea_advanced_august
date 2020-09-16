from threading import Thread
import time


def sleeping():
    time.sleep(5)
    print('Ended')


Thread(target=sleeping, daemon=True).start()
print('Hello world')
time.sleep(5.5)