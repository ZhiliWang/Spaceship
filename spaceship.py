########################################################################
# Zhili Wang                                                           #              
#                                                                      #
# Note:                                                                #
# - Some exceptions are handled in test suite and driver program!      #
# - Satisfying all of Professor Park's "AMAZING points":               #
#   * Graphics function and gameplay funcstions are separated          #
#   * It draws a R-shaped rocket spaceship instead of the one provided #
#       by instruction                                                 #
#   * All gameplay functions (except the graphics function) are within #
#       30 lines of code (excluding empty spaces and comments)         #
########################################################################
import sys, random, turtle, os
# enter/modify your file names/paths here
# wordlist.txt must be existing but scores.txt is not
WORDS_FILE = "wordlist.txt"
SCORES_FILE = "scores.txt"

def get_word(file_name):
    ########################################################################
    # Parameter(s): none                                                   #
    # Return: <class 'str'> "result word", a randomly chosen word          #
    # Purpose: opens a designated file full of vocabs, and randomly choose #
    #           one of them. The word is a cleaned-up string ready to use  #
    # Note: unlike the Database program, we can't give flexibility with    #
    #       file type. It must be strictly a txt file                      #
    ########################################################################
    if file_name.split(".")[-1] != "txt": 
        file_name += ".txt" # file type must strictly be "txt"

    word_file = open(file_name, 'r')
    line = word_file.readlines()
    word_file.close()
    result_word = line[random.randint(0, len(line))].strip('\n')    
    return result_word

def go_to(x, y, direction):
    ########################################################################
    # Parameters:                                                          #
    # <class 'int'> "x", x-coordinate                                      #
    # <class 'int'> "y", y-coordinate                                      #
    # <class 'int'> "direction", as int parameter of turtle's setheading() #          
    # Return: nothing                                                      #
    # Purpose: moving turtle to a designated location with specific        #
    #           coordinates and pointing to a specified angle              #
    ########################################################################
    turtle.penup()
    turtle.goto(x,y)
    turtle.seth(direction) # exactly the same with setheading()
    turtle.pendown()

