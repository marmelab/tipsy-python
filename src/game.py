from board import Board
from game_renderer import GameRenderer
from os import system
from os import get_terminal_size
from random import randrange


class Game:

    def __init__(self):
        self.board = Board()
        self.we_have_a_winner = False
        self.current_player = Board.RED if randrange(2) == 0 else Board.BLUE
        self.renderer = GameRenderer()
        self.remaining_turns = 0

    def start(self):
        system('clear')
        self.renderer.display_title()
        while True:
            system('clear')
            self.renderer.display_board(self)
            if self.we_have_a_winner:
                self.renderer.display_winner(self.we_have_a_winner)
                break
            self.renderer.display_instructions()
            self.__roll_dice()
            self.renderer.display_game_infos(self)
            input_command = ''
            while (input_command.lower() not in [Board.EAST, Board.WEST, Board.NORTH, Board.SOUTH]):
                input_command = input(self.renderer.input_message())

            self.__play_command(input_command)
            self.__check_win()
            self.__switch_player_turn()

    def __roll_dice(self):
        if(self.remaining_turns == 0):
            self.remaining_turns = randrange(1, 4)

    def __play_command(self, command):
        fallen_pucks = self.board.tilt(command)
        self.__replace_pucks(fallen_pucks)
        self.remaining_turns -=1

    def __replace_pucks(self, fallen_pucks):
        for puck in filter(lambda color: color != Board.BLACK, fallen_pucks):
            available_nodes = [node for node, attributes in self.board.graph.nodes(
                data=True) if not attributes.get(Board.PUCK_KEY) and not attributes.get(Board.EXIT_KEY)]
            self.board.add_puck(available_nodes[randrange(
                len(available_nodes)-1)], puck, flipped=True)

    def __switch_player_turn(self):
        if (self.remaining_turns > 0):
            return
        if self.current_player == Board.RED:
            self.current_player = Board.BLUE
        else:
            self.current_player = Board.RED

    def __check_win(self):
        if self.board.count_unflip_puck(Board.BLACK) <= 0:
            self.we_have_a_winner = self.current_player
        for color in [Board.BLUE, Board.RED]:
            if self.board.count_unflip_puck(color) <= 0:
                self.we_have_a_winner = color
