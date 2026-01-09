def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_primes(n):
    s = 0
    for i in range(2, n+1):
        if is_prime(i):
            s += i
    return s

n = int(input("Enter n: "))
print(sum_primes(n))
