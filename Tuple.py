#tuples -> immutabe
#round brakctes, with one item , tuple constructor
var = ("Geeks", "for", "Geeks")
print(var)

#with one itemn
values: tuple[int | str,...]=(1,2,4,"Geek")
print(values)

tup=(1,2,"shruti")
print(tup)
tupz=[1,2,"rr"]
print(tupz)

print 
#<class 'tuple'>
#<class 'str'>

#Tuple constructor in Python
tuple_constructor=tuple(("dsa", "dev"))
print(tuple_constructor)

# Tuples in Python are similar to Python lists but not entirely. Tuples are immutable and ordered and allow duplicate values. Some Characteristics of Tuples in Python.

# We can find items in a tuple since finding any item does not make changes in the tuple.
# One cannot add items to a tuple once it is created. 
# Tuples cannot be appended or extended.
# We cannot remove items from a tuple once it is created. 

# Python tuples are ordered and we can access their elements using their index values. They are also immutable, i.e., we cannot add, remove and change the elements once declared in the tuple, so when we tried to add an element at index 1, it generated the error.print("Value in Var[-3] = ", var[-3])

#operations:

#nested tupple 
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

#creating tuple with repetition
Tuple1=('Geeks')*3 #GeeksGeeksGeeks
Tuple1=('Geeks',)*3 #('Geeks', 'Geeks', 'Geeks')

print("\n Tuple with repetition:")
print(Tuple1)

#creating Tuple with the use of loop
Tuple1=('Geeks')
n=5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1=(Tuple1,)
    print(Tuple1)
    
#concatennation
# Concatenation of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')
 
Tuple3 = Tuple1 + Tuple2
 
# Printing first Tuple
print("Tuple 1: ")
print(Tuple1)
 
# Printing Second Tuple
print("\nTuple2: ")
print(Tuple2)
 
# Printing Final Tuple
print("\nTuples after Concatenation: ")
print(Tuple3)


#slicing
tup=tuple("gfgbjhb bjhbj")
print("removal of first ele",tup[1:])

#reversing
print("Tuple after sequence of Element is reversed", tup[::-1])

# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(tup[4:9])
#Printing elements between Range 4-9: 
#('j', 'h', 'b', ' ', 'b')

#Deleting a Tuple 
Tuple1=(0,1,2,3,4)
#del Tuple1

print("ele at index",tup.index("g"))
print("ele at ")

#count, all-> return a true if all elements are true or iof tuple is empty

# any() true is any elemnt of the tuple is true, if tuple is empty , return false

#len() returns length of the tuple or size of the tuple

#enumaertae() retunr a enumerate obje ct pof tbe tuple

print(enumerate(tup))

# Often, when dealing with iterators, we also need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task. The enumerate () method adds a counter to an iterable and returns it in the form of an enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function.

#Syntax: enumerate(iterable, start=0)

# Parameters:

# Iterable: any object that supports iteration
# Start: the index value from which the counter is to be started, by default it is 0
# Return: Returns an iterator with index and element pairs from the original iterable

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
 
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))


l1 = ["eat", "sleep", "repeat"]
 
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
 
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print (count, ele)
 
# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)
    
print("max is",max(tup))
# Syntax : max(arg1, arg2, *args[, key]) 

# Parameters : 

# arg1, arg2 : objects of the same datatype
# *args : multiple objects
# key : function where comparison of iterable is performed based on its return value
# Returns : The maximum value 

var1 = (3,10)
var2 = (4,5)
var3 = (9,0)
 
max_val = max(var1, var2, var3)
print("max is",max_val) #max is (9, 0)
print("min is", min(var1, var2, var3)) #min is (3, 10)

numbers = [1,2,3,4,5,1,4,5]
 
Sum = sum(numbers)

 
Sum = sum(numbers, 10)

print("sum", sum(var1)) # string tupple pr kaam nhi krega
