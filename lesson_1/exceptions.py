# try:
#     age = int(input('Enter your age'))
#     1 + '1'
#     1 / 0
# except ValueError:
#     print('Wrong value')
#     age = 0
# except ZeroDivisionError:
#     print('You cannot divide by zero')
#     age = 0
#
# print('Your age is', age)


try:
    age = int(input('Enter your age'))
except ValueError:
    age = 0
    print('Wrong value')
finally:
    print('Program closed')


print('Your age is', age)

# def a():
#     try:
#         print('1')
#         return 1
#     finally:
#         print('2')
#         return 2
#
#
# a()