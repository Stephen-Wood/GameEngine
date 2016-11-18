# Monster.py
# Thorin Schmidt
# 11/16/2016

''' Monster Package '''
from character import *
from random import randint, choice

class Monster(Character):
    ''' generic monster class '''
    def __init__(self,
                 name = "Generic Foe",
                 maxHealth = 10,
                 speed = 25,
                 stamina = 25,
                 strength = 10,
                 intelligence = 10,
                 dexterity = 10,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 50,
                 awareness = 50,
                 fear = 50):
        super(Monster, self).__init__(name, maxHealth, speed, stamina,
                                      strength, intelligence, dexterity,
                                      numberOfPotions, inventory)
        self.aggression = aggression
        self.awareness = awareness
        self.fear = fear  #indicates cowardice level

    def combat_choice(self):
        ''' combat AI

            returns a, h, or f.  Based on aggression, awareness, morale
            
            '''
        attackValue = randint(1,100) + self.aggression
        healValue = randint(1,100) + self.awareness
        fleeValue = randint(1,100) + self.fear

        if attackValue >= healValue and attackValue >= fleeValue:
            return "a"
        elif healValue >= attackValue and healValue >= fleeValue:
            return "h"
        elif fleeValue >= attackValue and fleeValue >= healValue:
            return "f"
        else:
            return "AI_error"

class Orc(Monster):
    ''' generic Orc class '''
    def __init__(self,
                 name = "Dorque da Orc",
                 maxHealth = 10,
                 speed = 25,
                 stamina = 25,
                 strength = 8,
                 intelligence = 8,
                 dexterity = 8,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 80,
                 awareness = 30,
                 fear = 20):
        super(Orc, self).__init__(name, maxHealth, speed, stamina, strength,
                                  intelligence, dexterity, numberOfPotions,
                                  inventory, aggression, awareness, fear)

def Slime(Monster):
    """ generic wimpy class
        this class"""
    def __init__(self,
                 name = "Slimey McSlimeface",
                 maxHealth = 6,
                 speed = 15,
                 stamina = 25,
                 strength = 5,
                 intelligence = 4,
                 dexterity = 2,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 60,
                 awareness = 15,
                 fear = 100):
        super(Slime, self).__init__(name, maxHealth, speed, stamina, strength,
                                   intelligence, dexterity, numberOfPotions,
                                   inventory, aggression, awareness, fear)

def Mir(Monster):
    """ generic Boss class

        this class is the boss class"""
    def __init__(self,
                 name = "Hackerman",
                 maxHealth = 16,
                 speed = 30,
                 stamina = 25,
                 strength = 7,
                 intelligence = 15,
                 dexterity = 10,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 150,
                 awareness = 120,
                 fear = 50):
        super(Hackerman, self).__init__(name, maxHealth, speed, stamina, strength,
                                   intelligence, dexterity, numberOfPotions,
                                   inventory, aggression, awareness, fear)   
              

def 

def random_monster():
    '''generate a monster at random

    create an instance of each monster here, then add that instance to
    the listOfMonsters.  The function will pick a random instance out of
    the list, then return it to the caller.'''
    
    monster = Monster()
    orc = Orc()
    slime = Slime()
              
    listOfMonsters = [monster, orc, slime]
    return choice(listOfMonsters)


if __name__ == "__main__":

    Grr = Monster(name = "Freddy")
    Randy = random_monster()
    print(Randy.name)


    
