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


# Operatory przynaleznosci

numbers = [1,2,3,4,5,6,7,8,9,10]

if (7 in numbers):
    print("7 znajduje się w kolekcji numbers")

animals = ("pies", "wąż", "żółw")

if ("kot" not in animals):
    print("kot nie znajduje się w krotce animals")

user = {
    "name" : "Adam",
    "age" : "20"
}

if ("name" in user):
    print("klucz 'name' znajduje się w słowniku user")


# Operatory tożsamości

text = "Hello"

print (dir(text))
print(text.upper())

x = 256
y = 256

print (x is y)

listOne = [1,2,3,4,5]

listTwo = listOne

print(listOne is listTwo)


listOne.append(6)

if(listOne is listTwo):
    print("Zmiana kolekcji")

listThree = [1,2,3,4,5,6]

if(listThree is listOne):
    print("Ta sama kolekcja to nie jest")


# Operator konkatenacji ( łaczenie znaków poprzez +)

firstName = "Jan"
lastName = "Kowalski"
fullName = firstName + " " + lastName
print(fullName)

listOne = [1,2,3]
listTwo = [4,5,6]

combinedList = listOne + listTwo
print(combinedList)

if (len(combinedList) > 5):
    print("Lista jest za długa")

greeting = "Hello"
print(greeting)
greeting = greeting + " " + fullName
print(greeting)