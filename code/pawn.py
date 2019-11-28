class Pawn:

    def __init__(self, colour, position):
        self.colour = colour
        self.position = position

    def move(self, position):
        self.position = position