class MyError(Exception):

    def __init__(self, data, *args, **kwargs):
        super().__init__(*args)
        self.data = data
        self.kwargs = kwargs


# raise MyError

try:
    raise MyError('data is 1', 'MyApp error')
except MyError as me:
    print(me)
    print(me.args)
    print(me.data)
    print(dir(me))


raise ValueError('Qwqwqwqwq')