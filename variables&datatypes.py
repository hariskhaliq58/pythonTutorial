# variable declaration and assighn values
# variable name should be meaningful
# variable name should not start with number
# string data type variables can e declared in three ways
name = "haris"
name2 = 'haris'
name3 ='''haris'''  
age = 23
college = "comsats"
age2 = age
old = False
married = None

# print the variables
print(name)
print(name2)
print(name3)
print("my name is",name,"my age is",age2)

# how to check variable data types python automatically detect the data types of variables
print(type(name))
print(type(age))
print(type(age2))
print(type(college))
print(type(old)) 
print(type(married))

#input in python
name = input("enter your name:")
marks = int(input("enter your marks:"))#type casting only integer value can be considered otherwise it will give error
print("welcome", name)
print("your details are:")
print("name:",name)
print("marks:",marks)