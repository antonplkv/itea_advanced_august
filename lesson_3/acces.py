class A:

    def __init__(self, a, b):
        self.__a = a
        self._b = b

    def get_a(self):
        return self.__a

    def set_a(self, value):
        self.__a = value

    def get_b(self):
        return self._b

    def set_b(self, value):
        if value > 10:
            raise Exception('Error!')

        self._b = value


obj = A(10, 20)
print(obj.get_a())
obj.set_a(25)
print(obj.get_a())
obj.set_b(4)

print(obj._A__a)