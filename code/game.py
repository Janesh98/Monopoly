class Game:

    def __init__(self, player_list, current_player):

        ''' keeps track of all players and which players turn it is
            player_list : list of players (Player[])
            current_player : player whose turn it currently is (Player)
        '''
        pass

    def roll_dice(self):

        ''' return random number (int) '''
        pass

    def sell_property(self):

        ''' auctions off the property to all players
            return (None)
        '''
        pass

    def trade(self, other_player):

        ''' allows current_player to trade assets from their
            portfolio with the portfolio of all other players
            if accepted
            return (None)
        '''
        pass

    def buy_property(self):

        ''' allows the player to buy property,
            the price of the property is deducted
            from the players account balance and the
            property is added to their portfolio
            return (None)
        '''
        pass

    def is_bankrupt(self):

        ''' checks whether the player is bankrupt,
            by making sure account balance + assets
            is greater than 0
            return (bool)
        '''
        pass

    def end_turn(self):

        ''' player ends their turn and the game gives
            the next player a turn
            return (None)
        '''
        pass
