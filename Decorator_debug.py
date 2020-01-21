"""Zadanie 1 Stwórz dekorator o nazwie debug, który podczas wywoływania funkcji będzie
 wyświetlał informacje o jej nazwie, przekazanych parametrach oraz zwracanym wyniku"""

def debug(function):
    def wrapper(*args):
        result = function(*args)
        return f"You called {function.__name__} with given parameters: {args}  " \
               f"The outcome of the function is {result}"
    return wrapper

@debug
def function_examp(a, b, c):
    return a + b * c

print(function_examp(3,2,4))