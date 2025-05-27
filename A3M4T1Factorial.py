import pyinputplus as pyip, math
while True: #Loop to ensure a positive integer
    myNum = int(pyip.inputInt('Please enter an integer : ')) #Ensure an integer as input
    if myNum > 0: # Valid input
        break
    else:
        print ('Enter a POSITIVE INTEGER only!')
print (f'Your number is {myNum}')

# Factorial by using math module
myFact01 = math.factorial (myNum)
print (f'Factorial using math module factorial function : {myFact01}')

# Factorial by using a function
def findFactorial(x):
    if x <= 1:
        return 1
    else:
        return x * findFactorial (x-1)

print (f'Factorial using Function with Recursion : {findFactorial (myNum)}')

# Factorial using FOR loop
if myNum <= 1:
    print ('Factorial by FOR loop : 1')
else:
    myFact03 = 1
    for num in range (myNum, 1, -1):
        myFact03 *=num
    print (f'Factorial by FOR loop : {myFact03}')
