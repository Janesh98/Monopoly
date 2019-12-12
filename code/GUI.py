from tkinter import *
from PIL import Image, ImageTk
from board import Tile, Pawn, Board, Dice
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
    def __init__(self, parent, board, client = None):
        Frame.__init__(self, parent, highlightthickness = 2, highlightbackground = "black", bd = 2)
        self.parent = parent
        self.root = parent.parent
        self.board = board
        self.dice = parent.dice
        self.init_window()
        self.buttons()
        self.client = client    #parent client

    def init_window(self):
        self.pack(side = BOTTOM)

    def do_something(self):
        self.client.send_server("foo")
    '''
    def roll_com(self):
        d1, d2 = self.dice.roll()
        self.parent.d1.set("Die 1: {}".format(d1))
        self.parent.d2.set("Die 2: {}".format(d2))
        print("Rolled {}:{}".format(d1, d2))
        n = d1 + d2
        self.board.pawns[0].move(n)
        for d_tile in self.board.display_tiles:
            d_tile.show_pawn()
    '''
    #process command from server
    def process(self, command):
        tokens = command.strip().split()

        if tokens[0] == "roll":
            self.display_dice(int(tokens[1]),int(tokens[2]))
        elif tokens[0].isdigit():
            if tokens[1] == "move":
                # move pawn by int
                self.board.pawns[0].move(int(tokens[2]))
                for d_tile in self.board.display_tiles:
                    d_tile.show_pawn()

    #sends a request for a roll to server
    def request_roll(self):
        self.client.send_server("roll")

    #displays roll sent by server
    def display_dice(self, d1, d2):
        self.parent.d1.set("Die 1: {}".format(d1))
        self.parent.d2.set("Die 2: {}".format(d2))

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

    def abandon(self):
        self.client.send_server("quit")
        self.root.destroy()

    def buttons(self):
        default_width = 18

        self.roll = Button(self, text ="ROLL", fg = "black", width = default_width, command = self.request_roll)
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

        self.abandon = Button(self, text ="ABANDON", fg = "red", width = default_width, command = self.abandon)
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
    def __init__(self, parent=None, dice=None):
        Frame.__init__(self, parent, highlightthickness = 2, highlightbackground = "black", bd = 2)               
        self.parent = parent
        self.dice = parent.dice
        self.funds_str = StringVar()
        self.d1 = parent.d1
        self.d2 = parent.d2
        self.init_window()
        self.info()
        self.cards()

    def init_window(self):
        self.pack(side = TOP, fill = BOTH)

    def info(self):
        self.funds_str.set("Funds: <0000>")#will link to player funds i.e. .format(player.funds)
        self.funds_lbl = Label(self, textvariable = self.funds_str)
        self.funds_lbl.grid(column = 3, columnspan = 3, sticky = N)

        self.parent.d1.set("Die 1: 0")
        self.d1_lbl = Label(self, textvariable = self.parent.d1)
        self.d1_lbl.grid(row=1 ,column=14, padx=4, sticky = N)

        self.parent.d2.set("Die 2: 0")
        self.d1_lbl = Label(self, textvariable = self.parent.d2)
        self.d1_lbl.grid(row =1, column=15, padx=4, sticky = N)

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


#general divider for UI layout
class Divider(Frame):
    def __init__(self, parent=None, dice=None):
        Frame.__init__(self, parent, bd = 2,)             
        self.parent = parent
        self.dice = dice
        self.d1 = StringVar()
        self.d2 = StringVar()

def main(parent=None):
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

    board_frame = BoardDisplay(game_divider, board_dim, board_dim, img_path, tiles, pawns)
    
    #interface_divider = parent, board_frame = internal reference of board for using commands on
    controls_frame = Controls(interface_divider, board_frame, parent)
    parent.ui_controls = controls_frame
    information_frame = Information(interface_divider)

    root.mainloop()

if __name__ == '__main__':
    main()
