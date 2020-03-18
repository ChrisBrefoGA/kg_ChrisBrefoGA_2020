#this is the code for my Kargo coding challenge Program
import sys
arglist = sys.argv #this is the argument list for the strings
if len(arglist) > 1:#if the right number of args have been typed in the command line
    string1 = arglist[1]#string1/arg1 for the program
    string2 = arglist[2]#string2/arg2 for the program
else:#if the wrong number of arguments haven't been provided by the user
    print("Not enough arguments. Please provide 2 separate strings.")#error statement
    exit()
str1Arr = []#this is the array for the first string
str2Arr = []# this is the array for the second string

count = 0#this variable is for string length in
         #the chance that string1 is longer than string2

res = True#response boolean that determines whether
          #the answer false or true will be printed

"""
insertChars checks the validity of the one-to-one mapping for each character
in string1. So, if a1(string1 character) has already been put in the array
then, it checks if a1)is associated with the same character a2. If a2(string2 character)
is a different character from the first occurrence of a1 then the program will return False,
if a2 is the same then it returns True.
param: a1 is the character in string1, a2 is the character in string2
returns: True if the characters were put in the array, False otherwise
"""
def insertChars(a1,a2):
    if a1 in str1Arr:#if a1 is already in the string array
        position = str1Arr.index(a1)#finds the index of the previous occurrence
        if a2 == str2Arr[position]:#if a2 is the same as a1's previous mapping 
            str1Arr.append(a1)#insert into the string1 array
            str2Arr.append(a2)#insert into the string2 array
            return True
        else:#if a2 isn't the same as a1's previous mapping 
            return False
    else:#if it's not already in the string array
        str1Arr.append(a1)#insert into the string1 array
        str2Arr.append(a2)#insert into the string2 array
        return True

for char1 in string1:# runs through each character in the first string
    if count < len(string2):#in the case string2 is smaller then string1 
       char2 = string2[count]#gets the character from string2 in the same position as char1
       res = insertChars(char1,char2)#runs insertChars with char1 and char2
                                     #to get the one-to-one mapping validity    
    else:#if string1 is bigger then string2 and hasn't got a multiple mapping occurrence
        break
    if res == False:#if string1 has a multiple mapping occurrence then break the loop
        break
    count += 1#increase count by 1
    
if res == True: sys.stdout.write("true")#if res stays true then string1 and string2 has a one-to-one mapping
else: sys.stdout.write("false")#if res becomes false then string1 and string2 doesn't have a one-to-one mapping
        
