import json

cart = {
    'tomato': 10,
    'meat': 2,
    'carrot': 5,
    'milk': 1
}
print(type(cart))
print(cart)


result_json = json.dumps(cart)
print(type(result_json))
print(result_json)

result_dict = json.loads(result_json)
print(result_dict)
print(type(result_dict))


file = open('test.json', 'w')
json.dump(cart, file)
file.close()

print('!!!')
file = open('test.json', 'r')
result = json.load(file)
print(type(result))
file.close()