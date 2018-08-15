from random import shuffle


SUITE = "H S D C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


class Deck():

    def __init__(self):
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def __str__(self):
        return "The Current Deck is: {}".format(self.allcards)

    def shuffle_deck(self):
        shuffle(self.allcards)

    def split_deck(self):
        return(self.allcards[:26], self.allcards[26:])


class Hand():

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "# of Cards: {}".format(len(self.cards))

    def add(self, added_card):
        self.cards.extend(added_card)

    def remove_card(self):
        return self.cards.pop()


class Player():

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return "{}: {} cards".format(self.name, len(self.hand.cards))

    def play_card(self):
        next_card = self.hand.remove_card()
        print("{}\'s card: {}".format(self.name, next_card))
        return next_card

    def war_cards(self):
        war = []
        if len(self.hand.cards) < 3:
            return war
        else:
            for x in range (3):
                war.append(self.hand.cards.pop())
            print("{}: War Cards: {}".format(self.name, war))
            return war

    def has_cards(self):
        return len(self.hand.cards) != 0

def rank_cards(card_c, card_u):
    if card_c[1] == card_u[1]:
        return True
    elif RANKS.index(card_c[1]) < RANKS.index(card_u[1]):
        print(user.name +" WINS!")
        user.hand.add(table_cards)
        return False
    else:
        print("Computer WINS!")
        comp.hand.add(table_cards)
        return False

# ******************************************************************************
# STARTING Game
# ******************************************************************************
ttl_rounds = 0
ttl_war = 0

d = Deck()
d.shuffle_deck()
# print(d)
(p_hand,c_hand) = d.split_deck()
# print(p_hand)
# print(c_hand)
comp = Player("Computer", Hand(c_hand))
name = input("Player, enter your name: ")
user = Player(name, Hand(p_hand))

while comp.has_cards() and user.has_cards():
    ttl_rounds += 1
    print("ROUND: {}".format(str(ttl_rounds)))
    print(comp)
    print(user)
    input("Press enter to play next card." + "\n")
    table_cards = []

    x = comp.play_card()
    y = user.play_card()

    table_cards.append(x)
    table_cards.append(y)

    if x[1] == y[1]:
        war = True
        while war:
            ttl_war += 1
            print("WAR WAR WAR WAR WAR WAR WAR")
            input("Press enter to start!")
            
            table_cards.extend(comp.war_cards())
            table_cards.extend(user.war_cards())

            x = comp.play_card()
            y = user.play_card()

            table_cards.append(x)
            table_cards.append(y)

            war = rank_cards(x, y)
    else:
        rank_cards(x, y)

print("Total Rounds Played: {}".format(str(ttl_rounds)))
print("Total Rounds of War: {}".format(str(ttl_war)))
if comp.has_cards():
    print("COMPUTER WINS! COMPUTER WINS! COMPUTER WINS! COMPUTER WINS! COMPUTER WINS!" )
else:
    print("{x} WINS! {x} WINS! {x} WINS! {x} WINS! {x} WINS! {x} WINS! {x} WINS!".format(x=user.name))
