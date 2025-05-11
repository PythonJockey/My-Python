# Check whether a number is odd or even
# Step 1 - Ask for input and convert it to an integer
myNum = int(input ('Please enter any number: '))
# Step 2 - Check whether the number is divisible by 2
if myNum%2 == 0:
    print (str(myNum) + ' is an Even number.')
else:
    print(str(myNum) + ' is an Odd number.')