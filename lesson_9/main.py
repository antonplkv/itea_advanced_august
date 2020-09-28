from flask import Flask, render_template

app = Flask(__name__)


@app.route('/products')
@app.route('/products/<product_name>')
def hello(product_name=None):
    products_db = {
        'Strawberry': {'count': 40, 'price': 20},
        'Orange': {'count': 50, 'price': 30},
        'Banana': {'count': 100, 'price': 10}
    }
    if not product_name:
        return render_template('index.html', products=products_db)
    else:
        product = products_db.get(product_name, {'count': 0, 'price': 0})
        product['total_price'] = product['count'] * product['price']
        product['name'] = product_name if product_name in products_db else 'Несуществующая позиция'
        return render_template('product_page.html', product=product)


if __name__ == '__main__':
    app.run(host='127.0.0.2', port=4444, debug=True)