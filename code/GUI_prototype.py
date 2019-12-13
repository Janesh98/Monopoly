from tkinter import *
from PIL import Image, ImageTk
from board import *
from time import sleep

'''
BOARD RELATED CLASSES
Pawn Token Class
Pawn Contaier Class - for showing pawns on a tile
Tile Classes (Side, Corner)
Board Display Class
'''

class PawnToken(Canvas): #REDUNDENT CLASS
	def __init__(self, parent, colour):
		Canvas.__init__(self, parent)
		self.parent = parent
		self.colour = colour
		self.draw_pawn()

	def draw_pawn(self):
		points = [60, 10, 110, 60, 60, 110, 10, 60]
		self.create_polygon(points, fill = self.colour)

#This the container inside each tile which handles pawn placement
class PawnContainer(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg="white")
		self.parent = parent
		self.pawn_tokens = []

	def update_container(self, pawns):
		for token in self.pawn_tokens:
			token.destroy()
		for pawn in pawns:
			pawn_token = Label(self, bg = pawn.colour)
			pawn_token.grid(row=1, column= pawn.pawn_id + 1, ipadx=2, ipady=2, padx=1)
			self.pawn_tokens.append(pawn_token)

#frames for side tile on board (property, chance, community chest)
#width = parent.parent as it will get width from frame containing parent canvas
class Tile1(Frame):
	def __init__(self, parent, position, category, name=None, colour=None, price=None):
		Frame.__init__(self, parent, width = parent.width * (2/25), height = parent.height * (13/100), highlightthickness = 1, highlightbackground = "black", bg="white") # correct ratios for side tile size            
		self.parent = parent
		self.position = position
		self.width = parent.width * (2/25)
		self.height = parent.height * (13/100)
		self.category = category
		self.name = name
		self.colour = colour
		self.price = price
		self.pawns_on_tile = []
		self.pawns_container = PawnContainer(self)
		self.init_tile()
		self.show_pawn()

	def init_tile(self):
		default_pawns_rel_height = .55
		if self.category == "property":
			self.banner = Canvas(self, bg = self.colour, bd = 0)
			self.banner.place(relx=0, rely=0, relwidth=1, relheight=.25)

			#code for putting text on canvas to allow rotation
			# self.property_name = Canvas(self, bg = None)
			# self.property_txt = self.property_name.create_text(20, 10, font = ('Helvetica', 7), width = self.width - 15, justify = CENTER)
			# self.property_name.insert(self.property_txt, 7, self.name)
			# self.property_name.place(relx=0, rely=.25)

			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=.25)

			self.pawns_container.place(relx=0, rely=default_pawns_rel_height, relwidth=1, relheight=.10)

			self.property_price = Label(self, text = self.price, font = ('Helvetica', 7), bg="white")
			self.property_price.place(relx=0, rely=.8)

		elif self.category == "community_chest":
			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=.25)

			self.pawns_container.place(relx=0, rely=default_pawns_rel_height, relwidth=1, relheight=.10)

		elif self.category == "tax":
			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=.25)

			self.pawns_container.place(relx=0, rely=default_pawns_rel_height, relwidth=1, relheight=.10)

		elif self.category == "transport":
			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=.25)

			self.pawns_container.place(relx=0, rely=default_pawns_rel_height, relwidth=1, relheight=.10)

		elif self.category == "chance":
			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=.25)

			self.pawns_container.place(relx=0, rely=default_pawns_rel_height, relwidth=1, relheight=.10)

	def show_pawn(self):
		for pawn in self.parent.pawns:
			if pawn.position == self.position and pawn not in self.pawns_on_tile:
				self.pawns_on_tile.append(pawn)
			elif pawn in self.pawns_on_tile and pawn.position != self.position:
				print("Pawn {} moved".format(pawn.pawn_id))
				self.pawns_on_tile.pop(self.pawns_on_tile.index(pawn))

		self.pawns_container.update_container(self.pawns_on_tile)

	def __str__(self):
		return("pos: {}, name: {}, pawns: {}".format(self.position, self.name, self.pawns_on_tile))

