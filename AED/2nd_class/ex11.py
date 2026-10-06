cart = [("Pizza", 10), ("Apple", 4), ("Apple", 4)]
cart_len = cart.__len__()
duplicated = False

for i in range(cart_len):
    if cart[i][0] == cart[cart_len - 1][0]:
        duplicated = True

    if i == cart_len:
        break

print(duplicated)