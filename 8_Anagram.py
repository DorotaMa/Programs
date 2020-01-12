""" Zadanie 8 Napisz funkcję, która przyjmuje dwa stringi i sprawdza, czy są swoimi
anagramami. Np.
„army” i „Mary”,
„dzielenia” i „niedziela”,
„Quid est veritas?” i „Vir est qui adest”,
„Jim Morrison” i „Mr Mojo Risin”
„Tom Marvolo Riddle” i „I am Lord Voldemort”"""

def Anagram(napis1, napis2):
    # funkcja sprawdza czy napis 1 i napis 2 są swoimi anagramami
    napis1 = napis1.replace(" ", "")
    napis2 = napis2.replace(" ","")
    napis1 = napis1.lower()
    napis2 = napis2.lower()
    slownik1 = {}
    slownik2 = {}
    for litera in napis1:
        slownik1[litera] = slownik1.get(litera, 0) + 1
    for litera in napis2:
        slownik2[litera] = slownik2.get(litera, 0) + 1
    return slownik1 == slownik2

print(Anagram('Quid est veritas', 'Vir est qui adest”' ))

def anagrams(napis1, napis2):
    napis1 = napis1.lower().replace(" ", "")
    napis2 = napis2.lower().replace(" ", "")
    return sorted(napis1) == sorted(napis2)

print(anagrams('Quid est veritas', 'Vir est qui adest”' ))
print(anagrams("Tom Marvolo Riddle", "I am Lord Voldemort"))
print(anagrams("Ala ma kota", "Kot ma Alę"))