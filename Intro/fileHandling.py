# file handling -> reading and writing from files
# -> open()
file_path="example.txt"

file_path = "example.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)


# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, this is a new file!")


# Appending to a file
with open("output.txt", "a") as file:
    file.write("\nAppending additional content.")

# reading a file line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character
        
        
#handling exceptions
try:
    with open("nonex", "r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"An error occurred: {e}")
    
#using with statement
with open("example.txt", "r") as file:
    content=file.read()
    