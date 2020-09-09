from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper(*args):
        print('Decoration started')
        result = func(*args)
        print('Decoration ended')
        return result

    return wrapper


@decorator
def target_function():
    print('Hello world')


target_function()
target_function.__wrapped__()