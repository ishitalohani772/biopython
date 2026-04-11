print("i am ishita lohani")

name = "ishita lohani"
marks = "90"
favourite = "mango"
print ("my name is", name)
print ("my marks in science", marks)
print ("my favourite fruit is", favourite)
age = "23"
print (type(age))
x = 5
y = 10
sum = x+y
print (sum)
diff = x-y
print (diff)
product = x*y
print (x*y)
div = x/y
print (x/y)

weight = 50
height = 5.6
bmi = weight/(height*height)
print(bmi)
radius = 10
pi = 3.14
area = pi*(radius*radius)
print(area)
principle = 1000
rate = 5
time = 3
x = 100
si = principle*rate*time/x
print(si)
length = 12
breadth = 16
perimeter_of_rectangle = 2*(length+breadth)
print(perimeter_of_rectangle)
print(type(breadth))
print("perimete of rectangle is",perimeter_of_rectangle)
area_of_rectangle = length*breadth
print(length*breadth)
print("area of rectangle is",area_of_rectangle)
x = None
y = True
z = False
print (type(y))
print(type(z))

print(type(x))
s1 = 15
s2 = 15
area_of_square = s1*s2
print(area_of_square)
perimeter_of_square = 4*s1
print(perimeter_of_square)
print(type(s1))
print("area of square is", area_of_square)
print("perimeter of square is", perimeter_of_square)
print(type(perimeter_of_square))
print(type(z))
x = 12
y = 15
sum = x+y
print(x+y)
print(type(x))
print("sum of x and y is" , sum)  #this is my first code
a = 12
b = 4
print(a+b)  
print (a-b) 
print(a*b)
print(a/b)
print(a//b)
print(a%b)
x = 12
y = 8
print(x%y)
print(x!=y)
a = 12
b = 7
c = 8
d = 6
print(a>b and c>d)
print(a>b and b>c)
print(a>b or b<c)
print("ishita")
print(name[2])
print(name[-4])
#slicing 
print(name[0:4])
print(name[:6])
print(name[::-1])
#upper strings
# strip emoves extra spaces
msg = "     hello    " 
print(msg)
print(msg.strip())
# replace = it replace any part of the string
text = "i love to eat icecream"
print(text.replace("icecream","pizza"))
# count helps in counting 
DNA = "ATGCGTAATTA"
print(DNA.count("A"))
print(DNA.count("G"))
print(DNA.count("T"))
#find helps to find a substring/index/position
text = "i love to eat ice cream"
print(text.find("icecream"))
print(text.find("i"))
# f string = string formatting, helps in changing the variable
name = "vedu"
age = "12"
print(f"my name is {name} and i am {age} years old")
# concatenation = addition of two strings
a = "hello"
b = "world"
print(a+b)
# input = it is used to take information from the user
name = input("enter your name")
a = input("enter first number")
b = input("enter second number")
print(a+b)
# conversion/casting = to convert one data type into another data type' also called type conversion
# types = implicint conversion and explicit conversion
# implicit converrsion  converts automatically where it is needed
x = 5
y = 2.5
z = x+y
print(z)
# explicit conversion 
x = "10"
x = int(x)
# list methods
# append = add items at the end
fruits = ["apple","mango","banana"]
fruits.append("kiwi")
print(fruits)
# insert = add items in the specific position, we provide index to add at specific location
fruits.insert(1,"litchi")
print(fruits)
# remove = it removes a  specific item 
fruits.remove("banana")
print(fruits)
# pop = it removes item by index
fruits.pop(2)
print(fruits)
print(fruits)
# sort = sort in ascending order
fruits.sort()
# reverse = to reverse the list 
fruits.reverse()
print(fruits)
numbers = [13,11,16,88,2,8,99,36]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
# list is also mutable, we can change the items of the list
fruits = ["apple","banana","mango"]
fruits[1] = "kiwi"
print(fruits)
# nested list = a list insde another list
students = [
    ["riya","24"]
["aman","20"]
["harsh","24"]
]
print(students[1])




