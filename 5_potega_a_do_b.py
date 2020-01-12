""" zadanie 5 Napisz funkcję pow(a, b), która będzie podnosiła a do b-tej potęgi. (Nie
używając poznanego operatora ** i zewnętrznych bibliotek).
Rekurencyjnie i iteracyjnie. """

def pow_iter(a, b):
    sum = 1
    for i in range(b):
        sum *= a
    return sum

def pow_reku(a, b):
    sum = a
    if b > 0:
        b = b - 1
        return sum * pow(a, b)
    else:
        return 1

print(pow_reku(3,0))
print(pow_reku(3,4))
print(pow_iter(3,0))
print(pow_iter(3,4))