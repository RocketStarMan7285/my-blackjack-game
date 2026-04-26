#driver program
import CardClass as create

#Print the hand of a player
def print_hand(playerInstance):
    print("\nYour hand: ")
    playerInstance.show_hand()

print("--------------BLACKJACK GAME--------------")

yourName = input("Enter your name here: ")

p1 = create.Player()
print(f"Player 1 {yourName} created")
cpu = create.Player()
print("Dealer created")

deck = create.Deck()
print("Deck created")
deck.shuffle_deck()

deck.deal_card(p1, 2)

print_hand(p1)
print("P1 total: ", p1.calc_hand())