from sort import Sort
from search import Search

# EX 1
ex_1_l = [40, 10, 30, 20, 50]

ex_1_1_l = ex_1_l.copy()
Sort.Selection(ex_1_1_l, 2)
print("\nEX 1.1:", ex_1_1_l)

ex_1_2_l = ex_1_l.copy()
Sort.Insertion(ex_1_2_l, 2)
print("\nEX 1.2:", ex_1_2_l)

# EX 2
ex_2_l = [3, 8, 15, 20, 24, 30, 45, 52, 60, 72, 85]
print("\nEX 2.1:", Search.Linear(ex_2_l.copy(), 30, True))
print("\nEX 2.2:", Search.Binary(ex_2_l.copy(), 30, True))

# EX 3
ex_3_l = ["André", "Bruno", "Carlos", "Daniela", "Fernanda", "Gustavo", "Helena", "Isabel", "José", "Luís"]
print("\nEX 3.1:", Search.Linear(ex_3_l.copy(), "José", True))
print("\nEX 3.2:", Search.Binary(ex_3_l.copy(), "José", True))

# EX 4
ex_4_l = [34, 7, 23, 32, 5, 62, 32, 2, 14, 53]

print("\nEX 4.1:")
ex_4_2_list = ex_4_l.copy()
ex_4_1_swaps = Sort.Selection(ex_4_2_list, None, True)
print(f"Swaps: {ex_4_1_swaps}")

print("\nEX 4.2:")
ex_4_2_list = ex_4_l.copy()
ex_4_2_swaps = Sort.Insertion(ex_4_2_list, None, True)
print(f"Swaps: {ex_4_2_swaps}")

print("\nEX 4.3.1:", Search.Binary(ex_4_2_list, 34, True))

print("\nEX 4.3.1:", Search.Binary(ex_4_2_list, 33, True))