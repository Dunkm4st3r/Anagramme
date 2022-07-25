# Eingabe der Anagramme
anagramm1 = list(input("Anagramm1: ").lower())
anagramm2 = list(input("Anagramm2: ").lower())

if len(anagramm1) == len(anagramm2):
    # x iteriert durch die Buchstaben von anagramm1
    for x in anagramm1:
        # y durch die Buchstaben von anagramm2
        for y in anagramm2:
            # wenn ein gleicher Buchstabe gefunden wurde, dann lösche ihn aus dem zweiten Anagramm
            if x == y:
                # Buchstabe löschen
                anagramm2.remove(x)
            else:
                pass

# Wenn mind. ein Buchstrabe übrig geblieben ist, dann ist es kein Anagramm
if len(anagramm2) > 0:
    print("Kein Anagramm des jeweils anderen Wortes.")
else:
    print("Anagramm des jeweils anderen Wortes!")