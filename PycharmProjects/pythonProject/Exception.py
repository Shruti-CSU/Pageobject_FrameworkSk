TotalItems = 0

#if TotalItems != 2:
    # raise Exception ("Total item count does not match")

if TotalItems != 2:
    pass

assert (TotalItems == 0)

# Try catch methods when you want to continue execution with failure cases

try:
    with open('filelog.txt', 'r') as file1: # Try to open file which does not exit in system
        file1.read()

except:
    print("Testcase reached in try catch module and its failure of run")

# Try catch method with actual error print

try:
    with open('filelog.txt' , 'r') as file2:
        file2.read()
except Exception as error: # this error is variable to print actual error
    print(error)

finally:  # This is use for clean up a data at then end of test
    print("This is the last block of test to clean the data")