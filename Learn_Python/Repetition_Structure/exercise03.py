name = str(input("Enter with a name: "))
size_name = len(name)

while size_name <= 3:
    print("name invalid, try again!")
    name = str(input("Enter with a name, again: "))
    size_name = len(name)
