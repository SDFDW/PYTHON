for i in range(1, 5):
    print("1", end=" ")
    for j in range(1, i-1):
        print(j+1, end=" ")
    if i > 1:
        print("1", end=" ")
    print()