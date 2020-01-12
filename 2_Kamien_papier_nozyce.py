znaki_wygrane = {
    'K': 'N',
    'N': 'P',
    'P': 'K',
}

znaki_nazwy = {
    'K': "Kamien",
    'P': "Papiper",
    'N': "Nozyce",
}

punkty_user = 0
punkty_komputer = 0
while punkty_user < 3 and punkty_komputer < 3:
    wybor_usera = input("Co wybierasz \n")
    wybor_komputera = choice(["k", "n", "p"])
    if znaki_wygrywanie[wybor_usera] == wybor_komputera:
        print(f"Wybrales {znaki_nazwy[wybor_usera]}, komputer: {znaki_nazwy[wybor_komputera]}, wygrales")
        punkty_user += 1
    elif znaki_wygrywanie[wybor_komputera] == wybor_usera:
        print(f"Wybrales {znaki_nazwy[wybor_usera]}, komputer: {znaki_nazwy[wybor_komputera]}, przegrales")
        punkty_komputer += 1
    else:
        print(f"Oboje wybraliscie {znaki_nazwy[wybor_usera]}, jest remis")

if punkty_komputer > punkty_user:
    print("Przegrales")
else:
    print("Wygrales")


# Choice - wybiera element z danej listy/obiektu
# Randint - losuje liczbe intiger
