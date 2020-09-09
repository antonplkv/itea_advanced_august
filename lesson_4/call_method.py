class A:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Wrapped')
        return self.func(*args, **kwargs)


@A
def example(a, b):
    return a + b


result = example(10, 20)
print(result)


