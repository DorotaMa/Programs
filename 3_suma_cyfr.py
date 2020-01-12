""" Zadanie Napisz funkcję która policzy sumę cyfr liczby, nie zamieniając jej na
    stringa, ani listę. Rekurencyjnie oraz iteracyjnie."""

def suma_cyfr_iter(liczba):
    suma = 0
    while liczba:
        suma += liczba % 10
        liczba = liczba //10
    return suma

def suma_cyfr_rek(liczba):
    if liczba < 10:
        return liczba
    else:
        return suma_cyfr_rek(liczba // 10) + liczba % 10