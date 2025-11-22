#password generator
import random
import string
def genrate_password(Length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
length = int(input("enter the length of password:"))
print("generated password is:",genrate_password(length))
