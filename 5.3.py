#Ticket Amount and Discount

n = int(input)
cost = int(input())
total = 0
for i in range(n):
    age = int(input())

    if age < 12:
        total = total + cost * 0.7
    elif age < 59:
        total = total + cost * 0.5
    else:
        total = total + cost
print(total)


   