class Tile2(Tile1):
	def __init__(self, parent, position, category, name=None, colour=None, price=None):
		Frame.__init__(self, parent, width = parent.width * (13/100), height = parent.height * (2/25), highlightthickness = 1, highlightbackground = "black", bg="white") # correct ratios for side tile size            
		self.parent = parent
		self.position = position
		self.width = parent.width * (13/100)
		self.height = parent.height * (2/25)
		self.category = category
		self.name = name
		self.colour = colour
		self.price = price
		self.pawns_on_tile = []
		self.pawns_container = PawnContainer(self)
		self.init_tile()
		self.show_pawn()

	def init_tile(self):
		default_pawns_rel_height = 0
		if self.category == "property":
			self.banner = Canvas(self, bg = self.colour, bd = 0)
			self.banner.place(relx=.75, rely=0, relwidth=.25, relheight=1)

			self.property_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.property_name.place(relx=0, rely=.1)

			self.pawns_container.place(relx=default_pawns_rel_height, rely=.5, relwidth=.75, relheight=.15)

			self.property_price = Label(self, text = self.price, font = ('Helvetica', 7), bg="white")
			self.property_price.place(relx=0, rely=.7)

		elif self.category == "community_chest":
			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=.25)

			self.pawns_container.place(relx=default_pawns_rel_height, rely=.5, relwidth=.75, relheight=.15)

		elif self.category == "transport":
			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=.1)

			self.pawns_container.place(relx=default_pawns_rel_height, rely=.5, relwidth=.75, relheight=.15)

			self.property_price = Label(self, text = self.price, font = ('Helvetica', 7), bg="white")
			self.property_price.place(relx=0, rely=.7)


class Tile3(Tile1):
	def __init__(self, parent, position, category, name=None, colour=None, price=None):
		Frame.__init__(self, parent, width = parent.width * (2/25), height = parent.height * (13/100), highlightthickness = 1, highlightbackground = "black", bg="white") # correct ratios for side tile size            
		self.parent = parent
		self.position = position
		self.width = parent.width * (2/25)
		self.height = parent.height * (13/100)
		self.category = category
		self.name = name
		self.colour = colour
		self.price = price
		self.pawns_on_tile = []
		self.pawns_container = PawnContainer(self)
		self.init_tile()
		self.show_pawn()

	def init_tile(self):
		default_pawns_rel_height = .35
		if self.category == "property":
			self.banner = Canvas(self, bg = self.colour, bd = 0)
			self.banner.place(relx=0, rely=.75, relwidth=1, relheight=.25)

			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=0)

			self.pawns_container.place(relx=0, rely=default_pawns_rel_height, relwidth=1, relheight=.10)

			self.property_price = Label(self, text = self.price, font = ('Helvetica', 7), bg="white")
			self.property_price.place(relx=0, rely=.6)

		elif self.category == "transport":
			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=0)

			self.pawns_container.place(relx=0, rely=default_pawns_rel_height, relwidth=1, relheight=.10)

		elif self.category == "chance":
			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=0)

			self.pawns_container.place(relx=0, rely=default_pawns_rel_height, relwidth=1, relheight=.10)

class Tile4(Tile1):
	def __init__(self, parent, position, category, name=None, colour=None, price=None):
		Frame.__init__(self, parent, width = parent.width * (13/100), height = parent.height * (2/25), highlightthickness = 1, highlightbackground = "black", bg="white") # correct ratios for side tile size            
		self.parent = parent
		self.position = position
		self.width = parent.width * (13/100)
		self.height = parent.height * (2/25)
		self.category = category
		self.name = name
		self.colour = colour
		self.price = price
		self.pawns_on_tile = []
		self.pawns_container = PawnContainer(self)
		self.init_tile()
		self.show_pawn()

	def init_tile(self):
		default_pawns_rel_height = .25
		if self.category == "property":
			self.banner = Canvas(self, bg = self.colour, bd = 0)
			self.banner.place(relx=0, rely=0, relwidth=.25, relheight=1)

			self.property_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.property_name.place(relx=.25, rely=.1)

			self.pawns_container.place(relx=default_pawns_rel_height, rely=.5, relwidth=.75, relheight=.15)

			self.property_price = Label(self, text = self.price, font = ('Helvetica', 7), bg="white")
			self.property_price.place(relx=.3, rely=.7)

		elif self.category == "community_chest":
			self.property_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.property_name.place(relx=.25, rely=.1)

			self.pawns_container.place(relx=default_pawns_rel_height, rely=.5, relwidth=.75, relheight=.15)

		elif self.category == "chance":
			self.property_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.property_name.place(relx=.25, rely=.1)

			self.pawns_container.place(relx=default_pawns_rel_height, rely=.5, relwidth=.75, relheight=.15)

		elif self.category == "tax":
			self.property_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.property_name.place(relx=.25, rely=.1)

			self.pawns_container.place(relx=default_pawns_rel_height, rely=.5, relwidth=.75, relheight=.15)

		elif self.category == "transport":
			self.property_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.property_name.place(relx=0, rely=.1)

			self.pawns_container.place(relx=default_pawns_rel_height, rely=.5, relwidth=.75, relheight=.15)

			self.property_price = Label(self, text = self.price, font = ('Helvetica', 7), bg="white")
			self.property_price.place(relx=.3, rely=.7)

