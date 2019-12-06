from tkinter import *
from PIL import Image, ImageTk
from board import Tile, Pawn, Board

#general divider for UI layout
class Divider(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent, bd = 2)             
		self.parent = parent

#frames for side tile on board (property, chance, community chest)
#width = parent.parent as it will get width from frame containing parent canvas
class Side1(Frame):
	def __init__(self, parent, category, name=None, colour=None, price=None):
		Frame.__init__(self, parent, width = parent.width * (2/25), height = parent.height * (13/100), highlightthickness = 1, highlightbackground = "black") # correct ratios for side tile size            
		self.parent = parent
		self.width = parent.width * (2/25)
		self.height = parent.height * (13/100)
		self.category = category
		self.name = name
		self.colour = colour
		self.price = price
		self.init_tile()


	def init_tile(self):
		if self.category == "property":
			self.banner = Canvas(self, bg = self.colour, bd = 0)
			self.banner.place(relx=0, rely=0, relwidth=1, relheight=.25)

			self.property_name = Label(self, text = self.name, font = ('Helvetica', 8), justify = CENTER, wraplength = self.width-4, padx=2)
			self.property_name.place(relx=0, rely=.25)

			self.show_pawns = Frame(self)
			self.show_pawns.place(relx=0, rely=.55, relwidth=1, relheight=.10)

			self.property_price = Label(self, text = self.price, font = ('Helvetica', 8))
			self.property_price.place(relx=0, rely=.8)

class Side2(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent, width = parent.parent.width * (13/100), height = parent.height * (2/25), highlightthickness = 1, highlightbackground = "black") # correct ratios for side tile size            
		self.parent = parent

class Side3(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent, width = parent.parent.width * (2/25), height = parent.height * (13/100), highlightthickness = 1, highlightbackground = "black") # correct ratios for side tile size            
		self.parent = parent

class Side4(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent, width = parent.parent.width * (2/25), height = parent.height * (13/100), highlightthickness = 1, highlightbackground = "black") # correct ratios for side tile size            
		self.parent = parent


#frame for corner tile (go to jail, jail, free parking, go)
class Corner(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent, width = parent.width * (13/100), height = parent.height * (13/100), highlightthickness = 1, highlightbackground = "black") # correct ratios for corner tile size            
		self.parent = parent

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
		# self.background_img = ImageTk.PhotoImage(Image.open(image).resize((h, w), Image.ANTIALIAS)) #initialize board image
		self.tiles = tiles
		self.pawns = pawns
		self.init_window()
		self.build_tiles()

	def init_window(self):
		self.pack(fill = BOTH, expand = 1)
		# self.board_canvas = BoardImage(self, self.width, self.height)
		# self.board_canvas.place(x=0, y=0)
		# self.board_canvas.background = self.background_img
		# self.bg = self.board_canvas.create_image(0, 0, anchor=NW, image=self.background_img)

	def find_corner(self, position):
		r = 0
		c = 0
		if position % 9 == 0:
			r = 11
			c = 11
		elif position % 9 == 1:
			r = 11
			c = 1
		elif position % 9 == 2:
			r = 1
			c = 1
		elif position % 9 == 3:
			r = 1
			c = 11

		return r, c

	def build_tiles(self):
		for tile in self.tiles:
			if tile.position % 10 == 0:
				r, c = self.find_corner(tile.position)
				Corner(self).grid(row=r, column=c)
			elif  10 > tile.position > 0:
				Side1(self, tile.category, tile.name, tile.colour, tile.price).grid(row=11, column=11-tile.position)
			else:
				print("oops!")


class Controls(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent, highlightthickness = 2, highlightbackground = "black", bd = 2)             
		self.parent = parent
		self.root = parent.parent
		self.init_window()
		self.buttons()

	def init_window(self):
		self.pack(side = BOTTOM)

	def do_something(self):
		print("Foo")

	def buttons(self):
		default_width = 18

		self.roll = Button(self, text ="ROLL", fg = "black", width = default_width, command = self.do_something)
		self.roll.grid(row=1, column=1)

		self.buy = Button(self, text ="BUY", fg = "black", width = default_width, command = self.do_something)
		self.buy.grid(row=1, column=2)

		self.sell = Button(self, text ="SELL", fg = "black", width = default_width, command = self.do_something)
		self.sell.grid(row=1, column=3)

		self.bail = Button(self, text ="BAIL", fg = "black", width = default_width, command = self.do_something)
		self.bail.grid(row=2, column=1)

		self.buy_house = Button(self, text ="BUY HOUSE/HOTEL", fg = "black", width = default_width, command = self.do_something)
		self.buy_house.grid(row=2, column=2)

		self.mortgage = Button(self, text ="MORTGAGE", fg = "black", width = default_width, command = self.do_something)
		self.mortgage.grid(row=2, column=3)		

		self.abandon = Button(self, text ="ABANDON", fg = "red", width = default_width, command = self.root.destroy)
		self.abandon.grid(row=2, column=4)


class PropertyInfo(Frame):
	def __init__(self, parent=None, board_dimension = 600):
		Frame.__init__(self, parent, width = board_dimension * (2/25), height = board_dimension * (13/100), highlightthickness = 2, highlightbackground = "black", bd = 1) # correct ratios for side tile size            
		self.parent = parent
		self.board_dimension = board_dimension
		self.property_title = "<>" #should point to property object from game.py
		#self.init_card() #problem with header box taking up entire card space...

	def init_card(self):
		self.header = Label(self, text = self.property_title, bg = "grey", width = self.board_dimension * (2/25))
		self.header.pack(side = TOP)

