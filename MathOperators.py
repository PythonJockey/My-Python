# Asking user for two numbers of his/her choice
import pyinputplus as pyip
# pyip for input validation

num1 = int(pyip.inputNum('Please enter the first number: '))
num2 = int(pyip.inputNum('Please enter the second number: '))
# using inputNum to avoid errors with improper inputs

numSum = num1 + num2

if num1 >= num2:
    numDifference = num1 - num2
else:
    numDifference = num2 - num1

numProduct = num1 * num2

if num1==0 or num2==0:
    print('Error: Division by Zero')
else:
    numDivision = num1/num2

# Displaying results
print ('The sum of the two numbers is: ', numSum)
print ('The substraction of the two numbers gives: ', numDifference)
print ('The multiplication of the two numbers gives: ', numProduct)
print ('The division of the two numbers gives: ', numDivision)
