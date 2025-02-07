with open('Text.txt', 'r') as readonly:
    obj1 = readonly.readline()
    reversed(obj1)
    with open('Text.txt', 'w') as writefile:
        for line in reversed(obj1):
            writefile.write(line)
