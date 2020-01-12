""" Napisz funkcję która sprawdzi, czy dana liczba jest liczbą narcystyczną
(n-cyfrowa liczba naturalna która jest sumą swoich cyfr podniesionych do
potęgi n) np.
153 = 1^3 + 5^3 + 3^3
9474 = 9^4 + 4^4 + 7^4 + 4^4 """

def narcyz(b):
    zmienna_pom = b  # tworze zmienna pomocnicza, ktora zawiera poczatkowa wartosc b
    lst = []
    sum = 0
    while b != 0:    # rozbijam liczbe b na pojedyncze cyfry i tworze z nich liste
        lst.append(b % 10)
        b = b // 10
    for elem in lst:
        sum += elem ** len(lst)   # sumuję potegi poszczegolnych cyfr z listy. wartosc potegi jest dlugoscia listy
    return lst, len(lst), sum, zmienna_pom == sum

print(narcyz(9474))