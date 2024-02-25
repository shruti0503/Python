
#Control statements in Python are used to manage the flow of 
# execution in a program. They include conditional statements (if, elif, else),
# loops (for and while), and the break, continue, and pass statements. Here's an overview:

x = 10
if x > 5:
    print("x is greater than 5")


y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")


z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 1

for number in range(10):
    if number == 5:
        break
    print(number)

for number in range(10):
    if number % 2 == 0:
        continue
    print(number)

for item in iterable:
    # TODO: Add code here
    pass
