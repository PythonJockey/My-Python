# Ask for input for new text
myTextWrite = input("Please enter text to add to 'tutedudeOutput.txt' : ")

#create new file tutedudeOutput.txt
with open ('tutedudeOutput.txt','w') as myFile:
    myFile.write (myTextWrite)
    myFile.write ('\n') # add newline character
    print ("Data successfully written to 'tutedudeOutput.txt'.")

# Ask for input to add to file
myTextAppend = input ("Please enter additional text to add to 'output.txt' : ")

# Append mode
with open ('tutedudeOutput.txt', 'a') as myFile:
    myFile.write (myTextAppend)
    myFile.write ('\n')
    print('Data successfully appended')

# Open file contents
with open ('tutedudeOutput.txt', 'r') as myFile:
    print (myFile.read())

