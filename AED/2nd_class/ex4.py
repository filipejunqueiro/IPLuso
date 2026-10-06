x, y, z = 50000, 1232103213, 21412412

def applyDiscount(n, disc):
    return n - (n * (disc / 100))

print(f"{applyDiscount(x, 10)}, {applyDiscount(y, 25)}, {applyDiscount(z, 35)}")