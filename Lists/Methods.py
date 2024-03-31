
a=["shruti"]
a.append("w")
a.append("w")
print(a)  # ['shruti', 'w', 'w']
#a.clear()
new=a.copy()
print("copied",new) # copied ['shruti', 'w', 'w']

print("count", a.count("w")) #count 2

a.extend(["3", "5"])
print(a) #['shruti', 'w', 'w', '3', '5']

print("index", a.index("5")) #index 4
a.insert(2,"added")
print("after adding", a) #after adding ['shruti', 'w', 'added', 'w', '3', '5']

print("after popping last value popped is", a.pop()) #after popping last value popped is 5
print("removing the  first element with specific value", a.remove("3")) # prints : NONE removing the  first element with specific value None
print(a) #['shruti', 'w', 'added', 'w']

print("reverse of the list", a.reverse()) #reverse of the list None
print(a) #['w', 'added', 'w', 'shruti']

a.sort()
print("after sorting", a) #after sorting ['added', 'shruti', 'w', 'w']