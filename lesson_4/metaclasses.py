a = 1

# print(type(type(type(a))))

def method(self):
    print(self.FLAG)


my_class = type('MyClass', (), {'FLAG': True, 'method': method})

obj = my_class()
print(type(obj))
print(obj.FLAG)
obj.method()


# class MyClass:
#
#     FLAG = True
#
#     def method(self):
#         print(self.FLAG)


class A:

    def say_hello(self):
        print('Hello!')


class MyMeta(type):

    def __new__(mcs, name, base, attrs):
        base = (A, )
        if not attrs.get('CAR_TYPE'):
            raise Exception('All class variables must be implemented')
        class_obj = super().__new__(mcs, name, base, attrs)
        return class_obj


class Car(metaclass=MyMeta):

    CAR_TYPE = 'coupe'

    def __init__(self, model, colour):
        self.model = model
        self.colour = colour

    def drive(self):
        print(f'{self.model} is driving')


Car('BMW', 'yellow').say_hello()