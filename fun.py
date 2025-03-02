# def greet():
#     print("hello,welcome to python")
# greet()

# def add(a,b):
#     return a+b

# print(add(3,3))

# def sub(a,b):

    
#     return a-b

# print(sub(5,2))

# def divide(a,b):
#     return a/b

# print(divide(12,6))

# def mul(a,b):
#     return a * b

# print(mul(2,6))


#Keyword arguments

# def emp_details(name,age):
#     print(f"Name:{name},Age:{age}")

# emp_details(age=25,name="shilpa")

def sum_numbers(*args):
    return sum(args)
print(sum_numbers(3,5,6))

def shilpa(**kwargs):
    for key,value in kwargs.items():
        
        print(f"{key}:{value}")

shilpa(name="pooja",age=25)    
#write a function that take any number of numbers as argument and returns there sum
def sum_number(*args):
    return sum(args)   

#write a function that accepts employee names and any number of details like age ,grade and city,designation, salary all the things

def shilpa(name,kwargs):
 for key,value in kwargs.items():
 
  print(f"{key}:{value}")

shilpa(name="pooja",age=25,designation="Data Analyst")
          

           







# import sys
# #print(sys.builtin_module_names)

# #import math
# #print(dir(math))
# #print(dir(sys))
# for item in dir(sys):   #---it gives function in list module- it is called Loop function
# print(item)



    