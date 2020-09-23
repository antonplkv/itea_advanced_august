import sqlite3

# parking_car_id = int(input('Enter car on parking'))
# connection = sqlite3.connect('lesson_8.db')
# cursor = connection.cursor()
# cursor.execute('SELECT car_price, car_colour FROM parking WHERE id=?', (parking_car_id, ))
#
# for data in cursor:
#     print(data)
# connection.close()


def add_car(car_colour, minutes_on_parking, car_model, car_price):
    connection = sqlite3.connect('lesson_8.db')
    cursor = connection.cursor()
    data = (car_colour, minutes_on_parking, car_model, car_price)
    cursor.execute("INSERT INTO parking ('car_colour', 'minutes_on_parking', 'car_model', 'car_price') VALUES(?, ?, ?, ?)", data)
    connection.commit()
    connection.close()


add_car('RED', 30, 'FIAT', 10000)