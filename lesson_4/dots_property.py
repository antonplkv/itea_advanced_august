class DotNotInRange(Exception):
    pass


class Dot:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not 0 < value < 10:
            raise DotNotInRange
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):

        if not 50 < value < 100:
            raise DotNotInRange

        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if not 100 < value < 150:
            raise DotNotInRange
        self._z = value


dot = Dot(8, 51, 120)
print(dot.x)
dot.x = 12
print(dot.x)