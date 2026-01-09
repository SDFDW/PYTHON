#Palindrome (3-digit number)
n = int(input("Enter three digit number: "))

rev = (n%10)*100 + ((n//10)%10)*10 + (n//100)

if n == rev:
    print("Palindrome number")
else:
    print("Not palindrome")