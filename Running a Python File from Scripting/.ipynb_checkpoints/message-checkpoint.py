delimitador = ','

names = input('Enter names separated by commas: ').title() # get and process input for a list of names
list_names = names.split(delimitador)
print(list_names)

assignments =  input('Enter assignment separated by commas: ') # get and process input for a list of the number of assignments
list_assignments = assignments.split(delimitador)
print(list_assignments)

grades = input('Enter grades separated by commas: ') # get and process input for a list of grades
list_grades = grades.split(delimitador)
print(list_grades)

# message string to be used for each student
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# HINT: use .format() with this string in your for loop
# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for i in range(len(list_names)):
     print(message.format(list_names[i], list_assignments[i], list_grades[i],
                          int(list_grades[i]) + int(list_assignments[i])*2))
