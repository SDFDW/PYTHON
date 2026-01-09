#Captcha Program
uid = input("Enter userid: ")
pwd = input("Enter password: ")

if uid=="admin" and pwd=="1234":
    captcha = 1234
    print("Captcha:", captcha)
    x = int(input("Enter captcha: "))

    if x == captcha:
        print("Login success")
    else:
        print("Captcha failed")
else:
    print("Invalid userid or password")