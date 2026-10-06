prods = {
    "Apple": 0,
    "Pizza": 50,
    "Burger": 10,
    "Sugar Pack": 4
}

for name, stock in prods.items():
    if stock == 0:
        print(f"{name} as no stock!")
    elif stock < 5:
        print(f"{name} is low on stock! - ({stock})")
