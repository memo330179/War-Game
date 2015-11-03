# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:20:41 2015

@author: Guillermo Ramos
"""
from war_game import War

def main():
    new_game = War()
    new_game.add_dealingPile()
    new_game.deal()
    while (new_game.makeMove() == False):
        new_game.makeMove()
    if new_game.currentState == 5:
        print "______________________________________"
        print "PLAYER 2 WINS!!!!!!"
        print "Final Score:"
        print str(new_game.otherPlayingPile.size()) + " in the playing pile and.."
        print str(new_game.otherStoragePile.size()) + " in the storage pile"
        print "______________________________________"
    elif new_game.currentState == 4:
        print "______________________________________"
        print "PLAYER 1 WINS!!!!!!"
        print "Final Score:"
        print str(new_game.myPlayingPile.size()) + " in the playing pile and.."
        print str(new_game.myStoragePile.size()) + " in the storage pile"
        print "______________________________________"

    
    
main()