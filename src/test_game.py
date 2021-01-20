import unittest
from game import Game


class TestGame(unittest.TestCase):

    def test_board_display_should_display_starting_board(self):
        # GIVEN
        game = Game()
        expected_board = \
"# #   # # # # # # \n" + \
"#       #       # \n" + \
"#   #       #     \n" + \
"#     #   #       \n" + \
"# #     o     # # \n" + \
"#     #   #     # \n" + \
"    #       #   # \n" + \
"#       #       # \n" + \
"# # # # # #   # # "

        # WHEN
        board = game.draw_board()


        # THEN
        self.assertEqual(board, expected_board)


if __name__ == '__main__':
    unittest.main()
