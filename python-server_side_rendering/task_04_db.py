import os
import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def get_data_from_json():
    with open('products.json', 'r') as file:
        data = json.load(file)
    return data['items']

def get_data_from_csv():
    items = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(row)
    return items

def get_data_from_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    conn.close()
    
    items = []
    for row in rows:
        items.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return items

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        items = get_data_from_json()
    elif source == 'csv':
        items = get_data_from_csv()
    elif source == 'sql':
        items = get_data_from_sql()
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        items = [item for item in items if item['id'] == product_id]
        if not items:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)