import os, random, string

print('Section 11: Files')

helloFile = open('hello.txt')


name = "Jason"
chars = string.ascii_letters+string.digits

name_extra = str(random.choice(range(1000)))
username = name.lower() + name_extra + '@gmail.com'

password = random.choice(chars) for i in range (10)
#password = ''.join(random.choice(chars) for i in range (10))


print(username)
print(password)
