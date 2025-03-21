weight_fish = int(input("What weight of fish: "))
tax_fish_weight = 0

#Using structure conditional
if weight_fish > 50:
    tax_fish_weight = (weight_fish - 50) * 4
    print("The value of tax weight exceeded is R$ %.2f" %tax_fish_weight)
else:
    print("Your free of payment tax of weight fish")
