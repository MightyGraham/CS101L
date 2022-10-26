def grade_menu():
    print('{:*^30}'.format('Grade Menu'))
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Test')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')


def add_test():
    try:
        t_grade = int(input("Enter grade from 0 - 100: "))
        if (t_grade > 100):
            print("ERROR: number cannot be over 100: ")
            t_grade = int(input('Enter grade from 0 - 100: '))
        elif t_grade < 0:
            print("ERROR: Value cannot be under zero")
            t_grade = int(input('Enter grade from 0 - 100: '))
        else:
            tests.append(t_grade)
            print("Tests:", tests)
            print()
    except ValueError:
        print("ERROR: You must enter a number!")
        t_grade = int(input('Enter grade from 0 - 100: '))


def remove_test():
    grade = int(input("Enter grade to remove: "))
    if grade in tests:
        tests.remove(grade)
        print("Grade has been removed successfully!")
        print("Tests:",tests)
        print()
    else:
        print("Could not find that score to remove")


def clear_test():
    tests.clear()
    print("Tests: ", tests)


def add_program():
    try:
        p_grade = int(input("Enter grade from 0 - 100: "))
        if (p_grade > 100):
            print("ERROR: number cannot be over 100: ")
            p_grade = int(input('Enter grade from 0 - 100: '))
        elif p_grade < 0:
            print("ERROR: Value cannot be under zero")
            p_grade = int(input('Enter grade from 0 - 100: '))
        else:
            programs.append(p_grade)
            print(tests)
    except ValueError:
        print("ERROR: You must enter a number!")



def remove_program():
    grade = int(input("Enter grade to remove: "))
    if grade in tests:
        print("Grade has been removed successfully!")
        print("Programs:",programs)
        print()
    else:
        print("Could not find that score to remove")


def clear_program():
    programs.clear()


def grade_weighted():
    pass
    '''mean = (sum(tests) / len(tests))
    sum = x - mean (squared)
    sqrt(sum / # of elements) '''
#find the mean(average) and the standard deviation
   
#Create empty lists for tests and programs
tests = []
programs = []   
while True: #Keep it as a loop
    grade_menu()
    print()
    selection = input('==> ')
    if selection == '1':#Add to Test
        add_test()
    elif selection == '2':#Remove from Test
        remove_test()
    elif selection == '3':#Clear Test
        clear_test()
    elif selection == '4':#Add Assignments
        add_program()
    elif selection == '5':#Remove Assignments
        remove_program()
    elif selection == '6':#Clear Assignments
        clear_program()
    elif selection == 'D' or selection == 'd':
        print('{:=^75}'.format(''))
        print("Tests: ", end='')
        print(tests)
        print("Programs: ", end='')
        print(programs)
        print()
        continue 
    elif selection == 'Q' or selection == 'q':
        print('Goodbye')
        break
