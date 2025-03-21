note = int(input("Input your note: "))

while (note > 10 or note < 0):
    print("Note invalid, try again!")
    note = int(input("Input your note, again: "))
    print("Your note valid is: ", note)
