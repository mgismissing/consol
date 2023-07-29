c0 = 0
c1 = 0
c2 = 0
def add(a, b, c):
    c = a + b
def sub(a, b, c):
    c = a - b
def mul(a, b, c):
    c = a * b
def div(a, b, c):
    try:
        c = a / b
    except ZeroDivisionError:
        c = a
def out(a):
    print(a)