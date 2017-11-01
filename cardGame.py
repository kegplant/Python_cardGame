#need to finish 2 "unfinished" methods and implement loop in main 
#ask card by value rather than by card!
import random
def swap(i,j,arr):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
class Deck(object):
    def __init__(self):
        self.cards=[]
        for i in range(1,14):
            for j in range(4):
                self.cards.append(Card(j,i))
    def deal(self,number):
        output=[]
        for i in range(number):
            output.append(self.cards.pop())
        return output
    def shuffle(self):
        for i in range(len(self.cards)):
            swap(i,random.randint(0,len(self.cards)-1),self.cards)
        return self
    def display(self):
        for card in self.cards:
            print "value: ",card.value
            print "Suit: ",card.suit
class Card(object):
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
    def check(self):#integrate this
        print "Suit:", self.suit
        print "Value:", self.value
class Player(object):
    def __init__(self,name):
        self.name=name
        self.cardHand=[]
        self.score=0
    def draw(self,cards):
        if type(cards) == type([a,b]):
            self.cardHand+=cards
        else:
            self.append(cards)
        return self
    def ask(self,card):
        return card#could check it exists
    def give(self,card):#unfinished
        self.cardHand.pop(self.cardHand.index(card))
        #works so long as keeps track of card by the object's memory location
        #should be check by value, not by object
        return card
    def play(self,card):
        self.give(card)
        self.give(card)
        self.score += 1
        return self
    def removeDup(self):#unfinished
        #removes dupes and add score
#         j=1
#         for i in range(1,5):
#             if self.cardHand[i] not in self.cardHand:
#                 swap(i,j,self.cardHand)
#                 j++
        while j<len(self.cardHand):
            continue
        return self
#game: get pairs
def main():
    #simulate player action in main for now
    deck=Deck()
    players=[Player("Joe"),Player("Song")]
    deck.shuffle()
    for player in players:
        cards=deck.deal(5)#should be an array of cards
        player.draw(cards)#update player hand
    #while True:#add condition later: player hands empty
    value=raw_input("value?")
    target=players[0].ask(value)   
    if target in players[1].cardHand:    
        players[0].draw(players[1].give(target))
        players[0].play(target)#could check
    else:     
        players[0].draw(deck.deal(1))
    #decide who wins    
        