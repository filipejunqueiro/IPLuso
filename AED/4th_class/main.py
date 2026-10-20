from random import randint as RNG

sorted_list = sorted(RNG(1, 1_000_000) for _ in range(1_000_000))

def binary_search(list: list[int], target: int):
    start = 0
    end = list.__len__() - 1

    while start <= end:
        middle = (start + end) >> 1

        if list[middle] == target:
            return True
        # Se o valor encontrado for menor que o alvo,
        # descartamos a metade esquerda
        elif list[middle] < target:
            start = middle + 1
        # Se o valor encontrado for maior que o alvo,
        # descartamos a metade direita
        else:
            end = middle - 1
    return False

print(binary_search(sorted_list, 900_000))