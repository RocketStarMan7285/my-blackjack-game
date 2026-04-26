import random

#key: card rank, value: point value based on rank
rank_ptval = { #dictionary
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
                "10": 10,
                "Jack": 10,
                "Queen": 10,
                "King": 10,
                "Ace": 11 #an ace can also be a one
                }

### Class that contains data for a single playing card ###
# members:
# -string suit: Hearts, Clubs, Spades, Diamonds
# -string rank: 
#   -2 to 10 
#   -10-point cards: Jack, Queen, King 
#   -Ace: either one point or 11 points depending on hand
### -------------------------------------------------- ###    
class Card:

    #initializer
    def __init__(self, suit, rank):
        self.suit = suit #string
        self.rank = rank #string
        self.pt_val = rank_ptval[rank] #the point value of each card is the key 

    ### METHODS TO TEST OUT CARD OBJECTS ###
    #print the suit and rank of the card
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    #get the point value of each card
    def get_ptval(self):
         return self.pt_val

### class that contains a list of 52 unique playing cards in a deck ###
class Deck:

    #initializer: create a deck of 52 unique cards
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks = list(rank_ptval.keys()) #return a list of the keys in the rank_ptval dictionary
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks] #52 card deck created

    def shuffle_deck(self):
        print("Shuffling deck...")
        random.shuffle(self.cards)

    #print the amount of cards that are left in the deck
    def print_deck_amt(self):
        print(f"The deck has {len(self.cards)} cards")

    #deal a set number of cards to a player's hand (defaulted to 1)
    def deal_card(self, player, num_cards = 1, printCards = False):
        
        #before executing anything, throw an error if 
        #the amount of cards left in the deck is less than num_cards
        if(len(self.cards) < num_cards): 
            raise ValueError("Can't deal anymore cards")
        
        #retrieve the first (num_cards) from the deck and remove
        cards_to_deal = self.cards[:num_cards]
        if printCards == True:
            print("Dealt: ")
            for i in cards_to_deal:
                print(i, end=" ")
        #update the original list of cards to exclude the dealt cards
        self.cards = self.cards[num_cards:]
        #add the cards to the player's hand
        player.add_to_hand(cards_to_deal)

        
### class that contains a list of all the cards in the player's hand ###
class Player:

    def __init__(self):
        self.card_list = [] #list of cards in a player's hand
        self.points = 0


    def calc_hand(self): #calculate the number of points in a player's hand

        for card in self.card_list:
            self.points += card.pt_val

        return self.points

    def is_bust(self):
        if self.points > 21:
            return True
        else:
            return False 

    
    def show_hand(self):
        for card in self.card_list:
            print(card)

    def add_to_hand(self, cards):
        if isinstance(cards, list):
            self.card_list.extend(cards) #deal multiple cards
        else:
            self.hand.appead(cards) #deal a single card
        

