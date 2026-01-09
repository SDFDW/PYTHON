#Total salary of employee
basic = float(input("Enter basic salary: "))

da = basic * 10 / 100
ta = basic * 12 / 100
hra = basic * 15 / 100

salary = basic + da + ta + hra

print("Total salary:", salary)