#frame for corner tile (go to jail, jail, free parking, go)
class Corner(Frame):
	def __init__(self, parent, position, category, name, image=None, price=None):
		Frame.__init__(self, parent, width = parent.width * (13/100), height = parent.height * (13/100), highlightthickness = 1, highlightbackground = "black") # correct ratios for corner tile size            
		self.parent = parent
		self.position = position
		self.width = parent.width * (13/100)
		self.height = parent.height * (13/100)
		self.category = category
		self.name = name
		self.img = ImageTk.PhotoImage(Image.open(image).resize( (round(self.height), round(self.width) ), Image.ANTIALIAS))
		self.price = price
		self.pawns_on_tile = []
		self.pawns_container = PawnContainer(self)
		self.init_tile()
		self.show_pawn()

	def init_tile(self):
		self.corner_canvas = BoardImage(self, self.width, self.height,)
		self.corner_canvas.place(x=0, y=0)
		self.corner_canvas.background = self.img
		self.bg = self.corner_canvas.create_image(0, 0, anchor=NW, image=self.img)

		self.pawns_container.place(relx=.45, rely=.80, relwidth=.5, relheight=.10)
		self.pawns_container.lift()

	def show_pawn(self):
		for pawn in self.parent.pawns:
			if pawn.position == self.position and pawn not in self.pawns_on_tile:
				self.pawns_on_tile.append(pawn)
			elif pawn in self.pawns_on_tile and pawn.position != self.position:
				print("Pawn {} moved".format(pawn.pawn_id))
				self.pawns_on_tile.pop(self.pawns_on_tile.index(pawn))

		self.pawns_container.update_container(self.pawns_on_tile)

	def __str__(self):
		return("pos: {}, name: {}, pawns: {}".format(self.position, self.name, self.pawns_on_tile))

class BoardImage(Canvas):
	def __init__(self, parent=None, w=None, h=None):
		Canvas.__init__(self, parent, width=w, height=h) # correct ratios for corner tile size            
		self.parent = parent
		self.height = h
		self.width = w

