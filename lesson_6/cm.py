class MyCm:

    def __init__(self, a, b):
        self._a = a
        self._b = b
        self._is_closed = False
        self._closed_because_of_exc = False

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def __enter__(self):
        if self._is_closed:
            raise Exception('U cannot open object again')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._closed_because_of_exc = True
        print(self._closed_because_of_exc)
        self._is_closed = True


with MyCm(10, 20) as obj:
    print(obj.get_a())
    print(obj.get_b())
    print(obj._is_closed)
    1 / 0
