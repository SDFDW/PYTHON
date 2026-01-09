def fibonacci(n):
    a, b = 1, 1
    print(a, b, end=" ")
    for i in range(n-2):
        c = a + b
        print(c, end=" ")
        a, b = b, c

n = int(input("Enter number of terms: "))
fibonacci(n)
