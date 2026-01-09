#Divisible by 7 and multiple of 5 (in a range)
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for i in range(start, end+1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)