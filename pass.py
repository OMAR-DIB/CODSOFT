import string as s
import random as rand

add=s.ascii_letters
add+=s.digits
add+=s.punctuation


length=input('Enter the length of your password: ')
while True:
    
        try:
            length=int(length)   
            if length<6:
                 length=input('Enter bigger length: ')
            else :
                 break
        except:
            length=input('Enter the length again: ')
    
password=""


for x in range(length):
    password+=rand.choice(add)

print(password)


