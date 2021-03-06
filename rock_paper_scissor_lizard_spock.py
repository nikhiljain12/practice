# To play the game, visit http://www.codeskulptor.org/#user29_ldOvao7Hqb_0.py

# The rules of rock-paper-scissors-lizard-Spock are:
# Scissors cut paper
# Paper covers rock
# Rock crushes lizard
# Lizard poisons Spock
# Spock smashes scissors
# Scissors decapitate lizard
# Lizard eats paper
# Paper disproves Spock
# Spock vaporizes rock
# Rock crushes scissors

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions
def name_to_number(name):
    if (name == "rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else:
        print 'Invalid entry'

def number_to_name(number):
    if (number == 0):
        return 'rock'
    elif (number == 1):
        return 'Spock'
    elif (number == 2):
        return 'paper'
    elif (number == 3):
        return 'lizard'
    elif (number == 4):
        return 'scissors'
    else:
        print 'Invalid entry'

def rpsls(player_choice): 
    print '\n'        
    print 'Player chooses ' + player_choice
    player_number = name_to_number(player_choice)
    computer_number = random.randrange(0,5)
    print 'Computer chooses ' + number_to_name(computer_number)            
    diff = (computer_number - player_number) % 5            
    if (diff == 1 or diff == 2):
        print 'Computer wins!'
    elif (diff == 3 or diff == 4):
        print 'Player wins!'
    else:
        print 'Player and computer tie!'
