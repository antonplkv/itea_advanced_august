
# while True:
#
#     user_input = input('Введите, что Вы хотите сделать\n')
#
#     if user_input == 'exit':
#         break
#     elif user_input == 'pass':
#         continue
#
#     print('The end of iteration')


a = [100, 200, 300]

my_range = range(101)
for i in my_range:
    print(i)

print('*'*10)
print(i)
print('*'*10)
for i in range(10):
    print(i)


def hello():
    print('Hello world')


# func_obj = hello
# func_obj()


def run_function_object(func_obj):
    func_obj()


run_function_object(hello)