#Ticket Amount for 5 People
total = 0

for i in range(5):
    age = int(input("Enter age: "))
    price = int(input("Enter ticket price: "))

    if age < 12:
        total += price * 0.7
    elif age > 59:
        total += price * 0.5
    else:
        total += price

print("Total ticket amount:", total)