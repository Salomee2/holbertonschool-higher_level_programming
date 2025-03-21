from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products_data = read_json('products.json')
    elif source == 'csv':
        products_data = read_csv('products.csv')

    if product_id:
        filtered_products = [product for product in products_data if int(product['id']) == product_id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found", source=source)
        products_data = filtered_products

    return render_template('product_display.html', products=products_data, source=source)

if __name__ == '__main__':
    app.run(debug=True, port=5000)