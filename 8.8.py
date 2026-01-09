def reverse_num(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

n = int(input("Enter number: "))
print(reverse_num(n))
