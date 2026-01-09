def armstrong(n):
    temp = n
    s = 0
    digits = len(str(n))
    while n > 0:
        d = n % 10
        s += d ** digits
        n //= 10
    return s == temp

n = int(input("Enter number: "))
if armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong")
