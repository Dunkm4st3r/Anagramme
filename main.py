# Eingabe der Amagramme
anagramm1 = list(input("Anagramm1: ").lower())
anagramm2 = list(input("Anagramm2: ").lower())

# x iteriert durch die Buchstaben von anagram1
for x in anagramm1:
    # y durch die Buchstaben von anagram2
    for y in anagramm2:
        if x == y:
            anagramm2.remove(x)
        else:
            pass

if len(anagramm2) > 0:
    print("Kein Anagramm des jeweils anderen Wortes.")
else:
    print(" Anagramm des jeweils anderen Wortes!")