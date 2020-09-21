class Array:

    def __init__(self, *args, type_=int):
        self._array = list(args)
        self._type = type_
        self._validate(*self._array)

    def _validate(self, *args):
        for arg in args:
            if not isinstance(arg, self._type):
                raise TypeError(f'Array can only consist of {self._type}')

    def __getitem__(self, item):
        return self._array[item]

    def __setitem__(self, key, value):
        self._validate(value)
        self._array[key] = value


array = Array(1, 2, 3, 4, 5, 6)

for i in array:
    print(i)