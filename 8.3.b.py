def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def sum_factorial(n):
    s = 0
    for i in range(1, n+1):
        s += factorial(i)
    return s

n = int(input("Enter n: "))
print(sum_factorial(n))
