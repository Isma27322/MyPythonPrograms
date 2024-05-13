import random
import time

def banner():
    print("The game of NIM program.\n")
    print("This game will give you a number of dice from 10 to 100,")
    print("and will see who goes first. Whoever goes first is allowed")
    print("to remove from 1 to half the number of dice. Then the game")
    print("will continue until there are no dice left.\n\n")

def main():
    playAgain = "Yes" # Stores if the user wants to play again
    
    while playAgain.lower() == "yes":
        banner()
        
        firstPlayer = random.randint(1, 2) # Chooses who will go first
        userChoiceFirst = 0 # Stores the user choice for coin flip as an integer
        
        print("We will choose who will go first by flipping a coin.")
        userFirstPlayer = input("Do you want to be heads or tails? ")
        
        while True:
            try:
                if userFirstPlayer.lower() == "heads":
                    userChoiceFirst = 1
                    break
                elif userFirstPlayer.lower() == "tails":
                    userChoiceFirst = 2
                    break
                else:
                    print("That is not a valid input.\n")
                    userFirstPlayer = input("Please try again. Do you want to be heads or tails? ")
            except:
                print("That is not a valid input.\n")
                userFirstPlayer = input("Please try again. Do you want to be heads or tails? ")
        
        print("\n")
        
        if userChoiceFirst == firstPlayer:
            print("You will go first!")
            comTurn = False
        else:
            print("The computer will go first!")
            comTurn = True
        
        numOfDice = random.randint(10, 100)
        
        while numOfDice > 0:
            print("There are", numOfDice, "dice left.")
            
            if comTurn:
                comWait = random.randint(500, 20000)
                print("It is the computer's turn.")
                print("/*************************************\\")
                print("      Processing, please wait")
                print("\\*************************************/")
                
                time.sleep(comWait / 1000)
                
                if numOfDice == 1:
                    comChoiceForNumOfDice = 1
                else:
                    comChoiceForNumOfDice = random.randint(1, numOfDice // 2)
                
                print("The computer is taking", comChoiceForNumOfDice, "dice")
                
                numOfDice -= comChoiceForNumOfDice
                comTurn = False
                
                print("\n")
            else:
                print("It is your turn.")
                print("How many dice do you want to take?")
                
                if numOfDice == 1:
                    print("You can take 1 die.")
                else:
                    print("You can take a minimum of 1.")
                    print("And a maximum of", numOfDice // 2, "dice.")
                    
                while True:
                    try:
                        userChoiceForNumOfDice = int(input())
                        
                        if 1 <= userChoiceForNumOfDice <= numOfDice // 2:
                            break
                        else:
                            print("That is larger than the number of dice you are allowed to take.")
                            print("How many dice do you want to take?")
                            print("You can take a minimum of 1.")
                            print("And a maximum of", numOfDice // 2, "dice.")
                    except:
                        print("That is not a valid input.\n")
                        print("How many dice do you want to take?")
                        print("You can take a minimum of 1.")
                        print("And a maximum of", numOfDice // 2, "dice.")
                
                print("\n")
                numOfDice -= userChoiceForNumOfDice
                comTurn = True
        
        if comTurn:
            print("Sorry, you have lost the game.\n")
        else:
            print("Congratulations, you have won!\n")
        
        playAgain = input("Would you like to play again? (Yes/No): ")
        print("\n\n")

# Start the game
main()
