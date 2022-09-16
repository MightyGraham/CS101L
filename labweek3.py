#1) Start
#2) Enter the name of the game (Flarsheim Guesser)
#3) create a while loop for whole game 
#4) Let user input a number between 1 and 100, then assign it
#5) Use modulus (%) to find the remainder of user's number when divided by 3
# Since the remainder when divided by 3 can only be 0, 1, and 2, we will need an if loop.
# If remainder is greater or equal to 3, then print a message saying "value must be under 3"
# If the remainder is less than 0, then print a message saying "value must be over 0"
#6) Use modulus (%) to find the remainder user's number when divided by 5 and 7
#7)Since the remainders when divided by 5 and 7 can be different, we do not need an If loop
#8)Show the number the user inputed
#9)If user wants

  
game = True 
print("Welcome to the Flarsheim Guesser!")
print()
while game:

    user_num = int(input("Think of a number between 1 and 100:"))
    print(user_num)
    remainder_3 = int(input("What is the remainder when your number is divided by 3 ?"))
    if remainder_3 > 3:
        print("Value must be under 3.")
        int(input("What is the remainder when your number is divided by 3 ?"))
    elif remainder_3 < 0:
        print("Value cannot be a negative.")
        int(input("What is the remainder when your number is divided by 3 ?"))
    else:
        print()
    int(input("What is the remainder when your number is divided by 5 ?"))
    print()
    int(input("What is the remainder when your number is divided by 7 ?"))
    print()
    print(f'I bet your number was {user_num}')
    print("How amazing is that?")
    print()
    answer = input("Wanna give it another go? Type Y to continue, otherwise type N. ")
    if answer == "Y" or answer == "y":
        continue  #figure out how to loop game
    elif answer == "N" or answer == "n":
        print("Thank you for playing, Goodbye")
        game = False
    else:
        print("Wanna give it another go? Type Y to continue, otherwise type N. ")
    

    
    
   
   
    
    
    


