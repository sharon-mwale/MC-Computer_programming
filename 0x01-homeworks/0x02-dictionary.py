if __name__ =="__main__":
    student = {
        "name": "John",
        "age": 20,
        "grade": "A"
    }

    print(student["age"])

    student["city"] = "New York"

    if "grade" in student:
        print("The key 'grade' exists in the dictionary.")
        del student["age"]
    else:
        print("The key 'grade' does not exist in the dictionary.")

    keys = list(student.keys())
    print(keys)

