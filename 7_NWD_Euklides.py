""" Zadanie 7 Stwórz funkcję do znajdowania największego wspólnego dzielnika dwóch
liczb. (algorytm Euklidesa) """

def Euklides(a,b):
    # funkcja znajduje najwiekszy wspolny dzielnik dwoch liczb
    lst = [a, b]
    a = max(lst)
    b = min(lst)
    c = a % b
    if c != 0:
        a = b
        b = c
        return Euklides(a, b)
    else:
        return print(f"{b} jest najwiekszym wspolnym dzielnikiem liczb a i b")

Euklides(282,78)