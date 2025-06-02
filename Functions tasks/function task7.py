def calculateHumanYears(dogAge):
    if (dogAge <= 2):
        dogAge = dogAge * 10.5
        return dogAge
    elif dogAge > 2:
        dogAge = 21 + (dogAge - 2) * 4
        return dogAge
    
while True:
    dogAge = int(input("Podaj wiek psa: "))
    age = calculateHumanYears(dogAge)
    print("Wiek psa wynosi: " + str(age))