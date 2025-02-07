
str = "shrutipatel715@gmail.com"
str1 = "CSU Student"
str3 = "patel"

print(str[2])  #will print 2nd no latter

print(str[6:11]) #will print data between this range

print(str + str1) #will combine both string

print(str3 in str)  #will check that string 3 is in string 1 or not

print(str3 in str1)

var = str.split("@")  #wil split the string from given values
print(var)
print(var[0])


str2 = " Testing "

print(str2.strip())  #strip will remove space from lest and right side
print(str2.lstrip())
print(str2.rstrip())

s = "Test"
i = 0

# print("{} {}".format(s, i))