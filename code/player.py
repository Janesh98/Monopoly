class Player:

    def __init__(self, name, money, portfolio=[], jail_free_card=False):
        self.name = name
        self.money = money
        self.portfolio = portfolio
        self.jail_free_card = jail_free_card
        self.balance = money

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def addProperty(self,propertyID):
        self.portfolio.append(propertyID)
    
    def removeProperty(self,propertyID):
        if propertyID in self.portfolio:
            self.portfolio.remove(propertyID)
        else:
            return "User does not own this property"

    def getOutOfJailWon(self):
        self.getOutOfJail = True
    
    def getOutOfJailUsed(self):
        self.getOutOfJail = False
