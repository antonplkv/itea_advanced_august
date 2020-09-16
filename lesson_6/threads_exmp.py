from threading import Thread
import time


def io_bound(id_):
    print(f'{id_} io bound started')
    time.sleep(5)
    print(f'{id_} woken up')


# Sync
# io_bound(1)
# io_bound(2)


# Concurent
# thread1 = Thread(target=io_bound, args=(1, ))
# thread2 = Thread(target=io_bound, args=(2, ))
# thread1.start()
# thread2.start()
# thread2.join()

# print('Main thread still working')

start = time.time()
threads = []
for i in range(100):
    thread = Thread(target=io_bound, args=(i,), name=f'MyThread-{i}')
    thread.start()
    threads.append(thread)

time.sleep(5)
end = time.time() - start



