# Game_of_war
# Guillermo Ramos 
#
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website: 
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c 
# on July 23, 2014
# 

#----------------------------------------------------------------------
from queue import Queue
from Stack import Stack
import random

class War(object):
    def __init__(self):
        """Initializes all of the instance variables"""
        self.myCurrent	= None	# my currently displayed card
        self.otherCurrent = None	# other currently displayed card
        self.currentState = 0	# keeps track of the state of play
        self.dealingPile = Stack()	# stack
        self.myPlayingPile = Stack()	# stack 
        self.myStoragePile = Queue()# queue
        self.otherPlayingPile	= Stack()# stack 
        self.otherStoragePile	= Queue()# queue
        self.lootPile = Queue()		# queue
    
    def add_dealingPile(self):
        """creates the dealing pile using 5 decks of 0-9"""
        decks = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
        random.shuffle(decks)# adds the shuffled decks of cards to the dealer's pile
        
        for cards in range(len(decks)):
            self.dealingPile.push(decks[cards - 1])
        
        
        
    def deal(self):
        """deals out 25 cards from to each player's playing pile from shuffled dealers pile"""
             
        for i in range(25):
            top_card = self.dealingPile.pop()
            self.myPlayingPile.push(top_card)
            top_card = self.dealingPile.pop()
            self.otherPlayingPile.push(top_card)
            
    def makeMove(self):
        """Creates a round instance.
        :pre: cards have been dealt to each player
        post: returns true if one of the players has won, false otherwise."""
        
        print "Players are showing their card"      
        self.displayMyCard() #round starts by having the players display cards
        self.displayOtherCard()
        self.compare_cards() #compare the cards to see what needs to be done
        while self.currentState == 3 and self.mybooCheck() != 1: #if we are in a state of war and one of the players has not won
            self.displayMyCard() 
            self.displayOtherCard()                
            self.compare_cards()
            
        print"--------------------------------------"
        print "        END OF ROUND           "
        print"--------------------------------------"
        
        if self.currentState == 5 or self.currentState == 4: # if one of the players has won then return true
            return True
        else: 
            return False
           

        
    
    def displayMyCard(self):
        """displays a card on the screen and returns the value"""
        try:
            #try to get the topmost card and assign it to current
            self.myCurrent = self.myPlayingPile.top()
            print "player 1 shows " + str(self.myCurrent)
        except IndexError: #if playing pile is empty try to move the storage
                print "Player 1 has run out of cards"
                self.move_my_storage()
                if self.currentState != 5: #if moving the storage was succesful then display another card
                    self.displayMyCard()
                

    def displayOtherCard(self):
        """displays a card on the screen and returns the value"""
        try:
            #try to get the topmost card and assign it to current
            self.otherCurrent = self.otherPlayingPile.top()
            print "Player 2 shows " + str(self.otherCurrent)
        except IndexError: #if playing pile is empty try to move the storage
                print "Player 2 has run out of cards"
                self.move_other_storage()
                if self.currentState != 5: #if moving the storage was succesful then display another card
                    self.displayOtherCard
            
    
    def mybooCheck(self):
        """check to see if one the players has one"""
        size = (self.currentState == 4 or self.currentState == 5)
        return size
        
        
        
    def compare_cards(self):
        """"compares myCurrent to otherCurrent and behaves appropriately
        pre: cards have been displayed"""
        if (self.myCurrent > self.otherCurrent and self.mybooCheck() != True):
            self.currentState = 1
            self.moveMyToLoot()
            self.moveOtherToLoot()
            self.move_my_loot()
            print "Player 1 takes the win"
        elif (self.myCurrent < self.otherCurrent and self.mybooCheck() != True):
            self.currentState = 2
            self.moveMyToLoot()
            self.moveOtherToLoot()
            print "Player 2 takes the win"
            self.move_other_loot()
        elif (self.myCurrent == self.otherCurrent and self.mybooCheck() != True):
            print "We are in a state of war"                
            self.moveMyToLoot()
            self.moveOtherToLoot()
            self.moveMyToLoot()
            self.moveOtherToLoot()
            self.currentState = 3
        
        if self.currentState == 5:
            self.move_other_loot()
        
        elif self.currentState == 4:
            self.move_my_loot()
            
    def move_my_loot(self):
        # moves everything from lootPile to myStoragePile    
        for cards in range(self.lootPile.size()):
            card = self.lootPile.dequeue()
            self.myStoragePile.enqueue(card)
    def move_other_loot(self):
        # moves everything from lootPile to otherStoragePile
        for cards in range(self.lootPile.size()):
            card = self.lootPile.dequeue()
            self.otherStoragePile.enqueue(card)
    def move_my_storage(self):
        # moves everything from myStoragePile to myPlayingPile
        print "Trying to refill playing pile"
        if self.myStoragePile.size() != 0:
            for cards in range(self.myStoragePile.size()):
                card = self.myStoragePile.dequeue()
                self.myPlayingPile.push(card)
            print "Refill Succesful"
        else:
            print "Refill Unsuccesful"
            self.currentState = 5

    def move_other_storage(self):
        # moves everything from otherStoragePile to otherPlayingPile
        print "Trying to refill playing pile"
        if self.otherStoragePile.size() != 0:
            for cards in range(self.otherStoragePile.size()):
                card = self.otherStoragePile.dequeue()
                self.otherPlayingPile.push(card)
            print "Refill Succesful"
        else:
            print "Refill Unsuccesful"
            self.currentState = 4
            
    def moveMyToLoot(self):
        try:
            print "Turning player 1's card into the loot pile"
            Card = self.myPlayingPile.pop()
            self.lootPile.enqueue(Card)
        except IndexError:
            self.move_my_storage()
    
    def moveOtherToLoot(self):
        try:
            print "Turning player 2's card into the loot pile"
            Card = self.otherPlayingPile.pop()
            self.lootPile.enqueue(Card)
        except IndexError:
                self.move_other_storage()
           
        
        
        
        
    