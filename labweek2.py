print("**** Welcome to the LAB grade calculator! ****")
print()
name = input("Who are we calculating grades for? ==> ") #assign variables to name and each of the grades
print(name)
print()
grade_labs = float(input("Enter the Labs grade ==> ")) 
if grade_labs>100: #if/elif/else is recommened here. Grades can't be negative and most grades don't go over 100
    print('Entered value for Labs cannot be over 100, grade has been changed to 100')
    grade_labs = 100#value for grade_labs needs to be changed to 100
elif grade_labs<0:
    print('Entered value for labs cannot be a negative number, grade has been changed to 0')
    grade_labs = 0#value for grade_labs needs to be changed to 0
else:
    print(grade_labs) #Everything should run smooth here and continue to the next questions
print() #for spacing
grade_EXAM = float(input("Enter the EXAMS grade ==> "))
if grade_EXAM>100: #rinse and repeat for EXAM and Attendance
    print('Entered value for EXAM cannot be over 100, grade has been changed to 100')
    grade_EXAM = 100
elif grade_EXAM <0:
    print('Entered value for EXAM cannot be a negative number, grade has been changed to 0')
    grade_EXAM = 0
else:
    print(grade_EXAM)
print()
attendance = float(input("Enter the Attendance grade ==> "))
if attendance>100: 
    print('Entered value for Attendance cannot be over 100, grade has been changed to 100')
    attendance = 100
elif attendance<0:
    print('Entered value for Attendance cannot be a negative number, grade has been changed to 0')
    attendance = 0
else:
    print(attendance)
print()
#Codes above all works! now the tricky part is to calculate those grades...
#I know that I have to use the if/elif/else statements for this part
#labs = .7, exams = .2, attendance = .1 
weighted_grade = grade_labs * .7 + grade_EXAM * .2 + attendance * .1
if weighted_grade >= 90: #don't forget to add colons when using if-else statements
    print(f'The weighted grade for {name} is {weighted_grade}')
    print(f'{name} has the letter grade of A')
elif weighted_grade < 90: #multiple elif statements for each of the letter grades
    print(f'The weighted grade for {name} is {weighted_grade}')
    print(f'{name} has the letter grade of B')
elif weighted_grade < 80:
    print(f'The weighted grade for {name} is {weighted_grade}')
    print(f'{name} has the letter grade of C')
elif weighted_grade < 70:
    print(f'The weighted grade for {name} is {weighted_grade}')
    print(f'{name} has the letter grade of D')
else:
    print(f'The weighted grade for {name} is {weighted_grade}')
    print(f'{name} has the letter grade of F')



print("**** Thank you for using the LAB grade calculator ****")