#will contain 9*5 grid
class Information(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent, highlightthickness = 2, highlightbackground = "black", bd = 2)               
		self.parent = parent
		self.funds_str = StringVar()
		self.init_window()
		self.info()
		self.cards()

	def init_window(self):
		self.pack(side = TOP, fill = BOTH)

	def info(self):
		self.funds_str.set("Funds: <0000>")#will link to player funds i.e. .format(player.funds)
		self.funds_lbl = Label(self, textvariable = self.funds_str)
		self.funds_lbl.grid(column = 3, columnspan = 3, sticky = N)

	def cards(self):
		self.utility_00 = PropertyInfo(self)
		self.utility_00.grid(row=2, column=1, padx=1, pady=4)

		self.utility_01 = PropertyInfo(self)
		self.utility_01.grid(row=2, column=2, padx=1, pady=4)

		self.transport_00 = PropertyInfo(self)
		self.transport_00.grid(row=2, column=3, padx=1, pady=4)

		self.transport_01 = PropertyInfo(self)
		self.transport_01.grid(row=2, column=4, padx=1, pady=4)

		self.transport_02 = PropertyInfo(self)
		self.transport_02.grid(row=2, column=5, padx=1, pady=4)

		self.transport_03 = PropertyInfo(self)
		self.transport_03.grid(row=2, column=6, padx=1, pady=4)

		self.property_01 = PropertyInfo(self)
		self.property_01.grid(row=2, column=8, padx=1, pady=4)

		self.property_02 = PropertyInfo(self)
		self.property_02.grid(row=2, column=9, padx=1, pady=4)

		self.property_03 = PropertyInfo(self)
		self.property_03.grid(row=3, column=1, padx=1, pady=4)

		self.property_04 = PropertyInfo(self)
		self.property_04.grid(row=3, column=2, padx=1, pady=4)

		self.property_05 = PropertyInfo(self)
		self.property_05.grid(row=3, column=3, padx=1, pady=4)

		self.property_06 = PropertyInfo(self)
		self.property_06.grid(row=3, column=4, padx=1, pady=4)

		self.property_07 = PropertyInfo(self)
		self.property_07.grid(row=3, column=5, padx=1, pady=4)

		self.property_08 = PropertyInfo(self)
		self.property_08.grid(row=3, column=6, padx=1, pady=4)

		self.property_09 = PropertyInfo(self)
		self.property_09.grid(row=3, column=7, padx=1, pady=4)

		self.property_10 = PropertyInfo(self)
		self.property_10.grid(row=3, column=8, padx=1, pady=4)

		self.property_11 = PropertyInfo(self)
		self.property_11.grid(row=3, column=9, padx=1, pady=4)

		self.property_12 = PropertyInfo(self)
		self.property_12.grid(row=4, column=1, padx=1, pady=4)

		self.property_13 = PropertyInfo(self)
		self.property_13.grid(row=4, column=2, padx=1, pady=4)

		self.property_14 = PropertyInfo(self)
		self.property_14.grid(row=4, column=3, padx=1, pady=4)

		self.property_15 = PropertyInfo(self)
		self.property_15.grid(row=4, column=4, padx=1, pady=4)

		self.property_16 = PropertyInfo(self)
		self.property_16.grid(row=4, column=5, padx=1, pady=4)

		self.property_17 = PropertyInfo(self)
		self.property_17.grid(row=4, column=6, padx=1, pady=4)

		self.property_18 = PropertyInfo(self)
		self.property_18.grid(row=4, column=7, padx=1, pady=4)

		self.property_19 = PropertyInfo(self)
		self.property_19.grid(row=4, column=8, padx=1, pady=4)

		self.property_20 = PropertyInfo(self)
		self.property_20.grid(row=4, column=9, padx=1, pady=4)

		self.property_21 = PropertyInfo(self)
		self.property_21.grid(row=5, column=1, padx=1, pady=4)

		self.property_22 = PropertyInfo(self)
		self.property_22.grid(row=5, column=2, padx=1, pady=4)


def main():
	root = Tk()
	root.geometry("1366x680")

	game_frame = Divider(root) # will occupy left of main window, contains monopoly board
	interface_frame = Divider(root) # will occupy right of main window, contains controls and info

	game_frame.pack(side = LEFT)
	interface_frame.pack(side = BOTTOM)

	board_dim = 680 #this is the side dimension for the monopoly board e.g. 600 x 600 square
	img_path = "board.png"

	#initialise board values
	p_colours = ["magenta", "cyan", "black", "green"]
	pawns = {}

	for i in range(0, 4):
		pawns[i] = Pawn(i, 0, p_colours[i])

	tiles = []
	tiles.append(Tile(0, 'go', 'Go'))
	tiles.append(Tile(1, 'property', 'Nubar', 'brown', '60'))
	tiles.append(Tile(2, 'community_chest', 'Community Chest'))
	tiles.append(Tile(3, 'property', 'Larkfield', 'brown', '60'))
	tiles.append(Tile(4, 'tax', 'Income Tax', None, '200'))
	tiles.append(Tile(5, 'transport', 'Helix Bus Stop', None, '200'))
	tiles.append(Tile(6, 'property', 'Business School', 'cyan', '100'))
	tiles.append(Tile(7, 'chance', 'Chance'))
	tiles.append(Tile(8, 'property', 'Business School', 'cyan', '100'))
	tiles.append(Tile(9, 'property', 'Business School', 'cyan', '100'))
	tiles.append(Tile(10, 'jail', 'Jail'))

	board_frame = BoardDisplay(game_frame, board_dim, board_dim, img_path, tiles)
	controls_frame = Controls(interface_frame)
	information_frame = Information(interface_frame)

	root.mainloop()

if __name__ == '__main__':
	main()