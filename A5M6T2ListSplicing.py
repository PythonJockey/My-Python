# Create a list from 1 to 10
originalList = []
for i in range (1,11):
    originalList.append(i)
print (f'Original List : {originalList}')

extractedList = originalList [0:5]
print (f'Extracted first five elements : {extractedList}')

extractedList.reverse()
print (f'Reversing extracted elements : {extractedList}')
