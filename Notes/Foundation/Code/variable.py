#All the important imports for the understanding of the file.
import keyword

#1  Basic assignment
name = "Yash"
age = 21
cgpa = 8.2
print(name, age,cgpa)

#2 Multiple assignments
a, b, c = 10, 20, 30
print(a, b, c)

#3 Same value to many variables
a = b = c = 10
print(a, b, c)

#4 Swapping without a temp variable
a, b = 10, 20
print("Before Swapping : ", a, b)
a, b = b, a
print("After Swapping : ", a, b)

#5 Dynamic typing datatype changes with value
a = "yash"
print(a, type(a))
a = 21
print(a, type(a))
a = 8.35
print(a, type(a))

#6 Variable and references
a=100
b=a
print(id(a)==id(b)) # True
b=200
print(id(a)==id(b)) # False
print(a, b)

#7 Valid vs Invalid
print("user_name".isidentifier())   #True
print("2cool".isidentifier())       #False
print("my var".isidentifier())      #False
print("_name".isidentifier())       #True

#8 Keywords you cannot use as a name
print(len(keyword.kwlist))
print(keyword.kwlist)
print(keyword.iskeyword("class"))

#9 Constants by convention and case sensitivity
PI = 3.14159
MAX_USERS = 100
name = "Yash"
Name = "Rawat"
print(PI, MAX_USERS, name, Name)

#10 del and NameError
city = "Haldwani"
print(city)
del city
city="Almora"
try:
    print(city)
except NameError as e:
    print("Error : ", e)
