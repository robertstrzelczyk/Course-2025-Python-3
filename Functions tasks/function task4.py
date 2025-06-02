def findLargest(num1, num2):
    if num1 > num2:
        print("num1 jest większa: " + str(num2))
        return num1
    elif num1 == num2:
        print("Obie liczby są równe")
    else:
        print("num2 jest większe od: " + str(num1))
        return num2
    
    
print(findLargest(3, 10))
print(findLargest(12,7))