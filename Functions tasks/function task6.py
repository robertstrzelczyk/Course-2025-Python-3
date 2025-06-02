def displayShoppingList(shoppingList):
    print("Lista zakupów:")
    for item in shoppingList:
        print(item)

shoppingList = []

while True:
    product = input("Wpisz kolejny produkt do listy:")
    if product == "koniec":
        break
    shoppingList.append(product)

displayShoppingList(shoppingList)