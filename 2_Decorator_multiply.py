"""Stwórz dekorator o nazwie multiply, który przyjmuje argument n i
zwiększa n-krotnie rezultat wykonania udekorowanej funkcji """

def dekorator_multiply(n = 1):
    def dekorator(func):
        def wrapper(arg):
            result = func(arg)
            try:
                return float(result) * n
            except ValueError:
                for x in range(n-1):
                    print(func(arg))
                return func(arg)
        return wrapper
    return dekorator

@dekorator_multiply(4)
def func(variable):
    return f"{variable}"

print(func('tekst'))
print(func(4))
print(func(4.3))
print(func(True))



