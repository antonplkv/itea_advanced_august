# def sum_(*args):
#     print(1, 2, 3, 10)
#     print((1, 2, 3, 10))
#     print(*args)
#     print(args)
#     return sum(args)
#
#
# result = sum_(1, 2, 3, 10)
# print(result)


# def test(*args):
#     print(args)



# a = [1, 2, 3, 5]
#
# test(*a)


def test(a, b, c):
    print(a + b - c)

data = [1, 2, 3]

#test(*data) == data(1, 2, 3)


# def test_kwargs(**kwargs):
#     print(kwargs['arg1'], kwargs['arg2'])
#
#
# test_kwargs(arg1=10, arg2=3, arg3=100)


def test_kwargs(*args, **kwargs):
    required_args = ('arg1', )

    for arg in required_args:
        if arg in kwargs.keys():
            continue
        else:
            raise Exception('Error')



data = {
    'arg100': 100,
    'arg2': 200,
    'arg4': 33,
}


a = 100


test_kwargs(**data) == test_kwargs(100, 200, 300, arg1=100, arg2=200, arg3=33)
