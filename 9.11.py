def reverse_num(n):
    if n < 10:
        return n
    return int(str(n % 10) + str(reverse_num(n // 10)))

n = int(input("Enter number: "))
print("Reverse =", reverse_num(n))
