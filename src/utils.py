import os
import json

def product_json(path):
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file
        data = json.load(file)

    return data

def create_object(data):
    name = []
    for name in data:
        products = []
        for products in name:
            products.append(**products)


