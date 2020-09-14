class ObjectAlreadyExists(Exception):
    pass


class Singletone:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            obj = super().__new__(cls)
            cls._instance = obj
        return cls._instance

    def __init__(self, x, y):
        self.x = x
        self.y = y


obj1 = Singletone(1, 2)
print(obj1)
obj2 = Singletone(2, 3)
print(obj2)
print(obj2.x)