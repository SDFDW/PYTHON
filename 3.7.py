#Check Userid and Password
uid = input("Enter userid: ")
pwd = input("Enter password: ")

if uid=="admin" and pwd=="1234":
    print("Login successful")
else:
    print("Invalid userid or password")