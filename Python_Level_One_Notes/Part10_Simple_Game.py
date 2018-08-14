import random
###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will ask how many digits you'd like to guess and generate a random number.
# 2. You will then guess at that number
# 3. The computer will then give back clues, the clues are:
#
#     How many numbers you guessed are in the number
#     how many numbers are in the right spot
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

def number_List(n):
    """
    Convert any number into a lits with each digit being one element.
    """
    numStr = str(n)
    lst = []

    for i in numStr:
        lst.append(int(i))

    return lst


def number_right(nGss, nSol):
    """
    Will count how many numbers are in commone between two lists.
    """
    count = 0
    for i in nGss:
        if i in nSol:
            count += 1
    return count

def number_position(nGss, nSol):
    """
    Will count how many numbers are the same AND have the same index
    """
    count = 0
    for i in range(nLength):
        if nGss[i] == nSol[i]:
            count += 1
    return count

# Ask the user how many integers they want to guess
nLength = int(input("How many digits do would you like to guess (max: 10)?"))


# Establish number to guess
digits = list(range(10))
random.shuffle(digits)
numList = digits[:nLength]
# only used for debugging
# print(numList)

# Set var, correct[0] - how many numbers correct correct[1] - how many numbers are in correct spot
correct = [0,0]

# Start game, will loop until all numbers are found and in right spot
while correct != [nLength,nLength]:
    guess = input("What is your guess(or enter Q to quit):  ")
    if guess.lower() == 'q':
        break
    lstGuess = number_List(guess)
    print(lstGuess)

    correct[0] = number_right(lstGuess, numList)
    correct[1] = number_position(lstGuess, numList)

    print("You have guessed: {} correct number(s)".format(correct[0]))
    print("You have guessed: {} correct position(s)".format(correct[1]))
    if correct == [nLength, nLength]:
        print("Congratulations that is the number!")
