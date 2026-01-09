#first n prime number
n = int(input())
count = 0
num = 2

while count < n:
    i = 2
    while i < num:
        if num % i == 0:
            break
        i = i + 1
    else:
        print(num)
        count = count + 1
    num = num + 1
    