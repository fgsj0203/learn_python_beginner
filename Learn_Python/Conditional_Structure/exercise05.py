note_one = float(input("note one: "))
note_two = float(input("note two: "))
notes_average = (note_one + note_two) / 2.0

if notes_average == 10.0:
    print("Approved with distinction")
elif (notes_average >= 7.0) and notes_average <= 9.9:
    print("Approved")
else:
    print("Reproved, try again!!")

