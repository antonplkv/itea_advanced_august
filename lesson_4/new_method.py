class Dot:

    def __new__(cls, x, y):
        if x < 0:
            raise Exception('X must be bigger than 0')
        obj = super().__new__(cls)
        obj.x = x
        obj.y = y
        return obj



b = Dot(0, 20)
print(b.x)