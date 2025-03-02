# String Manupulation- it is a inbuilt functions or methods used to manipulate the strings

#string is a collection of characters
#single or double quotes of creating string
string1='hello'
string2="hello"

string3=""" this is multiline string
this is used to store more character in variable"""

print(string1,string2,string3)

txt="python"
# positive index- In python indexing starts with zero - left to right
print(txt[0])
print(txt[3])

#Negetive index - in python indexing starts with -1 in reverse order-  Right to left

print(txt[-1])
print(txt[-4])

# Slicing used to extraction of substring
# Syntax :  string(start,end,step)

text="python programming"
print(text[0:6])
print(text[0:])
print(text[0:7])  #--- extracting sub string Python
print(text[7:])
print(text[:7])
print(text[:])
print(text[7:1])  #----extract programming

# Reverse order
print(text[::-1]) #-----Reverse a string

print(text[::2]) #----extract every second character -- Step value


# String concatination

string1='hello'
string2="world"

# using operators
print(string1 + " " + string2)


# using Join

print(" ".join([string1.string2]))