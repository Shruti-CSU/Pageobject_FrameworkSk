print("Hello from this side")

# Defining more veriables

a, b, c = 100, 0.5, "This is string"

print("{} {}".format("The value is", b))

print("{} {}".format(a, b))

print(type(a))
print(type(b))
print(type(c))

X, Y, Z = "This is", 10, "raw"

print("{} {} {}".format(X, Y, Z))

DataArray = [100, "This is String", 2.05, "Zoom"]

print(DataArray[-1])

DataArray.insert(2, 15000)
print(DataArray)

DataArray.append("This is last value")
print(DataArray)

del DataArray[-1]
print(DataArray)

print(type(DataArray))

#tupple diclaration

TuppleA = ("This is first value", 250, 450.45, "This is last")
print(TuppleA[0])
print(TuppleA[-1])

#Tupple do not support data modification

#Dictionary Declaration

Dic01 = {"A":152.23, "B":"This is string 1", 1:100, 2 : "This is sting 2"}
print(Dic01["B"])
print(Dic01[1])
