import random, string

password_length = 8

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for index in range(password_length):
    password = password + random.choice(characters)

print("Password generated: {}".format(password))