gender_people = str(input("Enter with your gender: F or M?\n"))
letter_string_list = gender_people[0]
lower_letter = letter_string_list.lower()



if lower_letter =="f":
    print("Female")
elif lower_letter == "m":
    print("Male")
else:
    print("Gender invalid")
