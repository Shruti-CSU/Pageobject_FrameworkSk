# To read or write a file first we always has to open a file

varf = open('Text.txt')

# print(varf.read(4)) #This will read first 4 character in file

# print(varf.readline()) #This will print 1st line from file
# print(varf.readline()) #This will print 2nd line from file
# print(varf.read(5)) #now its already reach at line 3, it will print first 4 letter from line 3 only

# For entire file we can impliment loop that can actully check entire file

varL = varf.readline()

while varL!='':
    print(varL)
    varL = varf.readline()

# for loop for read file

print("This is from for loop")

for varL in varf.readline():
    print(varL)


varf.close() # This will close the open file

