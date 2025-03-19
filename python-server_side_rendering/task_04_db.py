#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
        items = data["items"]
    return render_template('items.html', items=items)


@app.route('/products')
def product_display():
    source = request.args.get('source', type=str)
    id = request.args.get('id', type=int)
    if source == "json":
        try:
            with open('products.json', 'r') as file:
                items = json.load(file)
        except FileNotFoundError:
            items = ["Wrong source"]
    elif source == "csv":
        try:
            with open('products.csv', newline='', mode='r') as file:
                csv_reader = csv.DictReader(file)
                items = [row for row in csv_reader]
        except FileNotFoundError:
            items = ["Wrong source"]
    elif source == "sql":
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
        except ConnectionError:
            items = ["Product not found"]
            return render_template('/product_display.html', items=items)

        query = "SELECT * FROM Products"
        try:
            cursor.execute(query)
            results = cursor.fetchall()
        except sqlite3.DatabaseError:
            items = ["Product not found"]
            return render_template('/product_display.html', items=items)
        items = []
        for el in results:
            new_el = {
                "id": el[0],
                "name": el[1],
                "category": el[2],
                "price": el[3]
            }
            items.append(new_el)

    else:
        items = ["Wrong source"]

    if items != ["Wrong source"]:
        if id or id == 0:
            try:
                item = items[id]
                items = [item]
            except IndexError:
                items = ["Product not found"]

    return render_template('/product_display.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
