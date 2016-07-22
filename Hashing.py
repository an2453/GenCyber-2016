# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 09:38:13 2016

Anusua Nath
Gencyber2016
Hashing

@author: student
"""



import hashlib #Add the hash library

def md5(fname): #Begin defining your md5 hash
    hash_md5 = hashlib.md5() #Prepare to hash 
    with open(fname, "rb") as f: #Open a file
        for chunk in iter(lambda: f.read(4096), b""): #For each 4096 byte chunk of file
            hash_md5.update(chunk) #We gonna hash dat
    return hash_md5.hexdigest() #Gibs hash pls
    
#Obj: find 2 files that look the same but have different hashes
#Make sure the script and pictures are in the same folder
print(md5("00263048.jpg"))
print(md5("01321152.jpg"))

print(md5("whitest_shirt_ever.jpg"))
print(md5("ocean_breeze.jpg"))

'''
for i in range(1, 31):
    filename = "/home/student/Desktop/walls/the_wall" + str(i) + ".png"
    print(filename, " ", md5(filename))
#6, 14, 18, 22, 
 '''   