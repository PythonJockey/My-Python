# Creating a file tutedudeSample.txt
with open ('tutedudeSample.txt', 'w') as myFile:
    myFile.write ('First Line - This is sample text file.\n')
    myFile.write ('Second Line - It contains multiple lines.\n')

try:
    with open ('tutedudeSample.txt', 'r') as fileToRead:
        line1 = fileToRead.readline()
        line2 = fileToRead.readline()
        print (f'Line 1: {line1.strip()}')
        print (f'Line 2: {line2.strip()}')
except FileNotFoundError:
    print ("The file 'tutedudeSample.txt' was not found!")
