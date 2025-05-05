numbers = [-4,-3,-2,-1,0,1,2,3,4]

for n in numbers:
    if n == 0:
        print("Zero jest parzyste")
    elif n % 2 == 0:
        print(n, "jest parzyste")
    else:
        print(n, "jest nieparzyste")



    data = (1,2,3,4,5,6,7,8,9,10)

    for v in data:
        if v % 2 == 0:
            print(v, "jest parzyste")