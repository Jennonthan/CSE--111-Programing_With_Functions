'''
Brennon Laney
06/17/21
go through the list of students and separate the ids and
names and then write a code that can extract the name of
the student by given just the id.
'''

# I will split the csv file and put the names into the 
#students library and the ids into the ids library.
students = []
ids = []

# This will open the students.csv file for the duration
#of the with loop
with open('students.csv', 'rt') as names_ids:

    # I used this so that it will skip the first line 
    #in the csv file
    count = 0

    i_number = input('Please enter an I-Number (xxxxxxxxx): ')
    
    # This will if there are mroe than 9 digis in the i number 
    #it will find any dashes and it will remove them and split 
    #it into 3 strings and then combine those three stings 
    #together without the dashs 
    if len(i_number) > 9: 
        i_number1, i_number2, i_number3 = i_number.split('-')
        i_number_new = (f'{i_number1}{i_number2}{i_number3}')
        print(i_number_new)
    
    else:
        i_number_new = i_number

    # This will go through each item in the names_ids 
    #list which is the students.csv file
    for information in names_ids:
        
        if count != 0:
            # This will separate the ids and names in information and 
            #make libraries for it.
            information = information.split(',')
            
            # This will separate the \n from the student's name
            #and it will append it to students list
            students.append(information[1].strip())


            ids.append(information[0])

        # This adds one to the count so that it doesn't skip the next line in
        #the file
        count += 1

    student_id = False

    # If the id_number_new doesn't have any letters then it will continue with
    #the code
    if i_number_new.isdigit():

        # If the length of the i_number_new is equal to 9 characters it will
        #then got through the list of indexs of both ids and students lists.
        #If one of the ids is equal to the i_number_new it will set 
        #student_id as True and it will print the corresponding student to 
        #the i number
        if len(i_number_new) == 9:
            for i in range(0, (len(ids)-1)):

                # If an item in ids with the index of i is equal to the 
                #i_number_new then it will excicute the code below
                if ids[i] == i_number_new:
                    student = students[i]
                    student_id = True
                    print(student)
        
        # If the length of the i_number_new is less than 9 it will print the 
        #following
        elif len(i_number_new) < 9:
            print('Invalid I-Number: too few digits')
       
       
       
        # If the length of the i_number_new is more than 9 it will print the 
        #following   
        elif len(i_number_new) > 9:
            print('Invalid I-Number: too many digits')

    else:
        print('Invalid I-Number')
    
    # print(students)
    # print(ids)