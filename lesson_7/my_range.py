class MyRange:

    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._end:
            result = self._start
            self._start += 1
            return result
        else:
            raise StopIteration('My range object has no items')


# iter_obj = MyRange(0, 5)
# print(type(iter_obj))
# iterator = iter(iter_obj)
# print(type(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


#
# for i in MyRange(0, 5):
#     print(i)

my_range = list(MyRange(0, 100))
print(my_range)