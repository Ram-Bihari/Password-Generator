import random

print('Welcome to your password generator!')

chars = '`1234567890-=qwertyuiopasdfghjklzxcvbnm~!@#$%^&*_QWERTYUIOPASDFGHJKLZXCVBNM'

number = int(input('Amount of passwords to generate: '))

length = int(input('Password length: '))

print('\n here are your passwords: ')

for pwd in range(number):
    passwords= ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)