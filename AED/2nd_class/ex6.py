from random import random as rng

list = [-5 , 5, 10, 15, 20, -234]

neg = 0
pos = 0

for i in list:
    if i < 0:
        neg+=1

pos = list.__len__() - neg
print(f"neg: {neg}, pos: {pos}")