# tuples = like list, but cannot be changed (imutable)
# sets = unordered collection with no duplicates
number = (1,2,3,4,5)
fruits = ("apple","banana","mango")

print(fruits[1])
name = ["raj","meena","suhana"]
name[0] = "harsh"
print(name)
name[2] = "ishita"
print(name)
# tuples are fastest than list
# they are safe, because they are imutable
dna_bases = ["A","T","G","C"]
dna_bases[3] = "F"
print(dna_bases)
dna_bases[2] = "R"
print(dna_bases)
# they are good for fixed data
# count
t = (1,2,2,2,3)
print(t.count(2))
print(t.count(3))
# index
print(t.index(3))
# sets = collection of unique items, use curly brackets for sets
# key features = no duplicates
#                unordered(no indexing)
#                very fast for checking something
number = {1,2,2,3,4,4,4,4,4,5,6,1}
print(number)
# set operation
# union
A = {1,2,3,4}
B = {3,4,5,6}
print(A ,B)
# intersection = print common variables
print(A&B)
print(A-B)
print(B-A)

bases = {"A","T","G","C"}
print("A" in bases)
print("B" in bases)
# task = to removes using sets
number = [1,2,3,4,5,1,6,6]
unique_number = set(number)
print(unique_number)
unique_number = list(unique_number)
print(unique_number)
A = {1,2,3}
B = {4,5,6}
print(A,B)
numbers = A,B
print(A,B)
numbers =  list(numbers)
# dictionaries and loops
# dictionaries stores data in key value pairs , curly brackets are used for dictionary
bio = {'gene': 'BRCA1','function': 'DNA repair',
     'location': '17q21' }
#accessing values
print(bio["gene"])
print(bio["function"])
print(bio["location"])
# addig a new key - values pair
bio["protein"] = "breast cancer type 1"
print(bio["protein"])
bio["function"] = "tumor suppressor"
print(bio["function"])
# removing items
# pop = to remove one item
bio.pop("location")
print(bio)
# clear = to remove whole dictionary
bio.clear()
print(bio)
# dictionary methods
# nested dictionary

# loops = cantrolled structure that repeats a block of code multiple times until a specified condition is satisfied or
#  a sequence is completed
# two types of loops -
# for loops
# while loop
# for loop = repeats the code for each item in a list, string, or range
# range 
for i in range(1,6):
    print(i)
    # list 
    fruits = ["apple","banana","mango","orange"]
    for f in fruits:
        print(f)
# while loop = a while loop repeats a code untill it is true
 # conditional statements = if, elif , else
 # these help your python program make decisions
 # if statement :
    marks = 85
if marks>= 90:
    print("excellent")
    if marks<= 90:
        print("good")
        # identation
        age = 18
        if age>= 18:
         print("adult")
    marks = 75
    if marks>= 90:
       print("gragde A")
