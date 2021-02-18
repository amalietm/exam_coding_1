from random_words import RandomWords # provides random words
import time
import colorama 
from colorama import Fore, Back, Style

# printing messages
print()
print("Welcome to Random where you guess words for points!")
time.sleep(1)
print("You will be switching roles for each round.")
time.sleep(1)
print("To start, Player1 will be guesser and Player2 will be describer.")
time.sleep(1)
print("Press Enter to continue.")
   
while True:
    score_Player1 = 0
    score_Player2 = 0
    rw = RandomWords()
    colorama.init(autoreset = True)
    Player1 = "Player1"
    Player2 = "Player2"
    Player1 = "g"
    Player2 = "d"
    cancel_game = "q"
    word1 = rw.random_word()
    word2 = rw.random_word()
    describer = "Player2"
    guesser = "Player1"
    tries_player1 = 3
    tries_player2 = 3
    guess = input().lower()
        
    if word1:
        # directions
        print(Fore.RED + guesser + ": guesser")
        time.sleep(1)
        print(Fore.BLUE + describer + ": describer")
        time.sleep(1)
        print(Fore.RED + "If you wish to guess, press g")
        time.sleep(1)
        print(Fore.BLUE + "If you are to describe, press d")
        time.sleep(1)
        print("If you at any time want to cancel the game, press q")
        time.sleep(1)

        print()
        print (Fore.RED + "Guesser will start with 3 tries")
        time.sleep(1)
        print()
        print("This is the Random Word. To see, hold cursor over word as if to highlight.")
        time.sleep(1)
        print(Fore.BLUE + "Make sure the guesser doesn´t see the word!")
        time.sleep(1)
        print("Random Word: " + Back.BLACK + word1, end = "")
        if word1[-1] == "s":
            print(Back.BLACK + " --> Remember to mention the word being plural!")
        time.sleep(1)

        # game loop word1
        while guess != word1 or description != word1:
            choose_player = input(Fore.BLACK + "\nType which player to play: ")
            if choose_player == "g":
                guess = input(Fore.RED + "Guesser: ").lower()
                
                if guess == word1:
                    print(Fore.RED + "Correct!")
                    time.sleep(1)
                    break
                elif tries_player1 == 1:
                    print(Fore.RED + "You have no more tries...")
                    time.sleep(1)
                    print("The word was: " + word1)
                    time.sleep(1)
                    print()
                    break
                elif guess != word1:
                    tries_player1 -= 1
                    print(Fore.RED + "That´s not right, but try again!")
                    time.sleep(1)
                    print()
                    print (Fore.RED +"Tries: " + str(tries_player1))
                    time.sleep(1)
                    continue
                
                    
            elif choose_player == "d":
                description = input(Fore.BLUE + "Describer: ").lower()
                if description == word1:
                    print(Fore.BLUE + "You can´t use the word itself.. Switch players!")
                    time.sleep(1)
                    break

            elif choose_player == "q":
                print("See you next time!")
                quit()
                

            else:
                print("That is not a valid input. Choose g or d.")
                time.sleep(1)
                
        if guess == word1:
            print(Fore.RED + "You guessed right!")
            time.sleep(1)
            print() 
            score_Player1 += 1 

        # calculting score
        print("Player1: " + str(score_Player1) + " " + "Player2: " + str(score_Player2))
        time.sleep(1)
        print()
        
        # change of player    
        if guesser == "Player1": 
            guesser = "Player2"
            describer = "Player1"
        else:
            guesser = "Player1"
            describer = "Player2"
            
    
    if word2:
        # directions 
        print()
        print("NEW GAME")
        time.sleep(1)
        print()
        print(Fore.BLUE + guesser + ": guesser")
        time.sleep(1)
        print(Fore.RED + describer + ": describer")
        time.sleep(1)
        print(Fore.BLUE + "If you wish to guess, press g")
        time.sleep(1)
        print(Fore.RED + "If you are to describe, press d")
        time.sleep(1)

        
        print()
        print (Fore.BLUE + "Guesser will start with 3 tries")
        time.sleep(1)
        print()
        print("This is the Random Word. To see, hold cursor over word as if to highlight.")
        time.sleep(1)
        print(Fore.BLUE + "Make sure the guesser doesn´t see the word!")
        time.sleep(1)
        print("Random Word: " + Back.BLACK + word2, end = "")
        if word2[-1] == "s":
            print(Back.BLACK + " --> Remember to mention the word being plural!")
        time.sleep(1)

        # game loop word 2
        while guess != word2 or description != word2:
            choose_player = input(Fore.BLACK + "\nType which player to play: ")
            if choose_player == "g":
                guess = input(Fore.BLUE + "Guesser: ").lower()
                
                if guess == word2:
                    print(Fore.BLUE + "Correct!")
                    time.sleep(1)
                    break
                elif tries_player2 == 1:
                    print(Fore.BLUE + "You have no more tries...")
                    time.sleep(1)
                    print("The word was: " + word2)
                    time.sleep(1)
                    print()
                    break
                elif guess != word2:
                    tries_player2 -= 1
                    print(Fore.BLUE + "That´s not right, but try again!")
                    time.sleep(1)
                    print()
                    print (Fore.BLUE + "Tries: " + str(tries_player2))
                    time.sleep(1)
                    continue
                
                    
            elif choose_player == "d":
                description = input(Fore.RED + "Describer: ").lower()
                if description == word2:
                    print(Fore.RED + "You can´t use the word itself.. Switch players!")
                    time.sleep(1)
                    break

            else:
                print("That is not a valid input. Choose g or d.")
                time.sleep(1)
                
        if guess == word2:
            print(Fore.BLUE + "You guessed right!")
            time.sleep(1)
            print() 
            score_Player2 += 1 

        # calculting score
        print("Player1: " + str(score_Player1) + " " + "Player2: " + str(score_Player2))
        time.sleep(1)

        # calculating who won
        if score_Player1 > score_Player2: 
            print(Fore.RED + "Player1 won!")
        elif score_Player1 == score_Player2:
            print("It was a tie!")
        else:
            print(Fore.BLUE + "Player2 won!")

    # restarting game 
    while True: 
        print()
        time.sleep(1)
        answer = str(input("Do you still want to play? Press y if yes or n if no."))
        if answer == "y" or "n":
            break
        print("invalid input.")
    if answer == 'y':
        print()
        time.sleep(1)
        print("NEW GAME")
        time.sleep(1)
        print("Press Enter when ready.")
        continue
    else:
        time.sleep(1)
        print("See you next time!")
        break
                    
             
        

        
