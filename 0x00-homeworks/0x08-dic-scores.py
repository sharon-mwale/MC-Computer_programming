scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print(scores["Bob"])

scores["David"] = 95

if "Eve" in scores:
    print("The key 'Eve' exists in the dictionary.")
else:
    print("The key 'Eve' does not exist in the dictionary.")

del scores["Charlie"]

for key, value in scores.items():
    print(key, "->", value)
