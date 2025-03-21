number_one_integer = int(input("number one: "))
number_two_integer = int(input("number two: "))
number_three_floating = float(input("number three: "))

#Operation math
operation_one = (number_one_integer * 2) * (number_two_integer / 2)
operation_two = (number_one_integer * 3) + number_three_floating
operation_three = (number_three_floating ** 3)

print("Operation one is: ", operation_one)
print("Operation two is: ", operation_two)
print("Operation three is: %.2f" %operation_three)
