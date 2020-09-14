final_list = []

for i in range(100):
    final_list.append(i)

print(final_list)
result = [1 if x > 50 else 0 for x in range(100) if x % 2 == 0]
print(result)

source_list = [1, 2, 4, 8, 16, 32]

result_dict = {i ** 2: i ** 3 for i in source_list}
print(result_dict)

result_set = {i for i in range(100)}
print(result_set)

result_tuple = (x for x in range(100))
print(result_tuple)

x = None