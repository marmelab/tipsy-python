from board import Board
from os import system


class Game:
    OBSTACLE = '# '
    PUCK = 'o '
    def __init__(self):
        self.board = Board()

    def start(self):
        system('clear')
        self.display_title()
        while True:
            system('clear')
            print(self.draw_board())
            self.display_instructions()
            input_command = ''
            while (input_command.lower() not in [Board.EAST, Board.WEST, Board.NORTH, Board.SOUTH]):
                input_command = input('Use ' + Board.NORTH + ', ' + Board.SOUTH +
                                      ', ' + Board.EAST + ', ' + Board.WEST + ' to tilt the board: ')

            self.board.tilt(input_command)

    def draw_board(self):
        board = Game.OBSTACLE*(self.board.WIDTH+2)+'\n'
        for j in range(self.board.HEIGHT):
            board += Game.OBSTACLE
            for i in range(self.board.WIDTH):
                if (not self.board.graph.has_node((i, j))):
                    board += Game.OBSTACLE
                elif (self.board.graph.nodes[(i, j)].get('puck')):
                    board += Game.PUCK
                else:
                    board += '  '
            board += Game.OBSTACLE + '\n'
        board += Game.OBSTACLE*(self.board.WIDTH+2)
        return board

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
