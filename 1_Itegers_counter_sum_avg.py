"""Stwórz program, który będzie pobierał od użytkownika liczby całkowite tak długo,
aż ten nie wciśnie control+D – wówczas ma się pojawić informacja o tym,
 ile liczb całkowitych użytkownik podał, jaka jest ich suma oraz średnia."""

def Itegers():
    """ This program asks user for an integer as long as one clicks control + D
    - then it gives information about how many integers the user has given,
    what is their sum and average."""
    counter = 0
    sum = 0
    while True:
        try:
            n = int(input("Enter integer \n"))
            sum += n
            counter += 1
        except ValueError:
            print("Entered wrong value. It has to be integer")
        except EOFError:
            return f"You have given {counter} numbers. Their sum is {sum} and average is {sum/counter}"

print(Itegers())