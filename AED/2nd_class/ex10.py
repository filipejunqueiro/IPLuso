prod_list = [("Bread", 1), ("Pizza", 10), ("Apple", 4)]

prod_names = ""
final_price = 0

for prod in prod_list:
    prod_names += prod[0]+" "
    final_price += prod[1]

print(f"price: {final_price}$\nprods: {prod_names}")