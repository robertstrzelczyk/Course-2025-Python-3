def calculateArea(length, width):
    return length * width

length = int(input("Podaj długość prostokąta: "))
width = int(input("Podaj szerokość prostokąta: "))

sum = calculateArea(length,width)

print(sum)