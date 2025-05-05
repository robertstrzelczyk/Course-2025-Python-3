numbers = [-3,-2,-1,0,1,2,3]

set = {-1}

for num in numbers:
    if num % 2 != 0:
        set.add(num)


for n in set:
    print(n)