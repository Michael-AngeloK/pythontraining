products = [
    {"name": "Laptop", "price": 999, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 10},
    {"name": "Keyboard", "price": 75, "stock": 0},
    {"name": "Monitor", "price": 300, "stock": 3}
]

# Filter out-of-stock items out
in_stock = list(filter(lambda x: x["stock"] > 0, products))

# print(f"Items in stock: {in_stock}")


# Apply 10% discount\
    
discounted_product = list(map(lambda x: {**x, "price":round(x["price"] * 0.9)}, products))

# print(f"Discounted products: {discounted_product}")


# Sort by value
sorted_by_value = sorted(products, key=lambda x: x["price"] * x["stock"], reverse=True)

# print("Sorted by value: ", sorted_by_value)


# Conditional price labeling
price_label = list(map(lambda x: f"{x['name']}: {'Expensive' if x['price'] > 100 else 'Affordable'}", products))

print(price_label)