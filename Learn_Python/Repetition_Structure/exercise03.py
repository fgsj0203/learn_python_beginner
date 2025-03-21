name = str(input("Enter with a name: "))
size_name = len(name)

while size_name <= 3:
    print("name invalid, try again!")
    name = str(input("Enter with a name, again: "))
    size_name = len(name)

age = int(input("Enter with your age: "))
while (age < 0) or (age > 150):
    print("Age invalid, try again!!")
    age = int(input("Enter again your age: "))

salary = float(input("Enter your salary: "))
while salary < 0:
    print("Salary invalid, try again!")
    salary = float(input("Input your salary, again: "))

gender = str(input("Enter with your gender: "))
lower_gender_letter = gender[0].lower()
while (lower_gender_letter != "f") and (lower_gender_letter != "m"):
    print("gender invalid, try again!")
    gender = str(input("Enter with your gender: f or m "))
    lower_gender_letter = gender[0].lower()

state_civil = str(input("Enter with you state civil: "))
lower_state_civil_letter = state_civil[0].lower()
while (lower_state_civil_letter != "s") and (lower_state_civil_letter != "c") and (lower_state_civil_letter != "v") and (lower_state_civil_letter != "d"):
    print("State civil is invalid, try again!")
    state_civil = str(input("Enter with you state civil: "))
    lower_state_civil_letter = state_civil[0].lower()

print(name)
print(age)
print(salary)
print(gender)
print(state_civil)