#Board will contain 11*11 grid
class BoardDisplay(Frame):
	def __init__(self, parent, w=None, h=None, image=None, tiles=None, pawns=None):
		Frame.__init__(self, parent, width=w, height=h, bd = 0, highlightthickness = 2, highlightbackground = "black")              
		self.parent = parent
		self.width = w
		self.height = h
		self.background_img = ImageTk.PhotoImage(Image.open(image).resize( (round(h*(87/100)), round(w*(87/100)) ), Image.ANTIALIAS)) #initialize board image
		self.tiles = tiles
		self.pawns = pawns
		self.init_board()
		self.display_tiles = self.build_tiles()
		self.display_pawns = self.build_pawns()

	def init_board(self):
		self.pack(fill = BOTH, expand = 1)

		self.board_canvas = BoardImage(self, self.width*(87/100), self.height*(87/100))
		self.board_canvas.place(x=0, y=0)
		self.board_canvas.background = self.background_img
		self.bg = self.board_canvas.create_image(30, 30, anchor=NW, image=self.background_img)

	def find_corner(self, position):
		r = 0
		c = 0
		if position % 9 == 0:
			r = 11
			c = 11
			img_path = "go.png"
		elif position % 9 == 1:
			r = 11
			c = 1
			img_path = "jail.png"
		elif position % 9 == 2:
			r = 1
			c = 1
			img_path = "free_parking.png"
		elif position % 9 == 3:
			r = 1
			c = 11
			img_path = "goto_jail.png"

		return r, c, img_path

	def build_tiles(self):
		a = []
		for tile in self.tiles:
			if tile.position % 10 == 0:
				r, c, img_path = self.find_corner(tile.position)
				t = Corner(self, tile.position, tile.category, tile.name, img_path)
				t.grid(row=r, column=c)
				a.append(t)
			elif  10 > tile.position > 0:
				t = Tile1(self, tile.position, tile.category, tile.name, tile.colour, tile.price)
				t.grid(row=11, column=11-tile.position)
				a.append(t)
			elif  20 > tile.position > 10:
				t = Tile2(self, tile.position, tile.category, tile.name, tile.colour, tile.price)
				t.grid(row=11-(tile.position - 10), column=1)
				a.append(t)
			elif  30 > tile.position > 20:
				t = Tile3(self, tile.position, tile.category, tile.name, tile.colour, tile.price)
				t.grid(row=1, column=1+(tile.position - 20))
				a.append(t)
			elif  40 > tile.position > 30:
				t = Tile4(self, tile.position, tile.category, tile.name, tile.colour, tile.price)
				t.grid(row=1+(tile.position - 30), column=11)
				a.append(t)
			else:
				print("oops!")

		return a

	def build_pawns(self):
		a = []
		for pawn in self.pawns:
			a.append(PawnToken(self.display_tiles[1], pawn.colour))

		return a

	def refresh(self, pawns):
		pass

'''
INTERFACE RELATED CLASSES
Controls Class
Property Info Class
'''

class Controls(Frame):
	def __init__(self, parent, board):
		Frame.__init__(self, parent, highlightthickness = 2, highlightbackground = "black", bd = 2)             
		self.parent = parent
		self.root = parent.parent
		self.board = board
		self.dice = parent.dice
		self.init_window()
		self.buttons()

	def init_window(self):
		self.pack(side = BOTTOM)

	def do_something(self):
		print("Foo")

	def roll_com(self):
		d1, d2 = self.dice.roll()
		self.parent.d1.set("Die 1: {}".format(d1))
		self.parent.d2.set("Die 2: {}".format(d2))
		print("Rolled {}:{}".format(d1, d2))
		n = d1 + d2
		self.board.pawns[0].move(n)
		for d_tile in self.board.display_tiles:
			d_tile.show_pawn()

	def test_move_pawn(self):
		self.board.pawns[1].move(1)
		for d_tile in self.board.display_tiles:
			d_tile.show_pawn()

	def test_com1(self):
		print(self.board.pawns[0])

	def test_com2(self):
		print(len(self.board.display_tiles))
		for d_tile in self.board.display_tiles:
			print(d_tile)

	def buttons(self):
		default_width = 18

		self.roll = Button(self, text ="ROLL", fg = "black", width = default_width, command = self.roll_com)
		self.roll.grid(row=1, column=1)

		self.buy = Button(self, text ="BUY", fg = "black", width = default_width, command = self.test_com1)
		self.buy.grid(row=1, column=2)

		self.sell = Button(self, text ="SELL", fg = "black", width = default_width, command = self.test_com2)
		self.sell.grid(row=1, column=3)

		self.bail = Button(self, text ="BAIL", fg = "black", width = default_width, command = self.test_move_pawn)
		self.bail.grid(row=2, column=1)

		self.buy_house = Button(self, text ="BUY HOUSE/HOTEL", fg = "black", width = default_width, command = self.do_something)
		self.buy_house.grid(row=2, column=2)

		self.mortgage = Button(self, text ="MORTGAGE", fg = "black", width = default_width, command = self.do_something)
		self.mortgage.grid(row=2, column=3)		

		self.abandon = Button(self, text ="ABANDON", fg = "red", width = default_width, command = self.root.destroy)
		self.abandon.grid(row=2, column=4)


