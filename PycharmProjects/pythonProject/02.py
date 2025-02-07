# how to print list value basically array and insert new values

DataList = [1, 'This is', 0, 'List values', 100, 'x', 450, 500]

print(DataList[-1])  #will print last value
print(DataList[2:5]) #will print value from 2 to 4

DataList.insert(4, 1500)
print(DataList)

Datalist2  = [100, 500, 'This is string']

print(Datalist2[-1])

Datalist2.insert(3,'added via command')  #used to add new values
print(Datalist2)

Datalist2[3] = 'Added Via Command after list' #Used to update values
print(Datalist2)

Datalist2.append('This is end of list') #used to add values at the end
print(Datalist2)

del Datalist2[-1] #used to delete any value from the list
print(Datalist2)