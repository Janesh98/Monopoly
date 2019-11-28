from random import randint

class Game:

    def __init__(self, player_list, current_player):

        ''' keeps track of all players and which players turn it is
            player_list : list of players (Player[])
            current_player : player whose turn it currently is (Player)
        '''
        self.players = player_list
        self.player = current_player

    def roll_dice(self):

        ''' return random number (int) '''
        return randint(1, 6)

    def sell_property(self, propertyID, propertyCost):

        ''' auctions off the property to all players
            return (None)
        '''
        for player in players:
            if player.wants(propertyID, propertyCost):
                self.buy_property(propertyID, propertyCost)
                break

    def trade(self, other_player):

        ''' allows current_player to trade assets from their
            portfolio with the portfolio of all other players
            if accepted
            return (None)
        '''
        # TODO
        pass


    def buy_property(self, propertyID, propertyCost):

        ''' allows the player to buy property,
            the price of the property is deducted
            from the players account balance and the
            property is added to their portfolio
            return (None)
        '''
        balance = self.player.get_balance() - propertyCost
        if balance > 0:
            self.player.withdraw(propertyCost)
            self.player.addProperty(propertyID)
        else:
            print("You do no have sufficient funds to purchase this property")

    def is_bankrupt(self):

        ''' checks whether the player is bankrupt,
            by making sure account balance + assets
            is greater than 0
            return (bool)
        '''
        return self.current_player.get_balance() or self.current_player.portfolio_value() <= 0

    def end_turn(self):

        ''' player ends their turn and the game gives
            the next player a turn
            return (None)
        '''
        i = 0
        while self.players[i] != self.player:
            i+=1
        if i == len(self.players) - 1:
            self.player =  self.players[0]
        else:
            self.player = self.players[i + 1]
