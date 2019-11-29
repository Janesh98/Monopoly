from tkinter import *

#general divider for UI layout
class Divider(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent, bd = 2)             
		self.parent = parent

#frames for side tile on board (property, chance, community chest)
class Side1(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent, width = parent.width * (2/25), height = parent.height * (13/100), highlightthickness = 2, highlightbackground = "black") # correct ratios for side tile size            
		self.parent = parent

class Side2(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent, width = parent.width * (13/100), height = parent.height * (2/25), highlightthickness = 2, highlightbackground = "black") # correct ratios for side tile size            
		self.parent = parent

#frame for corner tile (go to jail, jail, free parking, go)
class Corner(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent, width = parent.width * (13/100), height = parent.height * (13/100), highlightthickness = 2, highlightbackground = "black") # correct ratios for corner tile size            
		self.parent = parent

#Board will contain 11*11 grid
class Board(Frame):
	def __init__(self, parent=None, w=None, h=None):
		Frame.__init__(self, parent, width=w, height=h, bd = 2, highlightthickness = 2, highlightbackground = "black")              
		self.parent = parent
		self.width = w
		self.height = h
		self.init_window()
		self.setup()

	def init_window(self):
		self.pack(fill = BOTH, expand = 1)

	def setup(self):
		# i = 40
		# r = 11
		# c = 11
		# while i > 0:
		# 	if i % 10 == 0:
		# 		self.new_tile = Corner(self)
		# 		self.new_tile.grid(row=r, column=c)

		# 		if c > 0 and r == 11:
		# 			c -= 1
		# 		elif c == 0 and r > 0:
		# 			r -= 1
		# 		elif c < 11 and r == 0:
		# 			c += 1
		# 		else:
		# 			r += 1
		# 	else:
		# 		self.new_tile = Side(self)
		# 		self.new_tile.grid(row=r, column=c)

		# 		if c > 0 and r == 11:
		# 			c -= 1
		# 		elif c == 0 and r > 0:
		# 			r -= 1
		# 		elif c < 11 and r == 0:
		# 			c += 1
		# 		else:
		# 			r += 1

		# 	i -= 1

	#Bottom side of board
		self.tile_00 = Corner(self)
		self.tile_00.grid(row=11, column=11)

		self.tile_01 = Side1(self)
		self.tile_01.grid(row=11, column=10)

		self.tile_02 = Side1(self)
		self.tile_02.grid(row=11, column=9)

		self.tile_03 = Side1(self)
		self.tile_03.grid(row=11, column=8)

		self.tile_04 = Side1(self)
		self.tile_04.grid(row=11, column=7)

		self.tile_05 = Side1(self)
		self.tile_05.grid(row=11, column=6)

		self.tile_06 = Side1(self)
		self.tile_06.grid(row=11, column=5)

		self.tile_07 = Side1(self)
		self.tile_07.grid(row=11, column=4)

		self.tile_08 = Side1(self)
		self.tile_08.grid(row=11, column=3)

		self.tile_09 = Side1(self)
		self.tile_09.grid(row=11, column=2)

		self.tile_10 = Corner(self)
		self.tile_10.grid(row=11, column=1)


	#Left side of board
		self.tile_11 = Side2(self)
		self.tile_11.grid(row=10, column=1)

		self.tile_12 = Side2(self)
		self.tile_12.grid(row=9, column=1)

		self.tile_13 = Side2(self)
		self.tile_13.grid(row=8, column=1)

		self.tile_14 = Side2(self)
		self.tile_14.grid(row=7, column=1)

		self.tile_15 = Side2(self)
		self.tile_15.grid(row=6, column=1)

		self.tile_16 = Side2(self)
		self.tile_16.grid(row=5, column=1)

		self.tile_17 = Side2(self)
		self.tile_17.grid(row=4, column=1)

		self.tile_18 = Side2(self)
		self.tile_18.grid(row=3, column=1)

		self.tile_19 = Side2(self)
		self.tile_19.grid(row=2, column=1)

		self.tile_20 = Corner(self)
		self.tile_20.grid(row=1, column=1)

	#Top side of board
		self.tile_21 = Side1(self)
		self.tile_21.grid(row=1, column=2)

		self.tile_22 = Side1(self)
		self.tile_22.grid(row=1, column=3)

		self.tile_23 = Side1(self)
		self.tile_23.grid(row=1, column=4)

		self.tile_24 = Side1(self)
		self.tile_24.grid(row=1, column=5)

		self.tile_25 = Side1(self)
		self.tile_25.grid(row=1, column=6)

		self.tile_26 = Side1(self)
		self.tile_26.grid(row=1, column=7)

		self.tile_27 = Side1(self)
		self.tile_27.grid(row=1, column=8)

		self.tile_28 = Side1(self)
		self.tile_28.grid(row=1, column=9)

		self.tile_29 = Side1(self)
		self.tile_29.grid(row=1, column=10)

		self.tile_30 = Corner(self)
		self.tile_30.grid(row=1, column=11)

	#Right side of board
		self.tile_31 = Side2(self)
		self.tile_31.grid(row=2, column=11)

		self.tile_32 = Side2(self)
		self.tile_32.grid(row=3, column=11)

		self.tile_33 = Side2(self)
		self.tile_33.grid(row=4, column=11)

		self.tile_34 = Side2(self)
		self.tile_34.grid(row=5, column=11)

		self.tile_35 = Side2(self)
		self.tile_35.grid(row=6, column=11)

		self.tile_36 = Side2(self)
		self.tile_36.grid(row=7, column=11)

		self.tile_37 = Side2(self)
		self.tile_37.grid(row=8, column=11)

		self.tile_38 = Side2(self)
		self.tile_38.grid(row=9, column=11)

		self.tile_39 = Side2(self)
		self.tile_39.grid(row=10, column=11)


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
	root.geometry("1300x600")

	game_frame = Divider(root) # will occupy left of main window, contains monopoly board
	interface_frame = Divider(root) # will occupy right of main window, contains controls and info

	game_frame.pack(side = LEFT)
	interface_frame.pack(side = BOTTOM)

	board_frame = Board(game_frame, 600, 600)
	controls_frame = Controls(interface_frame)
	information_frame = Information(interface_frame)

	root.mainloop()

if __name__ == '__main__':
	main()