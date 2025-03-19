# Operatory przypisania
balance = 1000
balance += 7000
balance -= 2000
balance *= 3
balance -= 4000
balance += 4000
balance /= 3
balance -= 4000
print(balance)

# Operatory porównania

print(15 > 10)
print(5 == 5)

x = 20
y = 30

print(x < y)
print(100 <= 101)

if (50 != 20):
    print("50 nie jest równe 20")

if ('hello' == 'goodbye'):
    print("hello jest równe goodbye")


# Operatory logiczne


age = 12
height = 150

if (age >= 10 and height >= 140):
    print("Osoba może przejechać się rollecoasterem")


hoursWorked = 9
projectFinished = True

if (hoursWorked > 8 and projectFinished == True):
    print("Możesz iść do domu")

temp = 35

if (temp < 0 or temp > 30):
    print("Ekstremalne warunki pogodowe")

isHoliday = False

if (not(isHoliday)):
    print("Dziś jest dzień roboczy")

errorsFound = 12
warnings = 1

if (not(errorsFound < 10 and warnings == 0)):
    print("Sprawdź kod jeszcze raz")