# Zadanie 1 #
krotka = (50, 100, 150, 200, 250)
print(type(krotka))
print(len(krotka))
print(krotka[len(krotka) -1])
print(krotka[1:4])
print(krotka[-3])


# Zadanie 2 #

krotkaBankowa = (100, 200, 300, 400, 500, 600)
summary = 0

for krotka in krotkaBankowa:
    summary += krotka

print(summary)