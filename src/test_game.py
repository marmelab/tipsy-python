import unittest
import re
from game import Game
from board import Board


class TestGame(unittest.TestCase):

    def remove_colors_tag(self, text):
        # in order remove colors tags, using regex, taken from : https://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python
        return re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])').sub('', text)

    def test_board_display_should_display_starting_board(self):
        # GIVEN
        game = Game()
        expected_board = \
            "# #   # # # # # # \n" + \
            "#       #       # \n" + \
            "#   # O   O #     \n" + \
            "#   0 # 0 # 0   # \n" + \
            "# #   O 0 O   # # \n" + \
            "#   0 # 0 # 0   # \n" + \
            "    # O   O #   # \n" + \
            "#       #       # \n" + \
            "# # # # # #   # # "

        # WHEN
        board = self.remove_colors_tag(game.renderer.draw_board(game))

        # THEN
        self.assertEqual(board, expected_board)

    def test_when_black_puck_fall_of_the_board_current_player_should_win(self):
        # GIVEN
        # # # # #
        # O     #
        #   *
        #     0 #
        # # # # #
        game = Game()
        board = Board(3, 3, obstacles=[], pucks={
                      Board.BLACK: [(1, 1)],Board.BLUE:[(0,0)],Board.RED:[(2,2)]}, exits=[(3, 1)])
        game.current_player = Board.BLUE
        game.board = board

        # WHEN
        game._Game__play_command(Board.EAST)
        game._Game__check_win()

        # THEN
        self.assertEqual(game.we_have_a_winner, Board.BLUE)

    def test_when_all_blue_pucks_fall_of_the_board_blue_player_should_win(self):
        # GIVEN
        # # # # #   0 : blue
        # *     #   O : red
        # O 0       * : black
        #       #
        # # # # #
        game = Game()
        board = Board(3, 3, obstacles=[], pucks={
                      Board.BLUE: [(1, 1)], Board.RED: [(2, 0)], Board.BLACK: [(0, 0)]}, exits=[(3, 1)])
        game.board = board
        print()
        print(game.renderer.draw_board(game))

        # WHEN
        game._Game__play_command(Board.EAST)
        game._Game__check_win()

        # THEN
        self.assertEqual(game.we_have_a_winner, Board.BLUE)


    def test_when_all_red_pucks_fall_of_the_board_blue_player_should_win(self):
        # GIVEN
        # # # # #   0 : blue
        # *     #   O : red
        # 0 O       * : black
        #       #
        # # # # #
        game = Game()
        board = Board(3, 3, obstacles=[], pucks={
                      Board.RED: [(1, 1)], Board.BLUE: [(2, 0)], Board.BLACK: [(0, 0)]}, exits=[(3, 1)])
        game.board = board
        print()
        print(game.renderer.draw_board(game))

        # WHEN
        game._Game__play_command(Board.EAST)
        game._Game__check_win()

        # THEN
        self.assertEqual(game.we_have_a_winner, Board.RED)


if __name__ == '__main__':
    unittest.main()
