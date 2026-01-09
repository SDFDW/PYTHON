#Reverse three-digit number
n = int(input("Enter three digit number: "))

a = n // 100
b = (n // 10) % 10
c = n % 10

rev = c*100 + b*10 + a

print("Reverse number:", rev)