list = [20, 22, 24, 30, 19, 17, 12]

min = list[0]
max = list[0]

for n in list:
    if n > max:
        max = n
    elif n < min:
        min = n

print(min, max)