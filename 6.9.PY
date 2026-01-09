#ALPHATICCAL TRIANGLE
for i in range(1, 6):

    # spaces
    for j in range(1, 6 - i):
        print(" ", end=" ")

    # alphabets
    K = 65   # ASCII of 'A'
    for j in range(1, 2*i):
        print(chr(K), end=" ")
        K += 1

    print()


