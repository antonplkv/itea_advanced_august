import random


class MyRange:

    def __init__(self, start, end, random_from=0, random_to=100):
        self._start = start
        self._end = end
        self._random_from = random_from
        self._random_to = random_to

    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._end:
            self._start += 1
            return random.randint(self._random_from, self._random_to)
        else:
            raise StopIteration('My range object has no items')


print(list(MyRange(0, 5)))