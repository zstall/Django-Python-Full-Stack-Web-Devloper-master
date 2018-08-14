#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Creating Deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def __str__(self):
        return("The Deck of cards is: {}".format(self.allcards))

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_deck(self):
        print("Splitting deck between players.")
        return(self.allcards[:26], self.allcards[26:])


class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def __str__(self, cards):
        return "Contains {} cards".format(len(slef.cards))

    def add(self, added_card):
        self.cards.extend(added_card)

    def remove_card(self):
        return self.cards.pop()


class Player():
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return("{} has {} cards remaining".format(self.name, len(self.hand.cards)))

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has played {} card.".format(self.name, drawn_card))
        print("\n")
        return(drawn_card)

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0

def rank_cards(card1, card2):
    # Player card should always be card2
    if card1[1] == card2[1]:
        return True
    elif RANKS.index(card1[1]) < RANKS.index(card2[1]):
        return False
        print(user.name+" has the higher card, adding to hand.")
        user.hand.add(table_cards)
    else:
        return False
        print(comp.name+" has the higher card, adding to hand.")
        comp.hand.add(table_cards)

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")


# Create the deck and split it in half
d = Deck()
d.shuffle()
half1,half2 = d.split_deck()
# Verifying that there are two halfs for players
# print(half1)
# print(half2)

comp = Player("Computer", Hand(half1))
p1 = input("Please enter your name: ")
user = Player(p1, Hand(half2))
# print(comp.hand.cards)
# print(user.hand.cards)

# Round count:
total_rounds = 0
war_count = 0

# Begin the game!
while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Round: " + str(total_rounds))
    print("Currently each player has: ")
    print(user)
    print(comp)
    input("Press Enter to play a card! \n")

    # Create a table for Cards
    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    # Check for a war
    if c_card[1] == p_card[1]:
        war = True
        while war:
            war_count += 1
            input("WAR! Press enter to continue!!! \n")
            table_cards.extend(user.remove_war_cards())
            table_cards.extend(comp.remove_war_cards())

            # War play Cards
            c_card = comp.play_card()
            p_card = user.play_card()

            table_cards.append(c_card)
            table_cards.append(p_card)

            war = rank_cards(c_card, p_card)
    else:
        rank_cards(c_card, p_card)

print("Great Game, it lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")






# Use the 3 classes along with some logic to play a game of war!
