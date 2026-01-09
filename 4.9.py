#Numbers divisible by a given number
n = int(input("Enter range limit: "))
d = int(input("Enter divisor: "))

for i in range(1, n+1):
    if i % d == 0:
        print(i)