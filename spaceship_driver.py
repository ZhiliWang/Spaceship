########################################################################
# Zhili Wang                                                           #
# CS5001                                                               #
# Homework 5 Part 2: Spaceship                                         #                 
#                                                                      #
# Note: Driver of the Spaceship game program                           #
#       * CHEAT MODE is on by default in your convenience of testing,  #
#         switch it off if you want                                    #
########################################################################
from spaceship import *
# enter/modify your file names/paths here
# wordlist.txt must be existing but scores.txt is not
WORDS_FILE = "wordlist.txt"
SCORES_FILE = "scores.txt"
GREETING = "The gameplaying rules are the same with Hangman.\n" \
+ "Please be patient while inputting each guess, otherwise the\n" \
+ "program won't read a player's guess and generate errors!\n"
def print_greeting():
########################################################################
# Parameter(s):                                                        #
# <class 'str'> "word", a word from previous get_word()                #
# <class 'str'> chars, a letter that players guess at each round       #
# <class 'int'> loop, number of times to run a for loop (positioning)  #
# Return: nothing                                                      #
# Purpose: graphing a player's correctly-guessed letters with turtle   #
########################################################################
    print("The gameplaying rules are the same with Hangman.\n"
      + "Please be patient while inputting each guess, otherwise the\n"
      + "program won't read a player's guess and generate errors!")

def cheat_mode(on_off, word):
########################################################################
# Parameter(s):                                                        #
# <class 'bool'> on_off: status of the CHEAT MODE on/off               #
# <class 'str'> word: a word passed from driver's main                 #
# Return: nothing                                                      #
# Purpose: showing the player/tester/grader the solution of the game   #
########################################################################
    if on_off:
        print("***CHEAT MODE IS ON (for program testing purposes)*** \n"
            + "--> [CHEAT MODE] The word is *{0}*".format(word))
    else:
        print("You turned off CHEAT MODE? That's the spirit, let's go!")

def print_greeting():
########################################################################
# Parameter(s):                                                        #
# <class 'str'> "word", a word from previous get_word()                #
# <class 'str'> chars, a letter that players guess at each round       #
# <class 'int'> loop, number of times to run a for loop (positioning)  #
# Return: nothing                                                      #
# Purpose: graphing a player's correctly-guessed letters with turtle   #
########################################################################
    print("The gameplaying rules are the same with Hangman.\n"
      + "Please be patient while inputting each guess, otherwise the\n"
      + "program won't read a player's guess and generate errors!")

def main():
########################################################################
# Parameter(s): nothing                                                #
# Return: nothing                                                      #
# Purpose: Driver that runs the game from a player's perspective. Be   #
#          aware the "CHEAT MODE" that tells the answer is turned ON   #
#          by default in your convenience for grading.                 #
########################################################################
    print(GREETING)
    user_yn_again = 'y'
    win = 0
    word = ''
    try:
        while user_yn_again == 'y':
            turtle.reset()
            num_errors = [0]
            word = get_word(WORDS_FILE)
            word_used = word.lower()
            cheat_mode(True, word)
            graph_lines(word)
            unknown = ''
            for i in range(len(word)):
                unknown += '_'
                
            while unknown != word_used and num_errors[0] <=4:
                print(unknown)
                unknown = play(word_used, unknown, num_errors)
            
            if num_errors[0] > 4:
                print('You lose, sorry!')
                print("The word was " + word)
                print("You have won {} games so far.".format(win))
                user_yn_again = input("Play again? Enter Y/N: ").lower()
            else:
                print('You win!')
                win += 1
                print("You have won {} games so far.".format(win))
                user_yn_again = input("Play again? Enter Y/N: ").lower()
    except Exception as err1:
        print("Unexpected Error about the driver before recording the score:"
              , err1)

    try:
        record_score(win)
    except FileNotFoundError as err2:
        print("FileNotFoundError: {0}".format(err2))
    except Exception as err3:
        print("Unexpected Error about the driver: {0}".format(err3))
                
main()
