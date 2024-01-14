import random
import string

upperstr = string.ascii_uppercase
lowerstr = string.ascii_lowercase
number = "0123456789"
character = "!@#$%^&*()"
all = upperstr + lowerstr + number + character

length = int(input("enter length password: "))
password = "".join((random.sample(all, length)))
print("your password: ", password)
