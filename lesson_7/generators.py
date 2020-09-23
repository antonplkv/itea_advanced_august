def my_range(start, end):

    while start < end:
        yield start
        start += 1


range_object = my_range(0, 5)
# iterator = iter(range_object)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in my_range(0, 10):
#     print(i)


def test_generator(start, end):

    while start < end:
        print('The beginning of loop')
        yield start
        start += 1
        print('The end of iteration')


gen = test_generator(0, 3)
iterator = iter(gen)

print(next(iterator))
print('------------------------')
print(next(iterator))
print('------------------------')
print(next(iterator))


my_gen_exp = (x for x in range(10))
print(my_gen_exp)
result = list(my_gen_exp)
print(result)

