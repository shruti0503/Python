new=["apple", "orange", "kiwi", "mango"]
newlist=[]

for x in new:
    if "a" in x:
        print(True)
        newlist.append(x)
    else:
        print(False)
print("new list is", newlist)

#using list compression
#synatx newlist=[expression for item in iterable if condition==True]
fruits =["apple", "orange", "kiwi", "mango" ]
newOne=[x for t in fruits if "a" in t]
newSecond=[x for x in fruits if x!="apple"]
print("new One is",newOne)
print("second one is", newSecond)

#The iterable can be any iterable object, like a list, tuple, set etc.
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
# newlist = [x.upper() for x in fruits]

#Set the values in the new list to upper case:
newThird=[x.upper() for x in fruits]
print("third one is", newThird) 

# setting to outcome to whatever we like 
newFourth=['hello' for x in fruits]
print("fouth one is", newFourth)

print("original is", fruits) # original remains unchnaged creates a new one instead

#return bnana instead of orange
newFifth=[x if x!="orange" else "banana" for x in fruits]
print(newFifth)


# True
# True
# False
# True
# new list is ['apple', 'orange', 'mango']
# new One is ['mango', 'mango', 'mango']
# second one is ['orange', 'kiwi', 'mango']
# third one is ['APPLE', 'ORANGE', 'KIWI', 'MANGO']
# fouth one is ['hello', 'hello', 'hello', 'hello']
# original is ['apple', 'orange', 'kiwi', 'mango']
# ['apple', 'banana', 'kiwi', 'mango']

# Using list comprehension to iterate through loop 
List = [character for character in 'Geeks 4 Geeks!'] 
  
# Displaying list 
print(List) 
#Output

['G', 'e', 'e', 'k', 's', ' ', '4', ' ', 'G', 'e', 'e', 'k', 's', '!']
#Time Analysis in List Comprehensions and Loop
#The list comprehensions in Python are more efficient both computationally and in terms of coding space and time than a for a loop. Typically, they are written in a single line of code. The below program depicts the difference between loops and list comprehension based on performance.

Python
# Import required module 
import time 
  
  
# define function to implement for loop 
def for_loop(n): 
    result = [] 
    for i in range(n): 
        result.append(i**2) 
    return result 
  
  
# define function to implement list comprehension 
def list_comprehension(n): 
    return [i**2 for i in range(n)] 
  
  
# Driver Code 
  
# Calculate time taken by for_loop() 
begin = time.time() 
for_loop(10**6) 
end = time.time() 
  
# Display time taken by for_loop() 
print('Time taken for_loop:', round(end-begin, 2)) 
  
# Calculate time takens by list_comprehension() 
begin = time.time() 
list_comprehension(10**6) 
end = time.time() 
  
# Display time taken by for_loop() 
print('Time taken for list_comprehension:', round(end-begin, 2))