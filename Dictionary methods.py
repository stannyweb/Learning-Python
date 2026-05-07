products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

# product.items() if I wanna iterate over the keys and the values.
for price in products.values():
    print(price)


for product, price in products.items():
    products[product] = round(price * 0.80)

print(products)


# With enumerate

for index, product in enumerate(products, start=3):
    print(index, product)