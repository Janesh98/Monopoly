from random import randint

class Game:

    def __init__(self, player_list, current_player):
        # keeps track of all players and which players turn it is
        self.players = player_list
        self.player = current_player

    def roll_dice(self):
        return randint(1, 6)

    def sell_property(self, propertyID, propertyCost):
        # auctions off the property to all players
        for player in players:
            if player.wants(propertyID, propertyCost):
                self.buy_property(propertyID, propertyCost)
                break

    def trade(self, other_player):
	    # allow trading of player portfolio with another player
        for other_prop in other_player.portfolio:
		    if self.player.wants(other_prop):
				for prop in self.player.portfolio:
				    if other_player.wants(prop):
					    self.player.swap(other_prop, other_player, prop)
						return
		print("{} does not wish to trade".format(other_player.name)


    def buy_property(self, propertyID, propertyCost):
        balance = self.player.get_balance() - propertyCost
        if balance > 0:
            self.player.withdraw(propertyCost)
            self.player.addProperty(propertyID)
        else:
            print("You do no have sufficient funds to purchase this property")

    def is_bankrupt(self):
        # bankrupt if account balance + assets is <= 0
        return self.current_player.get_balance() + self.current_player.portfolio_value() <= 0

    def end_turn(self):
	    # players turn ends, game gives next player a turn
        i = 0
        while self.players[i] != self.player:
            i+=1
        if i == len(self.players) - 1:
            self.player =  self.players[0]
        else:
            self.player = self.players[i + 1]
