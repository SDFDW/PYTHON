#percentage and marks
n = int(input("enter students:"))
total_percentage = 0

for i in range(n):
    total = 0
    for j in range(5):
        marks = int(input())
        total = total + marks
    
    percentage = total/5
    print("Percentage:",percentage)
    total_percentage = total_percentage + percentage

avg = total_percentage / n
print("Average:",avg)

