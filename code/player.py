class Player:

    def __init__(self, name, money, portfolio, jail_free_card=False):

        ''' initializes:
            name : user name (str)
            money : default starting account balance (int)
            portfolio : list of properties owned (str[])
            jail_free_card : boolean indicating whether the player is
                             in possession of a get out of jail free
                             card (bool)
        '''
        pass

    def get_balance(self):

        ''' return player account balance (int) '''
        pass

    def withdraw(self, amount):
        ''' withdraws amount from players' account balance
            return None
        '''
        pass

    def deposit(self, amount):

        ''' deposits amount into players' account
            return None
        '''
        pass
