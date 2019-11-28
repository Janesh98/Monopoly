import random

class Board:

    def __init__(self, pawn_list, property_list, chance_cards, comm_chest_cards):
        ''' initializes:
            pawn_list : list of different types of pawns (Pawn[])
            property_list : list of different types of pawns (Properties[])
            chance_cards : list of different types of chance cards (Chance[])
            comm_chest_cards : list of different community chest cards (Comm[])
        '''
        self.pawn_list = pawn_list
        self.property_list = property_list
        self.chance_cards = chance_cards["yes","no"]
        self.comm_chest_cards = comm_chest_cards

    def random_chance_card(self, chance_cards):

        ''' returns a random card from the list of the chance type
            return (card)
        '''
        return random.choice(chance_cards)

N
     def random_comm_card(self, card_type):

        ''' returns a random card from the list of the community chest type
            return (card)
        '''
        return random.choice(comm_chest_cards)
