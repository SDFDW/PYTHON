#Armstrong Numbers in Range
start = int(input())
end = int(input())

for num in range(start, end+1):
    temp = num
    sum = 0
    digits = len(str(num))

    while temp > 0:
        d = temp % 10
        sum = sum + d**digits
        temp = temp // 10

    if sum == num:
        print(num)