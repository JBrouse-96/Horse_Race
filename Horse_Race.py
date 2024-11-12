from tkinter import *
import random
from PIL import Image, ImageTK


root = Tk()
root.title('Horse Races - Place Your Bets!')
root.iconbitmap(r'F:\\Python_Projects\\Horse_Race\\Images\\PNG_cards')
root.geometry("900x500")
root.configure(background="green")

# Shuffle the cards
def shuffle():
    # Define the deck
    suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
    values = range(2, 15) # 11=Jack, 12= Queen, 13=King, 14=Ace

    global deck
    deck=[]

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_[{suit}]')

    # Create the players
    global dealer, player
    dealer = []
    player =[]

    # Grab a random card for the dealer
    card = random.choice(deck)
    # Remove card from deck
    deck.remove(card)
    # Append Card to dealer deck
    dealer.append(card)
    # Output card to screen
    dealer_label.config(text=card)

    # Grab a random card for the player
    card = random.choice(deck)
    # Remove card from deck
    deck.remove(card)
    # Append Card to dealer deck
    player.append(card)
    # Output card to screen
    player_label.config(text=card)

    # Put the number of remaining cards in the title bar
    root.title(f'Horse Races - {len(deck)} Cards Left in play!')

# Deal out cards
def deal_cards():
    try:
        # Get the dealers card
        card = random.choice(deck)
        # Remove card from deck
        deck.remove(card)
        # Append Card to dealer deck
        dealer.append(card)
        # Output card to screen
        dealer_label.config(text=card)

        # Get the players card
        card = random.choice(deck)
        # Remove card from deck
        deck.remove(card)
        # Append Card to dealer deck
        player.append(card)
        # Output card to screen
        player_label.config(text=card)

        # Put the number of remaining cards in the title bar
        root.title(f'Horse Races - {len(deck)} Cards Left in play!')
    except:
        root.title('Error. Please restart application.')

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Create Frames For Cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

# Put cards in frames
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)


# Create a couple buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command = shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=("Helvetica", 14), command = deal_cards)
card_button.pack(pady=20)


shuffle()

root.mainloop()