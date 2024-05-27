import random
print("Welcome to our Random Password Generator")
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num='123456789'
symbol='!@#$%^&'
string=lower+upper+num+symbol
l=6
password="".join(random.sample(string,l))
print("Generated password=",password)

