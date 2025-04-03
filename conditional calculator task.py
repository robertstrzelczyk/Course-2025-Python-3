dog_age = int(input('Podaj wiek psa: '))

if dog_age < 0:
    print("wiek psa nie może być mniejsza niż 0")
elif dog_age <= 1:
    human_age = dog_age * 15
elif dog_age <= 2:
    human_age = 15 + (dog_age - 1) * 9
elif dog_age > 2:
    human_age = 24 + (dog_age - 2) * 5

print("Wiek psa wynosi: ", human_age)
