# Dictionary of students
students = {
    'Alice':85,
    'Bob':79,
    'Carol':89,
    'Tom':94,
    'Dick':88,
    'Harry':92,
    'Jack':72,
    'Jane':73
}

# Ask for user query input
myStudent = input ('Please enter name of the student: ').strip()

# If student not in the records
if myStudent not in students.keys():
    print (f'{myStudent} not found in the records!')
    # Choose to Update Record?
    while True:
        myResponse = input(f"Do you want to enter {myStudent}'s name to record? (y/n): ")
        # Chose to update record
        if myResponse.lower() == 'yes' or myResponse.lower() == 'y':
            myStudentMarks = input(f'Please enter marks (out of 100) of {myStudent}: ')
            # Data entry validation - should be a number <= 100
            try:
                if int(myStudentMarks) <= 100: # Valid data
                    students[myStudent] = int(myStudentMarks)
                    print('Update attempt successful')
                    break
                else:
                    print ('Marks should be less than or equal to 100!')
            except ValueError: # Marks entry inappropriate
                print ('Enter valid number!')
        else:
            # Chose not to update records
            break
# Student present in records
else:
    print (f"{myStudent}'s marks : " + str(students.get(myStudent,0)))

# Rank-wise sorted list
myResponse2 = input ('Would you like to see rank-wise list of students on record? (y/n) : ')
if myResponse2.lower()== 'y' or myResponse2.lower()== 'yes':
    sortByRank = sorted(students.items(), key=lambda item: item[1], reverse=True)
    print (sortByRank)


