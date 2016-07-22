# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 09:58:57 2016

Anusua Nath
GenCyber 2016
Loops.py

@author: student
"""


'''
WHILE loop - loop that keeps running code until a certain condition is met

While loop will stop running after loop is met
'''


'''
import randon 
#this imports a random library inside my code
#a library is a collection of functions

myint = 465 #type of counter

while myint > 400:
    #edit my "counter"
    myint = myint-5
    #myint -=5
    print(myint)
'''   


'''
guess = int(input("Guess my number"))
number = random.randint(0, 100)

#Number Guessing Game Loop
    
while guess != number:
    if number < guess:
        print("This number is too big")
    else:
        print("This number is too small")
    guess = int(input("Guess again"))
    
print("Congrats, the number is correct")
print("Your number was", number)
'''


'''
Prompt: Guess the password
Write a while loop that checks if a string (called a password) is the same as 
the guessed password

The actual password should be 4 characters long, using all capital letters of 
the alphabet.
You can set your own password in the program.
The loop should let the guesser know is the password is wrong or not.

myguess = input("Enter a password")
password = "DUCK"

while myguess != password:
    print("Nope! Guess again!")
    myguess = input("Enter a password")
    
print("Fabulous! You got the password!")
'''


'''
#FOR LOOP
for i in range(1, 11): #i is a variable that exists inside my for loop
    print(i)
    
for i in range (10):
    print(i)
    
string = "Do you wanna be my lover"
for char in string: #goes through each character in the string
    print(char)
'''


'''
def ascii_to_eight_bit(letter):
    num = ord(letter)
    bitstring = ""
    for i in range(8):
        print(num)
        if num % 2 == 0:
            bitstring = '0' + bitstring
            print('0')
        else:
            bitstring = '1' + bitstring
            print('1')
        num = num // 2
    return bitstring

print(ascii_to_eight_bit('S'))
'''


'''
Write a funtion to check whether a password follows these rules:
    - Must be at least 6 characters long
    - Must contain at least one capital letter
    - Must contain at least one lowercase letter

If password fulfills all the requirements, return a boolian
return True - if password works
return False - if the password is missing some specifications
*function that takes a string
    
Use the for loop!

Remember:
for char in string --> will allow you to loop through each character in a string
len(string) gives you the length of the string
ASCII table capital/lowercase
'''


'''
def check_password (password):
    hasUpper = False
    hasLower = False
    longenough = False
    if len(password) > 6:
        longenough = True
    else:
        for char in password:
            if ord(char) in range(65, 91):
                hasUpper = True
            elif ord(char) in range(97, 123):
                hasLower = True
    if hasUpper == True and hasLower == True and longenough == True:
        return True
    
check_password("Digest")
 '''


        
    
            

















