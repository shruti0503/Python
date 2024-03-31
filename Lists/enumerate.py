# In Python, `enumerate` is a built-in function that adds a counter to an iterable
# (e.g., a list, tuple, string, etc.) and returns an enumerate object. 
# This object contains pairs of elements from the original iterable along with their respective index 
# or position.

# The `enumerate` function is commonly used in loops when you need to access both the index 
# and the value of elements in an iterable. Here's how `enumerate` works:

### Syntax:

# enumerate(iterable, start=0)


# - `iterable`: The iterable (such as a list, tuple, string, etc.) that you want to enumerate.
# - `start` (optional): The optional parameter that specifies the starting index of the enumeration.
# By default, it starts from 0.

### Example:

my_list = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(my_list):
    print(index, fruit)


### Output:
# ```
# 0 apple
# 1 banana
# 2 cherry
# ```

### Explanation:

# - In this example, `enumerate` is used to iterate over the `my_list`.
# - Inside the loop, `enumerate` returns pairs of (index, value) for each element in the list.
# - The loop iterates over these pairs, unpacking them into the `index` and `fruit` variables.
# - Each iteration of the loop prints the index and the corresponding element from the list.

### Additional Notes:

# - The `enumerate` function is particularly useful when you need both the index and 
# the value of elements in an iterable within a loop.
# - By default, `enumerate` starts the index from 0, but you can specify a different starting
# index using the `start` parameter.
# - The `enumerate` object returned by the function can be converted to a list of tuples or used 
# directly in loops, as shown in the example above.
# - Using `enumerate` avoids the need for maintaining a separate counter variable in the loop,
# making the code more concise and readable.