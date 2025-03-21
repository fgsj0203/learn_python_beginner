worked_hours_month = int(input("Amount hours worked in month: "))
work_value_hour = float(input("Your received value in hour worked: "))

#Operations for calculate
brute_salary = worked_hours_month * work_value_hour
ir_discount = brute_salary * 0.11
inss_discount = brute_salary * 0.08
sindicate_discount = brute_salary * 0.05
salary_liquid = brute_salary - (ir_discount + inss_discount + sindicate_discount)

#Printing values
print("Salary brute is: R$ %.2f" % brute_salary)
print("value of discount IR: R$ %.2f " % ir_discount)
print("value of discount INSS: R$ %.2f " % inss_discount)
print("Your salary liquid is: R$ %.2f " % salary_liquid)
