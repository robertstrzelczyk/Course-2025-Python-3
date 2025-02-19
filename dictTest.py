config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassword" : "12345"
}

print(config)
print(len(config))
print(config["dbType"])

for key, values in config.items():
    print("Key: " + key + " Values: " + values)