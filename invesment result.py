capital = 5000
rateOfInteres = 0.08
inflationRate = 0.15

earned = capital * rateOfInteres
print(earned)

lost = capital * inflationRate
print(lost)

newCapital = capital + earned - lost
print("Nowy kapitał:", newCapital)