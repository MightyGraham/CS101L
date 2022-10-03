ID_num = input("Enter 10-digit Library ID: ")



def get_school():
    '''This indicates the school of student based off of the number at index 5 of ID#'''
    school = "None"
    if ID_num[5] == "1": #if index at 5 of the ID number is a 1, the school is SCE
        school = "School of Computing and Engineering SCE"
    elif ID_num[5] == "2": #if index at 5 of the ID number is a 2, the school is School of Law
        school = "School of Law"
    elif ID_num[5] == "3": #if index at 5 of the ID number is a 3, the school is School of College of Arts and Sciences
        school = "College of Arts and sciences"
    else:
        school = "Invaid School" #If number isnt between 1 and 3, display invalid school
    return school
print(f'This card belongs to a student from the {get_school()}')

def get_grade():
    '''This indicates grade of student based off of the number at index 6 of ID#'''
    grade = "None"
    if ID_num[6] == "1": 
        grade = "Freshman"
    elif ID_num[6] == "2":
        grade = "Sophomore"
    elif ID_num[6] == "3":
        grade = "Junior"
    elif ID_num[6] == "4":
        grade = "Senior"
    else:
        grade = "Invalid Grade" #If number isnt between 1 and 4, display invalid grade
    return grade
print(f' This card belongs to a', get_grade())

def character_value(val):
    # character -> unicode integer ord()
    # integer -> unicode character chr()
    char_val = ord(val) - 65
    return char_val
    
    
def get_check_digit(ch):
    val_char = (ch) + 1
    return val_char
    
    
def verify_check_digit():
    while True:
        if len(ID_card) == 10: #Check if ID card is length of 10 characters 
            continue
        elif len(ID_card) != 10:
            print("False, length of ID given must be 10.")
        ID_Card = ID_card.split()#split characters individually
        if ID_Card.isalpha(0) and ID_Card.isalpha(1) and ID_Card.isalpha(1) and ID_Card.isalpha(2) and ID_Card.isalpha(3) and ID_Card.isalpha(4):
            continue #if the first 5 characters are in the alphabet, then continue on
        else:
            print("False, the first five characters are not letters.")
        if ID_Card.isdigit(7) and ID_Card.isdigit(8) and ID_Card.isdigit(9):
            return ID_Card
        else:
            print("False, the first five characters are not letters.")
            

        
        
