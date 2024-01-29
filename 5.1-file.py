#1

with open("file1.txt", "r") as file1:
    lines = file1.readlines()[:2]

# Write the two lines read from file1.txt to file2.txt
with open("file2.txt", "w") as file2:
    file2.writelines(lines)

# Read file2.txt and print the contents
with open("file2.txt", "r") as file2:
    contents = file2.read()
    
    print(contents)


