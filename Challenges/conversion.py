decimalNum = 45.6789
wholeNum = int(decimalNum)
print(type(wholeNum))
print(wholeNum)
signs = "4321"
num = int(signs)
print (num)
wholeNum2 = 123
nums = int(wholeNum2)
print(type(nums))
signs2 = "98.76"
nums2 = float(signs2)
print(type(nums2))
print(nums2)

listData = [1,2,3,4]
tupleData = tuple(listData)
print(tupleData)
print(type(tupleData))

tuple2 = ("AAA", "BBB")
newList = list(tuple2)
print(newList)
print(type(newList))

numbers = [7,8,9,10,11,12]
print(numbers)
tupleNumbers = tuple(numbers)
print(tupleNumbers)

mixedList = ["AAa", 1231, 111.55]
print(mixedList)
setMixed = set(mixedList)
print(setMixed)
frozenSetNumbers = frozenset(tupleNumbers)
print(frozenSetNumbers)
nameAgePairs = ( ("Marek", 23), ("Ola", 20))
ageDict = dict(nameAgePairs)
print(ageDict)

#muttable vs immuttable

number = 5
print(id(number))
number = number +2
print(id(number))
fruits = ["apple", "banana", "cherry"]
print(id(fruits))
fruits.append("orange")
print(fruits)
print(id(fruits))