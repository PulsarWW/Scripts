"""
This is the biggest proof of the "Monty Hall problem"

After 1,000,000 repetitions for each strategy we will see the results

More information about the problem: https://en.wikipedia.org/wiki/Monty_Hall_problem
"""

import random

class Player:
    def changeChoice(self, doors):
        for door in doors:
            if self.choice != door.number:
                self.choice = door.number
                return

    def gameResult(self, doors):
        for door in doors:
            if door.number == self.choice and door.outcome == True:
                self.victories += 1

    def __init__(self, victories, strategy, choice):
        self.victories = victories
        self.strategy = strategy
        self.choice = choice

class Door:
    def __init__(self, number, outcome):
        self.number = number
        self.outcome = outcome

def mixTheDoors(doors):
    trueDoor = random.randint(1, 3)
    for door in doors:
        if door.number == trueDoor:
            door.outcome = True
        else:
            door.outcome = False

def removeBadDoor(doors, choice):
    for door in doors:
        if door.number != choice and door.outcome == False:
            removed = door.number
            doors.remove(door)
            return removed

def coinflip():
    coin = random.randint(1, 2)
    if coin == 1:
        return True
    else:
        return False

player1 = Player(0, "change", 0) # will switch the door every time
player2 = Player(0, "insist", 0) # will never switch the door
player3 = Player(0, "random", 0) # will choose a door randomly
players = [player1, player2, player3]

door1 = Door(1, False)
door2 = Door(2, False)
door3 = Door(3, False)

for player in players:
    for i in range(1000000):
        doors = [door1, door2, door3]
        mixTheDoors(doors)

        player.choice = random.randint(1, 3)
        removed = removeBadDoor(doors, player.choice)

        if player.strategy == "change":
            player.changeChoice(doors)
            player.gameResult(doors)

        elif player.strategy == "insist":
            player.gameResult(doors)

        elif player.strategy == "random":
            if coinflip():
                player.changeChoice(doors)
                player.gameResult(doors)
            else:
                player.gameResult(doors)

print(
    "Player 1 won: " + str(player1.victories) + " times\n" + 
    "Player 2 won: " + str(player2.victories) + " times\n" +
    "Player 3 won: " + str(player3.victories) + " times\n"
)