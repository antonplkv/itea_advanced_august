import threading


class MyThread(threading.Thread):

    def __init__(self, num):
        super().__init__()
        self._num = num

    def run(self):
        print(f'Working in other thread. My id is {self._num}')


threads = [MyThread(i) for i in range(100)]
list(map(lambda m: m.start(), threads))