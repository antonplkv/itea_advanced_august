to_square = lambda x, y: (x ** 2, y ** 2)
result = to_square(2, 4)
print(result)


def confirmer(func_obj, arg):
    return func_obj(arg)


result = confirmer(lambda x: x ** 2, 10)
print(result)


list_of_numbers = [1, 2, 4, 8, 16]
list_of_numbers_2 = [2, 3, 5, 9, 17]

squares = []
for num in list_of_numbers:
    squares.append(num ** 2)

print(squares)

result = list(map(lambda x: x ** 2, list_of_numbers))
print(result)

print(list(map(lambda x, y: x + y if x + y > 10 else None, list_of_numbers, list_of_numbers_2)))


list_of_numbers = [100, 200, 300, 90, 80, 600]

print(list(filter(lambda x: x >= 100, list_of_numbers)))


dict_of_numbers = {
    1: 2,
    3: 4,
    5: 6
}

#print(list(map(lambda k: (k[0] ** 2, k[1] ** 2), dict_of_numbers.items())))



