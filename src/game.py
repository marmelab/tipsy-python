from board import Board
from os import system


class Game:
    def __init__(self):
        self.board = Board()

    def start(self):
        system('clear')
        self.display_title()
        while True:
            system('clear')
            self.display_board()
            self.display_instructions()
            input_command = ''
            while (input_command.lower() not in [Board.EAST, Board.WEST, Board.NORTH, Board.SOUTH]):
                input_command = input('Use ' + Board.NORTH + ', ' + Board.SOUTH +
                                      ', ' + Board.EAST + ', ' + Board.WEST + ' to tilt the board: ')
            print('move to ' + input_command)

            self.board.tilt(input_command)

    def display_board(self):
        print('# '*(self.board.WIDTH+2))
        for j in range(self.board.HEIGHT):
            line = '# '
            for i in range(self.board.WIDTH):
                if (self.board.graph.nodes[(i, j)].get('puck')):
                    line += 'o '
                elif (self.board.graph.nodes[(i, j)].get('obstacle')):
                    line += '# '
                else:
                    line += '  '
            line += '#'
            print(line)
        print('# '*(self.board.WIDTH+2))

    def display_title(self):
        print("    .    o8o")
        print("  .o8    `\"'")
        print(".o888oo oooo  oo.ooooo.   .oooo.o oooo    ooo")
        print("  888   `888   888' `88b d88(  \"8  `88.  .8'")
        print("  888    888   888   888 `\"Y88b.    `88..8'")
        print("  888 .  888   888   888 o.  )88b    `888'")
        print("  \"888\" o888o  888bod8P' 8\"\"888P'     .8'")
        print("               888                .o..P'")
        print("              o888o               `Y8P'")
        print("")
        print("")
        input("Welcome to Tipsy game. Type Enter to start")

    def display_instructions(self):
        print("     ^")
        print("     n")
        print(" < w * e >")
        print("     s")
        print("     v")
