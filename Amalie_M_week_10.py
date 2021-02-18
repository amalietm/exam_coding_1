# Make a dice roller program using Object Oriented Concepts. The user should be able to define:
# * how many sides there are on a dice
# * how many dice there are
# * how many times the dice are rolled

import random
class Dice:
   

    def __init__(self, sides=6 ):
       sides = int (input("How many sides would you like your dice to have?: "))
       self.__sides = sides
       

    def get_sides(self):
        return self.__sides
        

    def roll_dice(self):
        return random.randint(1,self.__sides)
       
    def no_of_rolls(self, rolls = 1):
        rolls = int(input ("How many times do you want to roll?: "))
        self.rolls = rolls
        for _ in range (self.rolls):
           print("{0}".format(self.roll_dice()))
       

    def __str__(self):
        return str("Rolling a dice with {0} sides".format(self.__sides))

die_amnt = 3
while die_amnt > 2:
     die_amnt = int (input ("How many dice do you want to roll?\n") )
     if die_amnt > 2:
         print("The maximum dice you can roll are 2")

if die_amnt == 1:
 die = Dice()
 die.no_of_rolls()
 print(die)
elif die_amnt == 2:
  die = Dice()
  die2 = Dice()
  print(die)
  die.no_of_rolls()
  print(die2)
  die2.no_of_rolls()
       




