if __name__ =="__main__":
    inventory = {
        "apples": 10,
        "bananas": 15,
        "oranges": 5
    }

    print(inventory["bananas"])

    inventory["oranges"] = 8

    if "grapes" in inventory:
        print("The key 'grapes' exists in the dictionary.")
    else:
        print("The key 'grapes' does not exist in the dictionary.")

    del inventory["apples"]

    values = list(inventory.values())
    print(values)
