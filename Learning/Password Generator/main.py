import random

print("Password Generator")
print('==================')

numOfPwd = int(input('No of Passwords?'))
pwdLen = int(input('Password Length?'))


def PasswordGenerator(numOfPwd, pwdLen):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*=().,<?'
    for num in range(numOfPwd):
        pwd = ""
        for len in range(pwdLen):
            pwd += random.choice(chars)
        print(pwd)


PasswordGenerator(numOfPwd, pwdLen)
