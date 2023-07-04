contacts = {
    "John": "john@example.com",
    "Jane": "jane@example.com",
    "Bob": "bob@example.com"
}

print(contacts["Jane"])

contacts["John"] = "john.doe@example.com"

if "Alice" in contacts:
    print("The key 'Alice' exists in the dictionary.")
else:
    print("The key 'Alice' does not exist in the dictionary.")

del contacts["Bob"]

for key, value in contacts.items():
    print(key, "->", value)
