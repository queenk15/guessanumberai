#Guess-A-Number AI
#
#Kyerra Jones
#September 1, 2016


def start_screen():
        print(" _________  __        _            __          ___       ___        _        ____  _____                       __                      ")
        print("|  _   _  |[  |      (_)          [  |  _    .'   `.   .' ..]      / \      |_   \|_   _|                     [  |                     ") 
        print("|_/ | | \_| | |--.   __   _ .--.   | | / ]  /  .-.  \ _| |_       / _ \       |   \ | |  __   _   _ .--..--.   | |.--.   .---.  _ .--. ")
        print("    | |     | .-. | [  | [ `.-. |  | '' <   | |   | |'-| |-'     /  _  \      | |\ \| | [  | | | [ `.-. .-. |  | '/'`\ \/ /__\\[ `/'`\]") 
        print("   _| |_    | | | |  | |  | | | |  | |`\ \  \  `-'  /  | |     _/ /   \ \_   _| |_\   |_ | \_/ |, | | | | | |  |  \__/ || \__., | |    ")
        print("  |_____|  [___]|__][___][___||__][__|  \_]  `.___.'  [___]   |____| |____| |_____|\____|'.__.'_/[___||__||__][__;.__.'  '.__.'[___]   ")

def play():

        #low = 1
        #high = 100
        #guess = (low + high) // 2
        tries = 0 

        print("What is your name?")
        name = input()
        print(name + " please enter the highest number I can guess")
        high = input()
        print(name + " please enter the lowest number I can guess")
        low = input()
        if low > high:
                print ("You entered a number higher than the high number. Please enter a lower number.")
                low = input()

        guess = (int(low) + int(high)) // 2
        print(name + " please think of a number between " + str(low) + " and " + str(high) + ". I will try to guess it press enter when you are ready.")
        input()

        print(name + " is your number " + str(guess) + " if not is it lower or higher or did I guess your number?")
        a = input()


        while a !='yes' or a != 'y':
                 

                if a =='lower' or a == 'l':
                        high = guess - 1
                        guess = (int(low) + int(high)) // 2
                        print(name + " is your number " + str(guess) + " if not is it lower or higher or did I guess your number?")
                        a = input()
                        tries += 1
                                
                if a =='higher' or a == 'h':
                        low = guess + 1
                        guess = (int(low) + int(high)) // 2
                        print(name + " is your number " + str(guess) + " if not is it lower or higher or did I guess your number?")
                        a = input()
                        tries += 1
                        
                if a == 'n' or a == 'no':
                        print(name + " please type yes, lower, or higher to continue.")
                        a = input()
                       
                if a =='yes' or a == 'y':
                        print(name + " I guessed your number!!!")
                        print(" I tried to guess your number " + str(tries) + " times.")
                        print("GAME OVER")
                        break
                else:
                        print(name + " I don't understand")
                        a = input()
                        break
def credit_screen():
        time = 0
        print("Author : Kyerra Jones")

        print("Inspiration: A good grade")

        print("Date Completed: November 13, 2016") 
        
#def play_again():
#     while True:
 #        answer = input("Would you like to play again? ")
  #              if answer == 'no' or answer == 'n':
   #                     return False
    #            elif answer == 'yes':
     #                   return True

                #print("What?!!! Just say yes or no.")

#game begins
start_screen()
play()
credit_screen()
               

                        
        

                

