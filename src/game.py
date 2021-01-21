from board import Board
from os import system


class Game:
    OBSTACLE = '# '
    EXIT = '  '
    PUCK = {Board.RED:'O ',Board.BLUE:'0 ', Board.BLACK:'* '}

    def __init__(self):
        self.pucks = 1
        self.board = Board()

    def start(self):
        system('clear')
        self.display_title()
        while True:
            system('clear')
            print(self.draw_board())
            if self.__check_win():
                self.__display_winner()
                break
            self.display_instructions()
            input_command = ''
            while (input_command.lower() not in [Board.EAST, Board.WEST, Board.NORTH, Board.SOUTH]):
                input_command = input('Use ' + Board.NORTH + ', ' + Board.SOUTH +
                                      ', ' + Board.EAST + ', ' + Board.WEST + ' to tilt the board: ')

            fallen_pucks = self.board.tilt(input_command)
            self.pucks -= fallen_pucks


    def __check_win(self):
        return self.pucks <= 0

    def __display_winner(self):
        print("oooooo   oooo                                            o8o              .o.")
        print(" `888.   .8'                                             `\"'              888")
        print("  `888. .8'    .ooooo.  oooo  oooo     oooo oooo    ooo oooo  ooo. .oo.   888")
        print("   `888.8'    d88' `88b `888  `888      `88. `88.  .8'  `888  `888P\"Y88b  Y8P")
        print("    `888'     888   888  888   888       `88..]88..8'    888   888   888  `8'")
        print("     888      888   888  888   888        `888'`888'     888   888   888  .o.")
        print("    o888o     `Y8bod8P'  `V88V\"V8P'        `8'  `8'     o888o o888o o888o Y8P")

    def draw_board(self):
        board = Game.OBSTACLE
        for i in range(self.board.WIDTH):
            if self.board.graph.has_node((i, -1)) and self.board.graph.nodes[(i, -1)].get(Board.EXIT_KEY):
                board += Game.EXIT
            else:
                board += Game.OBSTACLE
        board += '# \n'
        for j in range(self.board.HEIGHT):
            if self.board.graph.has_node((-1, j)) and self.board.graph.nodes[(-1, j)].get(Board.EXIT_KEY):
                board += Game.EXIT
            else:
                board += Game.OBSTACLE
            for i in range(self.board.WIDTH):
                if (not self.board.graph.has_node((i, j))):
                    board += Game.OBSTACLE
                elif (self.board.graph.nodes[(i, j)].get(Board.PUCK_KEY)):
                    board += Game.PUCK[self.board.graph.nodes[(i, j)].get(Board.PUCK_KEY)]
                else:
                    board += '  '
            if self.board.graph.has_node((self.board.WIDTH, j)) and self.board.graph.nodes[(self.board.WIDTH, j)].get(Board.EXIT_KEY):
                board += Game.EXIT
            else:
                board += Game.OBSTACLE
            board += '\n'
        board += Game.OBSTACLE
        for i in range(self.board.WIDTH):
            if self.board.graph.has_node((i, self.board.HEIGHT)) and self.board.graph.nodes[(i, self.board.HEIGHT)].get(Board.EXIT_KEY):
                board += Game.EXIT
            else:
                board += Game.OBSTACLE
        board += '# '
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
