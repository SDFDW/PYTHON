# prime or not

n = int(input("Enter number: "))

for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    if n > 1:
        print("Prime number")
    else:
        print("Not prime")