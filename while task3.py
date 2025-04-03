elements = int(input("Podaj liczbę elementów: "))
sum = 0

if elements == 0:
    print("Nie można obliczyć średniej arytmetycznej z 0 elementów")
else:
    i = elements
    while i > 0:
        i -= 1

        num = float(input("Podaj liczbę: "))
        sum += num

average = sum / elements
print("Średnia arytmetyczna wynosi: ", average)