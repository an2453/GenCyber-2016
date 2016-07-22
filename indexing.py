# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:06:45 2016

Anusua Nath
GenCyber 2016
Indexing and Cryptography - Caesar Cipher

@author: student
"""


'''
#A more in-depth look at string indexing

strng = "Pokemon GO is addicting"
print(strng[8])
print(strng[8:13])

seg = strng[8:13]
print(seg)

print(strng[8:])

print(strng[:13])

print(strng[-1:])
print(strng[-1])
print(strng[-23])
print(strng[-13:-8])
'''

'''
PSEUDO CODE CAESAR CIPHER
 1. Name your finction, Two parameter: string and integer.
 2. Create a string that will contain no characters (emptystring = '' OR "")
 3. Start a for loop that loops through each character in your unencrypted 
    message.
    a. Turn each character into an ASCII number using the ord function.
    b. Save that ASCII number into a variable.
    c. Add the shift to the ASCII variable.
    d. Have a conditional statement that will substract the ASCII variable if 
       it's greater than the range of letter.
    e. Change ASCII variable to a character using the chr function.
    f. emptystring += character_variable
 4. Return the encrypted string
'''


'''
def encryptCC (message, shift):
    encrypted = "" #Empty string where we will add and encrypted char to every iteration of the for loop
    for char in message: #A for loop that goes through each char of the string
        x = ord(char) #Convert char into ASCII equivalent
        if x >= 65 and x <= 90: #Checks if ASCII/char is within uppercase range
            x += shift #shiftedx = x + shift // adds shift to ASCII
            if x > 90: #If ASCII goes out of range, subtract 26 to complete the wrap
                x -= 26
            encrypted += chr(x) #Changing ASCII variable into char, adding this char to empty string
        elif x <= 122 and x >= 97: #Checks if ASCII/char is within lowercase range
            x += shift #Adds shift to ASCII
            if x > 122: #Subtract 26 to complete the wrap
                x -= 26
            encrypted += chr(x) #Changing ASCII variable into char, adding this char to empty string
        #elif x == 32: 
            #encrypted += " " 
        #OR else:
            #encrypted += chr(x) OR encrypted += char
    print(message, "shifted by", shift)
    return encrypted
        
print(encryptCC("I'm going to rob you", 5))
print(encryptCC("Don't forget about me", 2))
print(encryptCC("three lights are lit but the fourth one's out", 13))
'''


def decryptCC(encrypted): #one parameter called encrypted. string var
    for i in range(26):  # for loop that goes through numbers 0-26
        decrypted = "" #empty string every iteration of the for loop
        for char in encrypted: 
        #for loop inside for loop that loops through ea. char in string
            asc = ord(char) #convert char to ascii value
            if asc >= 65 and asc <= 91: #check if upper
                asc -= i #decrypt shift
                if asc< 65: #checks if ascii value is below 65 range
                    asc+= 26 #if true, add 26 to make it a letter
                decrypted += chr(asc) #add the decrypted char to decrypted string
            elif asc <= 122 and asc>=97: #check if lower
                asc -= i
                if asc<97:
                    asc+=26 
                decrypted +=chr(asc)
            else:
                decrypted += char #adds random char (not letter) to string
        print(i, decrypted) 
        #print each different variation of CC in the first for loop
    return (True) 

decryptCC("yvppp, kyv wcrz zj:trvjriuzvuzedrity") 
decryptCC("jgaaa, vjg hnck ku:ecguctfkgfkpoctej")
#testing decryption 

        

    





















       


