import random

class Player:
    """ Represents a player object, who each have health and a set of moves"""

    def __init__(self, mode = "human"):
        self.health = 100
        self.mode = mode

    # uses pseudo-random number generation for moves
    def normal_strike(self):
        if self.mode == "human":
            return random.randrange(18, 25)
        elif self.mode == "easy":
            return random.randrange(15, 22)
        elif self.mode == "medium":
            return random.randrange(18, 25)
        else:
            return random.randrange(21, 25)

    def lucky_strike(self):
        if self.mode == "human":
            return random.randrange(10, 35)
        elif self.mode == "easy":
            return random.randrange(7, 28)
        elif self.mode == "medium":
            return random.randrange(10, 35)
        else:
            return random.randrange(20, 35)


    # implemented heal as a negative number to easily distinguish
    def heal(self):
        return random.randrange(-30,-20)
