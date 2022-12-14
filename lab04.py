import random

def play_again() -> bool:
        ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
        playing = input("Do you want to try again? Type Y or Yes, N or No.")
        if playing == 'Y' or play_again == 'YES' :
            return True
        elif playing == 'N' or play_again == 'NO' :
            return False
        else:
            print("An error has occured, must type Y/YES or N/NO. Try again")
            playing = input("Do you want to try again? Type Y or Yes, N or No.")
        return play_again()
print(play_again())
    
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input("How much do you wish to wager?"))
    if wager >= 0 and wager <= bank:
        print(f'You have wagered {wager}, do want to go more?')
        return 1
    else:
        print("An error has occured, value cannot be under zero or over bank amount. Try Again.")
        wager = int(input("How much do you wish to wager?"))
    return get_wager()
print(get_wager())

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reel1 = random.randint(1, 10) 
    reel2 = random.randint(1, 10) 
    reel3 = random.randint(1, 10) 
    return reel1, reel2, reel3
print(get_slot_results(), end=',')

def get_matches(reela, reelb, reelc) -> int: #FIXME
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc and reelb == reelc:
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else:
        return 0
print(get_matches())

def get_bank() -> int:

    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank = int(print('How many chips do you want to play with? Enter value between 0 and 101'))
    if bank <= 0:
        print("Error: Value can't be under 0. Try again")
        bank = int(print('How many chips do you want to play with? Enter value between 0 and 101'))
    elif bank >= 101:
        print("Error: Value can't be under 0. Try again")
        bank = int(print('How many chips do you want to play with? Enter value between 0 and 101'))
    else:
        return bank
print(get_bank())

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 0:
        return wager * -1
    elif matches == 2:
        return wager * 3
    else:
        return wager * 10
print(get_payout())


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
