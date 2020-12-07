import requests
import random
import os

categories = ["alimentos", "acessorios", "limpeza", "remedios"]
path = r"C:\Users\David\Pictures\petshop"
products = [
    {
        "name": "Racao whiskas",
        "price": 15.00,
        "discount": False,
        "category": categories[0],
    },
    {
        "name": "Ração para Cães Adultos Pedigree Carne",
        "price": 119.99,
        "discount": True,
        "category": categories[0],
    },
    {
        "name": "Shampoo Pet Clean 3 Em 1 para Cães - 5 Litros",
        "price": 48.50,
        "discount": False,
        "category": categories[2],
    },
    {
        "name": "Simparic 80mg, 20,1 até 40kg, 03 Compr Zoetis para Cães",
        "price": 199.80,
        "discount": True,
        "category": categories[3],
    },
    {
        "name": "Dog Toilet Furacão Pet, Grade Azul Furacão Pet para Cães",
        "price": 62.99,
        "discount": True,
        "category": categories[1],
    },
]

files = [
    [("image", ("whiskas.png", open(f"{path}\\whiskas.png", "rb"), "image/png"))],
    [("image", ("pedigree.png", open(f"{path}\\pedigree.png", "rb"), "image/png"))],
    [("image", ("shampoo.png", open(f"{path}\\shampoo.png", "rb"), "image/png"))],
    [("image", ("simparic.png", open(f"{path}\\simparic.png", "rb"), "image/png"))],
    [("image", ("toilet.png", open(f"{path}\\toilet.png", "rb"), "image/png"))],
]


def add_discount(products):
    new_products = []
    for product in products:
        if product["discount"]:
            product["discount_price"] = round(random.uniform(10.0, 30.0), 2)
        product["discount_price"] = 0.0
        new_products.append(product)
    return new_products


products = add_discount(products)

for product, image_file in zip(products, files):
    response = requests.post(
        "http://localhost:5005/products", headers={}, data=product, files=image_file
    )

    print(response.text)