class PropertyInfo(Frame):
	def __init__(self, parent, deed_index, category, name=None, colour=None, rent=None, mortgage=None, unmortgage=None):
		Frame.__init__(self, parent, width = 850 * (2/25), height = 850 * (13/100), highlightthickness = 1, highlightbackground = "black", bg="white") # correct ratios for side tile size            
		self.parent = parent
		self.deed_index = deed_index
		self.width = 850 * (2/25)
		self.height = 850 * (13/100)
		self.category = category
		self.name = name
		self.colour = colour
		self.rent = rent
		self.mortgage = mortgage
		self.unmortgage = unmortgage
		self.init_tile()

	def init_tile(self):
		if self.category == "property":
			self.banner = Canvas(self, bg = self.colour, bd = 0)
			self.banner.place(relx=0, rely=0, relwidth=1, relheight=.25)

			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg=self.colour)
			self.tile_name.place(relx=.15, rely=.075)

			self.rent_lbl = Label(self, text ="Rent: " + self.rent, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.rent_lbl.place(relx=0, rely=.25)

			self.mortgage_lbl = Label(self, text ="Mortgage: " + self.mortgage, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.mortgage_lbl.place(relx=0, rely=.55)

			self.unmortgage_lbl = Label(self, text ="Unmortgage: " + self.unmortgage, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.unmortgage_lbl.place(relx=0, rely=.75)

		elif self.category == "transport":
			self.banner = Canvas(self, bg = 'white', bd = 0)
			self.banner.place(relx=0, rely=0, relwidth=1, relheight=.25)

			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=.25)

			self.rent_lbl = Label(self, text ="Rent: " + self.rent, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.rent_lbl.place(relx=0, rely=.55)

		elif self.category == "utility":
			self.banner = Canvas(self, bg = 'white', bd = 0)
			self.banner.place(relx=0, rely=0, relwidth=1, relheight=.25)

			self.tile_name = Label(self, text = self.name, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.tile_name.place(relx=0, rely=.25)

			self.rent_lbl = Label(self, text = self.rent, font = ('Helvetica', 7), justify = CENTER, wraplength = self.width-4, padx=2, bg="white")
			self.rent_lbl.place(relx=0, rely=.5)


#will contain 9*5 grid
class Information(Frame):

	def __init__(self, parent=None, property_deeds=None, dice=None):
		Frame.__init__(self, parent, highlightthickness = 2, highlightbackground = "black", bd = 2)               
		self.parent = parent
		self.property_deeds = property_deeds
		self.dice = parent.dice
		self.funds_str = StringVar()
		self.d1 = parent.d1
		self.d2 = parent.d2
		self.display_deeds = self.build_property_deeds()
		self.init_window()
		self.info()

	def init_window(self):
		self.pack(side = TOP, fill = BOTH)

	def build_property_deeds(self):
		a = []
		for deed in self.property_deeds:
			if  6 > deed.deed_index:
				t = PropertyInfo(self, deed.deed_index, deed.category, deed.name, deed.colour, deed.rent, deed.mortgage, deed.unmortgage)
				t.grid(row=2, column=(1+deed.deed_index), padx=1, pady=4)
				a.append(t)
			elif 8 > deed.deed_index > 5:
				t = PropertyInfo(self, deed.deed_index, deed.category, deed.name, deed.colour, deed.rent, deed.mortgage, deed.unmortgage)
				t.grid(row=2, column=(2+deed.deed_index), padx=1, pady=4)
				a.append(t)
			elif 17 > deed.deed_index > 7:
				t = PropertyInfo(self, deed.deed_index, deed.category, deed.name, deed.colour, deed.rent, deed.mortgage, deed.unmortgage)
				t.grid(row=3, column=(deed.deed_index-7), padx=1, pady=4)
				a.append(t)
			elif 26 > deed.deed_index > 16:
				t = PropertyInfo(self, deed.deed_index, deed.category, deed.name, deed.colour, deed.rent, deed.mortgage, deed.unmortgage)
				t.grid(row=4, column=(deed.deed_index-16), padx=1, pady=4)
				a.append(t)
			else:
				t = PropertyInfo(self, deed.deed_index, deed.category, deed.name, deed.colour, deed.rent, deed.mortgage, deed.unmortgage)
				t.grid(row=5, column=(deed.deed_index-25), padx=1, pady=4)
				a.append(t)


	def info(self):
		self.funds_str.set("Funds: <0000>")#will link to player funds i.e. .format(player.funds)
		self.funds_lbl = Label(self, textvariable = self.funds_str)
		self.funds_lbl.grid(column = 3, columnspan = 3, sticky = N)

		self.parent.d1.set("Die 1: 0")
		self.d1_lbl = Label(self, textvariable = self.parent.d1)
		self.d1_lbl.grid(row=1 ,column=6, padx=4, sticky = N)

		self.parent.d2.set("Die 2: 0")
		self.d1_lbl = Label(self, textvariable = self.parent.d2)
		self.d1_lbl.grid(row =1, column=7, padx=4, sticky = N)


#general divider for UI layout
class Divider(Frame):
	def __init__(self, parent=None, dice=None):
		Frame.__init__(self, parent, bd = 2,)             
		self.parent = parent
		self.dice = dice
		self.d1 = StringVar()
		self.d2 = StringVar()

def main():
	root = Tk()
	root.geometry("1366x700")
	root.configure(bg = "white")

	dice = Dice()
	game_divider = Divider(root) # will occupy left of main window, contains monopoly board
	interface_divider = Divider(root, dice) # will occupy right of main window, contains controls and info

	game_divider.pack(side = LEFT)
	interface_divider.pack(side = BOTTOM)

	board_dim = 700 #this is the side dimension for the monopoly board e.g. 600 x 600 square
	img_path = "centre_img.png"

	#initialise board values
	p_colours = ["magenta", "cyan", "black", "green"]
	pawns = []

	for i in range(0, 4):
		pawns.append(Pawn(i, 0, p_colours[i]))

	tiles = []
	tiles.append(Tile(0, 'go', 'Go'))
	tiles.append(Tile(1, 'property', 'Nubar', 'brown', '60'))
	tiles.append(Tile(2, 'community_chest', 'C. Chest'))
	tiles.append(Tile(3, 'property', 'Larkfield', 'brown', '60'))
	tiles.append(Tile(4, 'tax', 'Inc. Tax', None, '200'))
	tiles.append(Tile(5, 'transport', 'Helix Bus Stop', None, '200'))
	tiles.append(Tile(6, 'property', 'Business School', 'cyan', '100'))
	tiles.append(Tile(7, 'chance', 'Chance'))
	tiles.append(Tile(8, 'property', 'Henry Grattan', 'cyan', '100'))
	tiles.append(Tile(9, 'property', 'T. Larkin Theatre', 'cyan', '100'))
	tiles.append(Tile(10, 'jail', 'Jail'))
	tiles.append(Tile(11, 'property', 'DCU Canteen', 'magenta', '140'))
	tiles.append(Tile(12, 'transport', 'DCU Library', None, '150'))
	tiles.append(Tile(13, 'property', 'Interfaith', 'magenta', '140'))
	tiles.append(Tile(14, 'property', 'Albert College', 'magenta', '160'))
	tiles.append(Tile(15, 'transport', 'St Pats Bus Stop', None, '200'))
	tiles.append(Tile(16, 'property', 'Nursing', 'orange', '180'))
	tiles.append(Tile(17, 'community_chest', 'C. Chest'))
	tiles.append(Tile(18, 'property', 'Lonsdale', 'orange', '180'))
	tiles.append(Tile(19, 'property', 'Estates Office', 'orange', '200'))
	tiles.append(Tile(20, 'free_parking', 'Free Parking'))
	tiles.append(Tile(21, 'property', 'Londis', 'red', '220'))
	tiles.append(Tile(22, 'chance', 'Chance'))
	tiles.append(Tile(23, 'property', 'The U', 'red', '220'))
	tiles.append(Tile(24, 'property', 'Hampstead', 'red', '240'))
	tiles.append(Tile(25, 'transport', 'Ballymun Bus Stop', None, '200'))
	tiles.append(Tile(26, 'property', 'Purcell House', 'yellow', '260'))
	tiles.append(Tile(27, 'transport', 'DCU Sport', None, '150'))
	tiles.append(Tile(28, 'property', 'All Hallows', 'yellow', '260'))
	tiles.append(Tile(29, 'property', 'St Pats', 'yellow', '280'))
	tiles.append(Tile(30, 'goto_jail', 'Go To Jail!'))
	tiles.append(Tile(31, 'property', 'Stokes', 'green', '300'))
	tiles.append(Tile(32, 'property', 'Campus Store', 'green', '300'))
	tiles.append(Tile(33, 'community_chest', 'C. Chest'))
	tiles.append(Tile(34, 'property', 'The Helix', 'green', '320'))
	tiles.append(Tile(35, 'transport', 'Collins Av Bus Stop', None, '200'))
	tiles.append(Tile(36, 'chance', 'Chance'))
	tiles.append(Tile(37, 'property', 'McNulty Build.', 'blue', '350'))
	tiles.append(Tile(38, 'tax', 'Super Tax', None, '100'))
	tiles.append(Tile(39, 'property', 'College Park', 'blue', '400'))

	property_deeds = []
	property_deeds.append(PropertyDeed(0, 'utility', 'DCU Sport', None, '4x Dice Roll', '75'))
	property_deeds.append(PropertyDeed(1, 'utility', 'DCU Library', None, '4x Dice Roll', '75'))
	property_deeds.append(PropertyDeed(2, 'transport', 'Helix Bus Stop', None, '25', '100'))
	property_deeds.append(PropertyDeed(3, 'transport', 'St Pats Bus Stop', None, '25', '100'))
	property_deeds.append(PropertyDeed(4, 'transport', 'Ballymun Bus Stop', None, '25', '100'))
	property_deeds.append(PropertyDeed(5, 'transport', 'Collins Ave. Bus Stop', None, '25', '100'))
	property_deeds.append(PropertyDeed(6, 'property', 'Nubar', 'Brown', '2', '30'))
	property_deeds.append(PropertyDeed(7, 'property', 'Larkfield','Brown', '4', '30'))
	property_deeds.append(PropertyDeed(8, 'property', 'B. School','Cyan', '6', '50'))
	property_deeds.append(PropertyDeed(9, 'property', 'H. Grattan','Cyan', '6', '50'))
	property_deeds.append(PropertyDeed(10, 'property', 'T.L. Theatre','Cyan', '8', '60'))
	property_deeds.append(PropertyDeed(11, 'property', 'DCU Canteen','Magenta', '10', '70'))
	property_deeds.append(PropertyDeed(12, 'property', 'Interfaith','Magenta', '10', '70'))
	property_deeds.append(PropertyDeed(13, 'property', 'Albert College','Magenta', '12', '80'))
	property_deeds.append(PropertyDeed(14, 'property', 'Nursing Build.','Orange', '14', '90'))
	property_deeds.append(PropertyDeed(15, 'property', 'Lonsdale','Orange', '14', '90'))
	property_deeds.append(PropertyDeed(16, 'property', 'Estates','Orange', '16', '100'))
	property_deeds.append(PropertyDeed(17, 'property', 'Londis','Red', '18', '120'))
	property_deeds.append(PropertyDeed(18, 'property', 'The U','Red', '18', '120'))
	property_deeds.append(PropertyDeed(19, 'property', 'Hampstead','Red', '20', '140'))
	property_deeds.append(PropertyDeed(20, 'property', 'Purcell H.','Yellow', '22', '160'))
	property_deeds.append(PropertyDeed(21, 'property', 'All Hallows','Yellow', '22', '160'))
	property_deeds.append(PropertyDeed(22, 'property', 'St Pats','Yellow', '24', '180'))
	property_deeds.append(PropertyDeed(23, 'property', 'Stokes Build.','Green', '26', '200'))
	property_deeds.append(PropertyDeed(24, 'property', 'Campus Store','Green', '26', '200'))
	property_deeds.append(PropertyDeed(25, 'property', 'The Helix','Green', '28', '220'))
	property_deeds.append(PropertyDeed(26, 'property', 'McNulty B.','Blue', '35', '175'))
	property_deeds.append(PropertyDeed(27, 'property', 'The Helix','Blue', '50', '175'))

	board_frame = BoardDisplay(game_divider, board_dim, board_dim, img_path, tiles, pawns)

	controls_frame = Controls(interface_divider, board_frame) #interface_divideHampsteadr = parent, board_frame = internal reference of board for using commands on
	information_frame = Information(interface_divider, property_deeds)

	root.mainloop()

if __name__ == '__main__':
	main()