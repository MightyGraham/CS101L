#First, I'll create functions for each of the options
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
        t_grade = int(input("Enter grade from 0 - 100: ")
        if t_grade > '100' :
            print("ERROR: Value cannot be over 100")
            t_grade = int(input('Enter grade from 0 - 100: ')
        elif t_grade < '0' :
            print("ERROR: Value cannot be under zero")
            t_grade = int(input('Enter grade from 0 - 100: ')
        else:
            
#Create empty lists for tests and programs
tests = []
programs = []   
while True: #Keep it as a loop
    grade_menu()
    print()
    selection = input('==> ')
    if selection == '1':#Add Test
        add_test()
    elif selection == '2':#Remove Test
        pass
    elif selection == '3':#Clear Test
        pass
    elif selection == '4':#Add Assignments
        pass
    elif selection == '5':#Remove Assignments
        pass
    elif selection == '6':#Clear Assignments
        pass
    elif selection == 'D' or selection == 'd':
        print('{:=^75}'.format(''))
        print("Tests: ", end='')
        print(tests)
        print("Print: ", end='')
        print(programs)
        print()
        continue 
    elif selection == 'Q' or selection == 'q':
        print('Goodbye')
        break
    
    
