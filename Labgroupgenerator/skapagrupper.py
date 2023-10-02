################################################################
# Labbgruppgenerator
#
# Detta program tar en lista av studenter kopierad från omniway
# och genererar slumpmässigt labbrupper två och två baserat
# på denna lista.
# Programmet är skapat av KYH23-gruppen.
#
# input: programmet läser in en fil av namnet studerande.txt
# output: en fil där varje rad är en ny labbgrupp.
#
# Filer:
# skapagrupper.py
################################################################

import random

# Open the file studerande.txt as read only.
with open("studerande.txt", "r") as filehandler:
    i = 0;
    students = []
    
    # Read every line and store it in a list students.
    while True:
        line = filehandler.readline()					# read the line.
        
        if not line:									# if there are no more lines, cancel loop.
            break
        
        # the file studerande.txt is filled with random crap from the copy paste.
        # we want to sort everything that is not a student name.
        if i%5 == 0:								# every fifth line is a new student.
            current_student = line
            current_student = current_student[:-23]	# remove the last 23 characters (this is the course)
            students.append(current_student)		# add to the list of students.
        i = i+1
    
    
    # Lets randomly generate lab grops.
    groups = []
    i = 1
    
    # while we have students left in the list, select two students at random.
    while len(students) > 0:
        rand_student1 = random.randint(0, len(students)-1)			# randomly select student 1.
        student1 = students.pop(rand_student1)						# take out and remove (pop) student from list.
        
        # if there is an uneven number of students in the class, there will be a group with only one student left
        # the following code snippet is to handle that case.
        if len(students) > 0:		# we have another student to chose, so continue as normal.
            rand_student2 = random.randint(0, len(students)-1)
            student2 = students.pop(rand_student2)
        else:						# we now dont have any new students to chose, so we will have to do a special case for this.
            student2 = ""			# student2 will be empty if there are no more students to chose from the list.

        
        if student2 != "":		# if student2 has something in it, we know we can create a full labgroup from these two students.
            groups.append("group " + str(i) + ": " + student1 + ", " + student2);
            i = i+1
        else:					# If student 2 is empty, place student one in the last complete group. And there will be one group of three.
            groups[-1] = groups[-1] + ", " + student1

    # Lets print out the grups for show.
    for group in groups:
        print(group)

    # save the groups to a new file.
    with open("student_groups.txt", mode="w") as file:
        for group in groups:
            file.write(group + "\n")