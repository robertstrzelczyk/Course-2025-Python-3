def createUser(name, concat):
    userDictonary = {
        "name": name,
        "email": None,
        "telephone": None
    }
    concatTypeString = isinstance(concat, str)
    concatTypeInt = isinstance(concat, int)
    if (concatTypeString):
        userDictonary["email"] = concat
    elif (concatTypeInt):
        userDictonary["telephone"] = concat

    return userDictonary

print(createUser("Ola", "ola@example.com"))
print(createUser("Kasia", 987654321))

    