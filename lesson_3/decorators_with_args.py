def auto_add(fix_num):

    def actual_decorator(func):

        def wrapper(a, b):
            print('Addition started')
            result = func(a, b) + fix_num
            print('Addition ended')
            return result

        return wrapper

    return actual_decorator


@auto_add(10)
def sum_(a, b):
    return a + b

# Run without @ on target function
# actual_decorator = auto_add(10)
# wrapper = actual_decorator(sum_)
# result = wrapper(10, 20)

result = sum_(10, 20)
print(result)