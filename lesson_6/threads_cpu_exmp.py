from threading import Thread
from multiprocessing import Process
import time


def cpu_bound(id_):
    result = [i for i in range(100_000)]


def run_sync():
    start = time.time()
    for i in range(500):
        cpu_bound(i)
    print(str(time.time() - start))


def run_parallel():
    start = time.time()

    for i in range(500):
        process = Process(target=cpu_bound, args=(i, ))
        process.start()
    else:
        process.join()
        print(str(time.time() - start))


run_sync()
run_parallel()

