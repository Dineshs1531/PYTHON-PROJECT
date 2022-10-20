import random
print("WELCOME TO PASSWORD GENERATOR ")
c='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*/?>:;'
s=int(input("enter the how many password needed : "))
len=int(input("how many length of the password : "))

print("your passwords are: ")
for j in range(s):
    j=''
    for f in range(len):
        j+=random.choice(c)
    print(j)