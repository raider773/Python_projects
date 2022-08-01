import random

#Classes

class Account:
    def __init__ (self,owner,balance = 1000):
        self.balance = balance
        self.owner = owner 
    
    def withdraw_money(self,value):        
        self.balance = self.balance - value
    def deposit_money(self,value):
        self.balance = self.balance + value
    def __str__(self):
        return '{} has $ {}'.format (self.owner,self.balance)
        
 
class Card:
    
    def __init__ (self,suit,value):
        self.value = value
        self.suit = suit
    def show (self):
        print ('{} of {}'.format (self.value,self.suit)) 
        
        
class Deck:
    def __init__(self):
        self.cards = []
        self.Create_Deck()
    def Create_Deck(self):
        for s in ['spades','Clubs','Diamonds','Hearts']:
            for v in range (1,14):
                self.cards.append(Card(s,v))
    def shuffle(self):
        random.shuffle(self.cards)
    def draw_card(self):       
        return self.cards.pop()
    
class Turn:
    
    def __init__(self,owner):
        self.hand = []
        self.owner = owner 
        
    def hit (self,deck):
        self.hand.append(deck.draw_card())        
            
    def show_hand (self):
        for i in self.hand:
            i.show()
            
            
            
#functions      
  
def Replay ():
    'ask if play another hand'
    replay = False
    print("Do you want to play another hand?")
    answer = input("Type yes or no: ")
    answer = answer.lower()    
    while answer != "yes" and answer != "no":
        print("Please enter a valid answer")
        answer = input("Type 'yes' or 'no': ")
        answer = answer.lower()
    if answer == "yes":
        replay = True
    return replay

def value_as (hand):
    'checks as value'
    value = hand[-1].value
    if hand[-1].value == 1:
        value = check_if_1_or_11()
    return value        
   
    
def value_11_12_13 (hand):
    'checks 11,12,13'
    value = hand[-1].value
    if hand[-1].value == 11 or hand[-1].value == 12 or hand[-1].value == 13:
        value =10
    return value


def check_if_1_or_11():
    while True:
        try:
            value = int(input("As value can be 1 or 11: "))
            while value != 1 and value != 11:
                print("only 1 or 11 please")
                value = int(input("As value can be 1 or 11: "))
            break
        except ValueError:
            print("only 1 or 11 please")
    return value
    

           
def check_card (hand):
    "use as or +10 func"
    if hand[-1].value == 1:
        value = value_as (hand)
    elif hand[-1].value == 11 or hand[-1].value == 12 or hand[-1].value == 13:
        value = value_11_12_13 (hand)
    else:
        value = hand[-1].value
    return value

def Hit_or_Stay():
    'stay = False'
    ask = input("Hit or Stay: ")
    while ask.lower() != 'hit' and ask.lower() != 'stay':
        print("please enter hit or stay")
        ask = input("Hit or Stay: ")
    if ask.lower() == "hit":
        return True
    elif ask.lower() == "stay":
        return False

def ask_bet():
    while True:
        try:
            value = int(input("Amount to bet: "))            
        except ValueError:
            print("only a number please")
            continue
        else:
            return value
            break

 
        
       
    

    
#MAIN PROGRAM

#account last all game 
AccountPlayer = Account('player')
while True:
    print("\n" * 100) 
    print(" WELCOME TO BLACKJACK")
    print(" Player can either hit (draw a card) or stay (end player's turn)")
    print(" If player reachs 21 he wins 150% of bet")
    print(" if player wins against computer then he wins bet * 2")
    print(" 11,12 and 13 have a value of 10")
    print(" if an As is drawn player can choose if the value is 1 or 11")
    print("current money:")
    print(AccountPlayer.balance)
    #create all classes
    deck = Deck()
    deck.shuffle()
    TurnPc = Turn('pc')
    TurnPlayer = Turn('player')
    
    #ask for bet and verify if valid 
    bet = ask_bet()
    while bet > AccountPlayer.balance:
        print('not enough money')
        bet = ask_bet()
        
    #give two cards to pc and show one
    TurnPc.hit(deck)
    PCValue = value_11_12_13 (TurnPc.hand)
    print()
    print("PC hand")
    print()
    print("*************")    
    TurnPc.show_hand()
    print()
    
    TurnPc.hit(deck)
    PCValue = PCValue + value_11_12_13(TurnPc.hand)
    
    #give player 2 cards adn show them
    TurnPlayer.hit(deck)
    PlayerValue = check_card(TurnPlayer.hand)    
    
    TurnPlayer.hit(deck)
    PlayerValue = PlayerValue + check_card(TurnPlayer.hand)
    
    print()
    print("Player hand")
    print()   
    TurnPlayer.show_hand()
    
    
    
    #Player Turn
    
    while Hit_or_Stay():
        TurnPlayer.hit(deck)
        PlayerValue = PlayerValue + check_card(TurnPlayer.hand)
        
        print()
        print("Player hand")
        print()   
        TurnPlayer.show_hand()
        
        if PlayerValue >= 21:
            break
    
    #after stay check if player won and give bet
        
    if PlayerValue > 21:
        print('value greater than 21. You lost')
        AccountPlayer.withdraw_money(bet)
        
    elif PlayerValue == 21:
        print("21 !! You Won")
        NewBet = (150*bet)//100
        AccountPlayer.deposit_money (NewBet)
        
    else:
        #Turn Pc
        while True:
            if PCValue > PlayerValue and  PCValue < 21:
                print("PC Won")
                AccountPlayer.withdraw_money(bet)
                break
            elif PCValue >= 21:
                print("You Won !!")
                NewBet = bet * 2
                AccountPlayer.deposit_money(NewBet)
                break
            
            else:
                TurnPc.hit(deck)
                PCValue = PCValue + value_11_12_13(TurnPc.hand)
                print()
                print("PC hand")
                print()
                TurnPc.show_hand()
                print()

    #check if balance = 0
    if AccountPlayer.balance == 0:
        print()
        print("you lost all your money")
        break
    if Replay () == False:
        print()
        print("thank you for playing!")
        break
    
input()
                
        
        
        
    
    
    
    
        
        
            
    
    
        
    
    
    
     
    
    
    
        
        
        
    
    
    
    
        
    
    
        
    
    
    
    
    
































