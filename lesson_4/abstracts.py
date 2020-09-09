from abc import abstractmethod, ABC


class Draw(ABC):

    @abstractmethod
    def draw(self):
        pass


class Triangle(Draw):

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def draw(self):
        print(f'Drawing triangles on dots {self._x} {self._y} {self._z}')


class Square(Draw):

    def __init__(self, x, y, z, a):
        self._x = x
        self._y = y
        self._z = z
        self._a = a



triangle = Triangle(1, 2, 3)
square = Square(1, 2, 3, 4)

triangle.draw()
square.draw()