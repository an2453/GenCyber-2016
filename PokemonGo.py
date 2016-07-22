# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:38:10 2016

Anusua Nath
PokemonGo

@author: student
"""


''
from random import randint

class Pokemon:
    # Pokemon maker
    def __init__(self, oriName, oriType, orihp, oriMoves):
        # Pokemon traits
        self.name = oriName
        self.type = oriType
        self.hp = orihp
        self.cp = randint(1, 600)
        self.moves = oriMoves
   
   #Fight
    def battle(self, myMove, opponent, opponentMove):
        # Make my move and announce it
        print(self.name + " USED " + myMove + "!!!")
        # Opponent health - my attack damage
        opponent.hp -= (self.moves[myMove] * self.cp)
        print(opponent.name + " HAS " + str(opponent.hp) + " HP LEFT!!!")
        # Check if they are alive
        if opponent.hp <= 0:
            print(opponent.name + " DIED!!!")
            print("YOU WIN!!!")
            return
        # Make their move
        print(opponent.name + " USED " + opponentMove + "!!!")
        self.hp -= (opponent.moves[opponentMove] * opponent.cp)
        print(self.name + " HAS " + str(self.hp) + " HP LEFT!!!")
        # Check if I am alive
        if self.hp <= 0:
            print(self.name + " DIED!!!")
            print("YOU LOSE!!!")
            return
        print("DRAW!!!")
        
        
eevee_moves = {"Swift": 10, "Dig": 20}
vee = Pokemon("Eevee", "Normal", 90, eevee_moves)
 
squirtle_moves = {"Squirt": 40, "Water Gun": 100}       
squats = Pokemon("Squirtle", "Water", 90, squirtle_moves)

print("Vee CP: " + str(vee.cp))
print("Squats CP: " + str(squats.cp))

vee.battle("Dig", squats, "Squirt")

