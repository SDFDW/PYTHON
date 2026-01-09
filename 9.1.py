def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def sum_fact(n):
    if n == 1:
        return 1
    return fact(n) + sum_fact(n-1)

n = int(input("Enter n: "))
print("Sum =", sum_fact(n))
