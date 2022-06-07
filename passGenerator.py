# Password generator
import random

lowerAlphaList = ('abcdefghijklmnopqrstuvwxyz')
upperAlphaList = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
specialList = ('!@#$%^&*()-_<>?')
digitList = ('0123456789')
newPass = ''

allChar = lowerAlphaList + upperAlphaList + specialList + digitList

print('How long do you want the password to be? (8-64): ')
choice = input()
passLength = int(choice)

for i in range(passLength):
    if passLength > 64:
        break
    newPass = newPass + random.choice(allChar)

print(newPass)
