from random import randint

class Tile():
	'''
	category is the type of the tile. it can be property, chance, community_chest, police, jail, free_parking or go.
	position of tile on board (0-39)
	ptr - e.g if tile is of 'property'.
	'''
	def __init__(self, position, category, name=None, colour=None, price=None):
		self.position = position
		self.category = category
		self.name = name
		self.colour = colour
		self.price = price

class Pawn():
	def __init__(self, pawn_id, position, colour, ptr=None):
		self.pawn_id = pawn_id
		self.position = position
		self.colour = colour
		self.ptr = ptr

	def set_position(self, position):
		self.position = position

	def get_position(self):
		return self.position

	def move(self, moves):
		if self.position + moves > 39: #if pos = 35, moves = 6 new_pos = 1, 
			self.position = (self.position + moves) - 40
		else:
			self.position += moves

	def __str__(self):
		return "Pawn: {}, Position {}".format(self.pawn_id, self.position)

class Board():
	'''
	tiles - list of all tiles contained in board
	pawns - dictionary of pawns on board
	'''
	def __init__(self, tiles, pawns):
		self.tiles = tiles
		self.pawns = pawns

	def __str__(self):
		a = []
		for pawn in self.pawns.keys():
			s = str(self.pawns[pawn])
			a.append(s)
		return '\n'.join(a)


class Dice():
	def __init__(self):
		self.d1 = 1
		self.d2 = 1

	def roll(self):
		self.d1 = randint(1, 6)
		self.d2 = randint(1, 6)
		
		return self.d1, self.d2