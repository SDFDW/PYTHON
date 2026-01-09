#Userid & Password (3 attempts only)
uid = "admin"
pwd = "1234"

for i in range(3):
    u = input("Enter userid: ")
    p = input("Enter password: ")

    if u == uid and p == pwd:
        print("Login Successful")
        break
    else:
        print("Incorrect credentials")

else:
    print("Program terminated")