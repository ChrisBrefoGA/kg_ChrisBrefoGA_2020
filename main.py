#this is the coding for my Kargo coding challenge

print("type in a string")
string1 = input()
print("type in another string")
string2 = input()
str1Arr = []#this is the array for the first string
str2Arr = []# this is the array for the second string

count = 0# this variable is for string length in
         #the chance that string1 is longer than string2
res = True

def insertChars(a1,a2):
    if a1 in str1Arr:
        position = str1Arr.index(a1)
        if a2 == str2Arr[position]:
            str1Arr.append(a1)
            str2Arr.append(a2)
            return True
        else:
            return False
    else:
        str1Arr.append(a1)
        str2Arr.append(a2)
        return True

for char1 in string1:
    if count < len(string2):
       char2 = string2[count]
       res = insertChars(char1,char2)     
    else:
        break
    if res == False:
        break
    count += 1
if res == True: print("true")
else: print("false")
        
