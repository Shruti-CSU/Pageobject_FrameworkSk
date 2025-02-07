
t = 10

while t>1:
    print(t)
    t = t - 1   #the loop will continue till t is not greater than 5 and it will decreased by 1 from t-1 logic

print("end the loop")

#while loop with if condition

t = 10

while t>1:
    if t != 5: #if t does not equal to 5 then print other values
        print(t)
    t = t - 1
print("end loop")

#while loop with break statement

t = 10

while t>1:
    if t == 5:
        break
    print(t)
    t = t - 1
print("end statement")

#while loop with continue statement

t = 10

while t>1:
    if t == 5: #if this condition match continue will skip all the other condition and print end
        t = t-1
        continue
    if t == 3:  
        break
    print(t)
    t = t - 1
print("end")