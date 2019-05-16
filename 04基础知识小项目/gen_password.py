import random

CHARS = "ABCDEFGHIJKLSMNOPQESTUVWXYZ"
Special_char = ",./;'!@#$%^&*()_."
chars = "abcdefghijklmnopqrstuvwxyz"

Desc_char = CHARS + Special_char + chars

PassLength = int(input("please input your the length of your password:"))
password = ""
for i in range(PassLength):
    password += random.choice(Desc_char)

print(password)