import random
import sys
import time

def throw_dice(again):
    while again != False:
        print("Throwing the dice...")
        time.sleep(3)
        print("......")
        dice_roller = random.randint(1,6)
        print(f"You got number {dice_roller} \n")
        
        if dice_roller == 6:
            print("Congratz! You got a number 6!")
            print("You got one chance to roll again!")
            print("Reroll.....")
        
        print(f"You got number {dice_roller}")

        play_again = input("You want to play again (Y/n) : ")
        print("\n")
        
        if str.upper(play_again) == 'Y':
            again = True
        else:
            again = False
            break

if __name__ == '__main__':
    play = False 
    user_input = input("You want to play (Y/n) : ")
    
    if str.upper(user_input) == 'Y':
        play = True
        throw_dice(play)
    else:
        sys.exit()
