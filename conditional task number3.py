experience = 2
languages = ["python", "typescript", "javascript", "java"]
contractType = "b2b"

if experience >= 2 and "python" in languages and "javascript" in languages:
    if contractType == "b2b" or contractType == "employment":
        print("Kandydat jest przyjęty !!!")
else:
    print("Kandydat nie został przyjęty.....")