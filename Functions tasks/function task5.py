def cToF(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print (str(celsius) + " stopni Celsjuszsa to " + str(fahrenheit) + " stopni Fahrenheita")
    return fahrenheit

def fToC(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print (str(fahrenheit) + " stopni Fahrenheita to " + str(celsius) + " stopni Celsjusza")
    return celsius


print(cToF(20))
print(fToC(86))
