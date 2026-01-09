def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y-1)

def armstrong(n, digits):
    if n == 0:
        return 0
    return power(n % 10, digits) + armstrong(n // 10, digits)

num = int(input("Enter number: "))
d = len(str(num))

if armstrong(num, d) == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")
