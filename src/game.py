from board import Board
from os import system
from os import get_terminal_size


class Game:
    TOP_PADDING = int(get_terminal_size()[1]*0.20)
    LEFT_PADING = int((get_terminal_size()[0]-50) / 2)
    WHITE_BG = '\033[47m'
    GREY_BG = '\033[47m'
    END_COLOR = '\033[0m'
    OBSTACLE = WHITE_BG + '# ' + END_COLOR
    EXIT = WHITE_BG + '  ' + END_COLOR
    EMPTY_CELL = WHITE_BG + '  ' + END_COLOR
    PUCK = {Board.RED: WHITE_BG + '\033[31mO ' + END_COLOR,
            Board.BLUE: WHITE_BG + '\033[34m0 ' + END_COLOR,
            Board.BLACK: WHITE_BG + '\033[90m0 ' + END_COLOR}

    def __init__(self):
        self.board = Board()
        self.we_have_a_winner = False
        self.current_player = Board.RED
        self.pucks = {Board.RED: 6, Board.BLUE: 6, Board.BLACK: 1}

    def start(self):
        system('clear')
        self.display_title()
        while True:
            system('clear')

            print('\n' * Game.TOP_PADDING)
            for line in self.draw_board().split('\n'):
                print(' ' * Game.LEFT_PADING + line)

            if self.we_have_a_winner:
                self.__display_winner(self.we_have_a_winner)
                break
            self.display_game_infos()
            self.display_instructions()
            input_command = ''
            while (input_command.lower() not in [Board.EAST, Board.WEST, Board.NORTH, Board.SOUTH]):
                input_command = input(' ' * Game.LEFT_PADING + 'Use ' + Board.NORTH + ', ' + Board.SOUTH +
                                      ', ' + Board.EAST + ', ' + Board.WEST + ' to tilt the board: ')

            self.__play_command(input_command)
            self.__check_win()
            self.__switch_player_turn()

    def __play_command(self, command):
        fallen_pucks = self.board.tilt(command)
        self.__update_pucks(fallen_pucks)

    def __switch_player_turn(self):
        if self.current_player == Board.RED:
            self.current_player = Board.BLUE
        else:
            self.current_player = Board.RED

    def __update_pucks(self, fallen_pucks):
        for color in fallen_pucks:
            self.pucks[color] -= 1

    def __check_win(self):
        if self.pucks.get(Board.BLACK) <= 0:
            self.we_have_a_winner = self.current_player
        for color in [Board.BLUE, Board.RED]:
            if self.pucks.get(color) <= 0:
                self.we_have_a_winner = color

    def __display_winner(self, winner):
        print(Game.LEFT_PADING*' ' + winner +
              " won the game! Congrats to the winner!")

    def draw_board(self):
        board = Game.OBSTACLE
        for i in range(self.board.WIDTH):
            if self.board.graph.has_node((i, -1)) and self.board.graph.nodes[(i, -1)].get(Board.EXIT_KEY):
                board += Game.EXIT
            else:
                board += Game.OBSTACLE
        board += Game.OBSTACLE + '\n'
        for j in range(self.board.HEIGHT):
            if self.board.graph.has_node((-1, j)) and self.board.graph.nodes[(-1, j)].get(Board.EXIT_KEY):
                board += Game.EXIT
            else:
                board += Game.OBSTACLE
            for i in range(self.board.WIDTH):
                if (not self.board.graph.has_node((i, j))):
                    board += Game.OBSTACLE
                elif (self.board.graph.nodes[(i, j)].get(Board.PUCK_KEY)):
                    board += Game.PUCK[self.board.graph.nodes[(
                        i, j)].get(Board.PUCK_KEY)]
                else:
                    board += Game.EMPTY_CELL
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
        board += Game.OBSTACLE
        return board

    def display_title(self):
        print('\n' * Game.TOP_PADDING)
        print(' ' * Game.LEFT_PADING + "    .    o8o")
        print(' ' * Game.LEFT_PADING + "  .o8    `\"'")
        print(' ' * Game.LEFT_PADING +
              ".o888oo oooo  oo.ooooo.   .oooo.o oooo    ooo")
        print(' ' * Game.LEFT_PADING +
              "  888   `888   888' `88b d88(  \"8  `88.  .8'")
        print(' ' * Game.LEFT_PADING +
              "  888    888   888   888 `\"Y88b.    `88..8'")
        print(' ' * Game.LEFT_PADING +
              "  888 .  888   888   888 o.  )88b    `888'")
        print(' ' * Game.LEFT_PADING +
              "  \"888\" o888o  888bod8P' 8\"\"888P'     .8'")
        print(' ' * Game.LEFT_PADING + "               888                .o..P'")
        print(' ' * Game.LEFT_PADING + "              o888o               `Y8P'")
        print(' ' * Game.LEFT_PADING + "")
        print(' ' * Game.LEFT_PADING + "")
        input(' ' * Game.LEFT_PADING +
              "Welcome to Tipsy game. Type Enter to start")

    def display_instructions(self):
        print(' ' * Game.LEFT_PADING + "     ^")
        print(' ' * Game.LEFT_PADING + "     n")
        print(' ' * Game.LEFT_PADING + " < w * e >")
        print(' ' * Game.LEFT_PADING + "     s")
        print(' ' * Game.LEFT_PADING + "     v")

    def display_game_infos(self):
        print(' ' * Game.LEFT_PADING + '')
        print(' ' * Game.LEFT_PADING + 'it\'s '+self.current_player+' turn...')
