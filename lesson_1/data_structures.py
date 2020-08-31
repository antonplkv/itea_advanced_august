products = ['tomatoes', 'potato', 'strawberry', 123]
print(products[-1])
products.append('carrot')
products[-2] += 12
print(products)

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

list_1.extend(list_2)
print(list_1)

tuple_1 = 1,
print(tuple_1)

product_cart = {
    'potato': 3,
    'cherry': 2,
    'milk': 3,
    ('peach', 'banana'): {
        'peach': 5,
        'banana': 5
    },
}

#print(product_cart[('peach', 'banana')]['banana'])
print(product_cart.get('carrot', 0))

for k, v in product_cart.items():
    print(k, v)


my_set = {100, 3000, 100000, 2000, 10, 10}
print(my_set)