def graph_lines(word):
    ########################################################################
    # Parameter(s):                                                        #
    # <class 'str'> "word", a word from previous get_word()                #
    # Return: nothing                                                      #
    # Purpose: graphing input lines under letters to show player positions #
    #           of their correctly guessed characters with turtle          #
    ########################################################################
    word_len = len(word)
    go_to(-(word_len // 2 * 30), -180, 0)
    for i in range(word_len):
        turtle.forward(20)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
        
def graph_wrong(word, chars, num_errors):
    ########################################################################
    # Parameter(s):                                                        #
    # <class 'str'> "word", a word passed from driver                      #
    # <class 'str'> chars, a letter that players guess at each round       #
    # <class 'list'> num_errors, a sized-1 list with number of player's    #
    #                 wrong guess                                          #
    # Return: nothing                                                      #
    # Purpose: graphing a player's wrong-guessed letters with turtle       #
    ########################################################################
    go_to(-(len(word)//2*30), -230, 0)
    turtle.penup()
    for i in range(num_errors[0]):
        turtle.forward(20)
    turtle.pendown()
    turtle.write(chars, align='center', font=("Arial", 20, "bold"))
    graph_spaceship(num_errors)
	
def graph_correct(word, char, loop):
    ########################################################################
    # Parameter(s):                                                        #
    # <class 'str'> "word", a word passed from driver                      #
    # <class 'str'> chars, a letter that players guess at each round       #
    # <class 'int'> loop, number of times to run a for loop (positioning)  #
    # Return: nothing                                                      #
    # Purpose: graphing a player's correctly-guessed letters with turtle   #
    ########################################################################
    go_to(-(len(word) // 2 * 30), -180, 0)
    turtle.penup()
    for i in range(loop):
        turtle.forward(30) # was 30 
    turtle.forward(10)
    turtle.pendown()
    turtle.write(char, align='center', font=("Arial", 20, "normal"))

def graph_spaceship(num_err):
    #########################################################################
    # Parameter(s):                                                         #
    # <class 'list'> "num_err", a sized-1 list with number of player's      #
    #                 wrong guess                                           #
    # Return: nothing                                                       #
    # Purpose: graphing 5 stages of a "R"-shaped rocket spaceship depending #
    #           on how many errors the player has so far                    #
    #########################################################################
    ship = turtle.Turtle()
    ship.speed(0)
    # "R-shape" Rocket/Spaceship Part 1
    if num_err[0] == 0:
        ship.begin_fill()
        ship.penup()
        ship.goto(-185,250)
        ship.pendown()
        ship.goto(-200,180)
        ship.goto(-200,-125)
        ship.goto(-170,-125)
        ship.goto(-170,180)
        ship.goto(-185,250)
        ship.end_fill()
    # "R-shape" Rocket/Spaceship Part 2       
    elif num_err[0] == 1:
        ship.begin_fill()
        ship.penup()
        ship.goto(-170,60)
        ship.pendown()
        ship.circle(45, 180)
        ship.goto(-220, 150)
        ship.goto(-255, 160)
        ship.goto(-220, 170)
        ship.goto(-135, 170)
        ship.setheading(360)
        ship.circle(-65, 180)
        ship.goto(-170, 40)
        ship.goto(-170, 60)
        ship.end_fill()
    # "R-shape" Rocket/Spaceship Part 3 
    elif num_err[0] == 2:
        ship.begin_fill()
        ship.penup()
        ship.goto(-135, 60)
        ship.pendown()
        ship.setheading(360)
        ship.circle(-75, 90)
        ship.goto(-60, -125)
        ship.goto(-90, -125)
        ship.goto(-90, 0)
        ship.setheading(90)
        ship.circle(40, 90)
        ship.goto(-135, 60)
        ship.end_fill()
    # Left Flame (Part 4)
    elif num_err[0] == 3:
        ship.begin_fill()
        ship.fillcolor("red")
        ship.penup()
        ship.goto(-200, -125)
        ship.pendown()
        ship.goto(-195, -135)
        ship.goto(-190, -125)
        ship.goto(-185, -145)
        ship.goto(-180, -125)
        ship.goto(-175, -135)
        ship.goto(-170, -125)
        ship.goto(-200, -125)
        ship.end_fill()
    # Right Flame (Part 5)
    elif num_err[0] == 4:
        ship.begin_fill()
        ship.fillcolor("red")
        ship.penup()
        ship.goto(-90,-125)
        ship.pendown()
        ship.goto(-85, -135)
        ship.goto(-80, -125)
        ship.goto(-75, -145)
        ship.goto(-70, -125)
        ship.goto(-65, -135)
        ship.goto(-60, -125)
        ship.goto(-90, -125)
        ship.end_fill()
    num_err[0] += 1
    
def play(word, output, num_errors):
    ########################################################################
    # Parameter(s):                                                        #
    # <class 'str'> "word", a word passed from driver                      #
    # <class 'str'> chars, storing a string                                #
    # <class 'list'> num_errors, a sized-1 list with number of player's    #
    #                 wrong guess                                          #
    # Return:                                                              #
    # <class 'str'> answer                                                 #
    # OR                                                                   #
    # <class 'str'> output, either return the correct answer or a mixture  #
    #                       of correctly guessed letters and unknown ones  #
    # Purpose: printing a string to present what and where the correctly   #
    #          guessed letters are, on shell, not turtle                   #
    ########################################################################
    chars = ''
    # in case if player inputs something longer than size-1
    while len(chars) != 1:
        try:
            chars = input("Please guess a letter: ").lower()
        except ValueError as e:
            print("You might input a character that is not single-digit:"
                  , e.value)
    answer = ''
    try:
        if chars in word:
            for i in range(len(word)):
                if chars == word[i]:
                    answer += chars
                    graph_correct(word, chars, i)
                else:
                    answer += output[i]
            return answer
        else:
            graph_wrong(word, chars, num_errors)
            return output
    except IndexError as e:
        print("Indexes don't match: ", e)
        
def record_score(num_wins):
    ########################################################################
    # Parameter(s):                                                        #
    # <class 'int'> "num_wins", player's current wins/scores from driver   #
    # Return: nothing                                                      #
    # Purpose: graphing input lines under letters to show player positions #
    #           of their correctly guessed characters with turtle          #
    ########################################################################
    player = input("Please Enter Your Name: ")
    score_top_line = 0

    # if file exists / not first time playing
    # split first line of file by space and get current high score
    if os.path.isfile(SCORES_FILE):
        try:
            scorecard = open(SCORES_FILE, 'r')
            high_file = scorecard.readline().split()
            score_top_line = int(high_file[-1])
            scorecard.close()
        except OSError as e:
            print("Unable to open file: It doesn't exist OR no access"
                   " permission.")
        except Exception as err:
            print("Unexpected Error about the file: {0}".format(err))
        # if player's current score is same or less than the highest
        if num_wins <= score_top_line:       
            scorecard = open(SCORES_FILE, 'a')
            scorecard.write(player + " " + str(num_wins) + "\n")
        # if player's current score is the new highest, record it at top
        else:
            try:
                scorecard = open(SCORES_FILE, 'r+')
                contents = scorecard.read()
                scorecard.seek(0, 0)
                scorecard.write(player + " " + str(num_wins) + "\n" + contents)
                scorecard.close()
            except OSError as e:
                print("Unable to open file: It doesn't exist OR no access"
                   " permission.")
            except Exception as err:
                print("Unexpected Error about 'spaceship.py': {0}".format(err))
        print("{0}'s score of {1} is saved.".format(player, num_wins))

        # if file doesn't exist
    # first time playing/recording a score,
    # whatever win is, it's the new-highest
    else:
        scorecard = open(SCORES_FILE, 'a')
        scorecard.write(player + " " + str(num_wins) + "\n")
        print(SCORES_FILE + " does not exist but we created a new one:\n"
              "{0}'s score of {1} is saved.".format(player, num_wins))

