from board import Board
from game_renderer import GameRenderer
from os import system
from os import get_terminal_size


class Game:


    def __init__(self):
        self.board = Board()
        self.we_have_a_winner = False
        self.current_player = Board.RED
        self.renderer = GameRenderer()

    def start(self):
        system('clear')
        self.renderer.display_title()
        while True:
            system('clear')
            self.renderer.display_board(self);
            if self.we_have_a_winner:
                self.renderer.display_winner(self.we_have_a_winner)
                break
            self.renderer.display_game_infos(self)
            self.renderer.display_instructions()
            input_command = ''
            while (input_command.lower() not in [Board.EAST, Board.WEST, Board.NORTH, Board.SOUTH]):
                input_command = input(self.renderer.input_message())

            self.__play_command(input_command)
            self.__check_win()
            self.__switch_player_turn()

    def __play_command(self, command):
        self.board.tilt(command)

    def __switch_player_turn(self):
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
