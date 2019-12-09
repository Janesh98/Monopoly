class propertyCard:
    def __init__(self,colour,name,cost,rent):
        # self.type = cardtype,
        self.colour = colour
        self.name = name
        self.cost = cost
        self.rent = rent
        self.type = "propertyCard"

class communityChest:
    def __init__(self, title):
        self.type = "communityChest"
        self.title = title

class chance:
    def __init__(self, title):
        self.type = "chance"
        self.title = title
    
class transport:
    def __init__(self, name , rent):
        self.name = name
        self.rent = rent
        self.type = "transport"

class utility:
    def __init__(self,name,rent):#
        self.name = name 
        self.rent = rent
        self.type = "utility"

class tax:
    def __init__(self,name, charge):
        self.name = name
        self.charge = charge
        self.type = "tax"
    


propertys = [
    [
        propertyCard('brown','Nubar',60,2),
        propertyCard('brown','Larkfield',60,4)    
    ],
    [
        propertyCard('lightblue','Buisness School',100,6),
        propertyCard('lightblue','Henry Grattan',100,6),
        propertyCard('lightblue','T Larkin Theathre',120,8),
    ],
    [
        propertyCard('pink','DCU Canteen',140,10),
        propertyCard('pink','InterFate Centre',140,10),
        propertyCard('pink','Albert College',160,12),
    ],
    [
        propertyCard('orange','nursing building',180, 14),
        propertyCard('orange','Lonsdale Building',180, 14),
        propertyCard('orange','Estates Office',200, 16),
    ],
    [
        propertyCard('red','Londis',220,18),
        propertyCard('red','The U',220, 18),
        propertyCard('red','Hampstead',240,20)
    ],
    [
        propertyCard('yellow','Purcell House',260,22),
        propertyCard('yellow','All Hallows Campus',260,22),
        propertyCard('yellow','St.Patricks Campus',280,24)
    ],
    [
        propertyCard('green', 'Stokes Building', 300,26),
        propertyCard('green', 'Campus Store', 300,26),
        propertyCard('green', 'The Helix', 320,28),
    ],
    [
        propertyCard('blue', 'Mc Nulty Buidling', 350,35),
        propertyCard('blue', 'College Park', 400,50),
    ]
]

utilitys = [
    utility("libary",150),
    utility("DCU Sport", 150)
]

transports = [
    transport("Ballymun Road Bus Stop",200),
    transport("St pats bus stop" , 200),
    transport("Collins Ave Bus stop" , 200),
    transport("Helix bus stop", 200)
]

taxs = [
    tax("Income tax", 200),
    tax("Student Levy", 100)
]


chanceCards = [
    chance("Advance to GO"),
    chance("Advance token to DCU libary. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 times the amount thrown."),
    chance("Advance token to the nearest St pats bus stop and pay owner twice the rental to which he/she is otherwise entitled. If St pats bus stop is unowned, you may buy it from the Bank."),
    chance("Bank pays you dividend of $50."),
    chance("Get out of Jail Free"),
    chance("Go Back Three 3 Spaces."),
    chance("Go to jail"),
    chance("Make general repairs on all your property: For each house pay $25, For each hotel pay $100"),
    chance("Pay poor tax of $15"),
    chance("You have been elected Chairman of the Board. Pay each player $50. "),
]

communityChestCards = [
    communityChest("Advance to GO, Collect $200"),
    communityChest("Bank error in your favor. Collect $200."),
    communityChest("Doctor's fees. fee Pay $50. "),
    communityChest("From sale of stock you get $50."),
    communityChest("Get Out of Jail Free."),
    communityChest("Grand Opera Night. Collect $50 from every player for opening night seats."),
    communityChest("Holiday Fund matures. Receive $100"),
    communityChest("Income tax refund. Collect $20."),
    communityChest("Life insurance matures – Collect $100"),
    communityChest("Hospital Fees. Pay $50."),
    communityChest("School fees. Pay $50."),
    communityChest("Receive $25 consultancy fee."),
    communityChest("You are assessed for street repairs: Pay $40 per house and $115 per hotel you own.")
]


