import shelve

FILENAME = 'DICT_DB'

# with shelve.open(FILENAME) as db:
#     db['Ukraine'] = 'Kiev'


# with shelve.open(FILENAME) as db:
#     db['cart'] = ['tomato', 'cucumber']

with shelve.open(FILENAME) as db:
    print(list(db.items()))


with open('new_file.txt', 'w') as file:
    file.write(212121)