counter = 0


def increase_counter(func):

    def wrapper(name):
        global counter
        counter += 1
        result = func(name)
        result += 3
        return result

    return wrapper


@increase_counter
def hello_world(name):
    print(f'Hello world {name}')
    return 1

# decorator(hello_world)()
# decorator(hello_world)()
# decorator(hello_world)()
# decorator(hello_world)()


hello_world('John')
hello_world('Michael')
hello_world('Ginni')
print(hello_world('Carla'))

print(counter)