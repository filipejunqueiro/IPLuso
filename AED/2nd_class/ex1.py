def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

TASKS = (sum, sub, mul, div)

x, y = 106.54, 89

for task in TASKS:
    print(f"{task.__name__}: {task(x, y):.2f}")