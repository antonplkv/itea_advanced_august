class A:

    X = 100

    def __init__(self, a):
        self.a = a

    def print_object_data(self):
        print(self.a, self.X)

    def change_x(self):
        self.X += 20
        print(self.X)





print(A.X)

obj = A(-10)
obj.print_object_data()
A.X = 200
obj.print_object_data()
obj.change_x()
print(A.X)