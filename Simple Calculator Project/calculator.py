num = 0
operation = None
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]
exit = "exit"

while True:
    if reset == True:
        num = int(input("Podaj liczbę: ")) # Użytkownik podaję liczbę początkową
        reset = False
     
     ## Użytkownik podaje operacje arytmetyczna
    operation = input("Podaj operację takie jak: " + str(calcOperations) + "lub koniec lub reset: ")
    if operation == exit: break
    if operation == "reset":
       reset = True
       continue

    if not operation in calcOperations:
        print("Wprowadzona została błędna operacja")
        continue

    secondNum = int(input("Podaj drugą liczbę: "))

    if operation == "+":
        result = num + secondNum

    if operation == "-":
        result = num - secondNum

    if operation == "*":
        result = num * secondNum

    if operation == "/":
        result = num / secondNum

    if operation == "**":
        result = num ** secondNum

    print ("Wynik " + str(num) + " " + operation + " " + str(secondNum) + " = " + str(result))
    num = result
    result = None
