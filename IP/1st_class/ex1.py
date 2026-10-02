def q1() -> None:
    res = (float(input("n1:")) + float(input("n2: ")))
    print("res:", res, "\n")

def q2() -> None:
    res = sum(([i for i in range(5)]))
    print("res:", res, "\n")

def q3() -> None:
    res = ([i for i in range(5)])
    print("res:", res, "\n")

def q4() -> None:
    res = (float(input("w: ")) * float(input("h: ")))
    print("res:", res, "\n")

def q5() -> None:
    res = 2**3
    print("res:", res, "\n")

def q6() -> None:
    res = 4**2
    print("res:", res, "\n")

def q7() -> None:
    print("res:", "Hello world", "\n")

def q8() -> None:
    try:
        res = ((float(input("n1: ")) * float(input("n2: ")) * float(input("n3: "))) + 2) / 0
        print("res:", res, "\n")
    except:
        print("res:", "Computers can't divide by 0 :)", "\n")

def q9() -> None:
    res = (2/(5**3))/100
    print("res:", res, "\n")

def q10() -> None:
    res = sum([i for i in range(3)]) / 3
    print(res)

TASKS = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)

for task in TASKS:
    print(task.__name__)
    task()