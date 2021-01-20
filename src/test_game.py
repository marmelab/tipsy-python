import unittest
from game import Game


class TestGame(unittest.TestCase):

    def test_empty_board_display_should_display_only_border_and_puck(self):
        # GIVEN
        game = Game()
        expectedBoard = \
"# # # # # # # # # \n" + \
"#       #       # \n" + \
"#   #       #   # \n" + \
"#     #   #     # \n" + \
"# #     o     # # \n" + \
"#     #   #     # \n" + \
"#   #       #   # \n" + \
"#       #       # \n" + \
"# # # # # # # # # "

        # WHEN
        board = game.draw_board()


        # THEN

        self.assertEqual(board, expectedBoard)


if __name__ == '__main__':
    unittest.main()
