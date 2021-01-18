import unittest
from board import Board


class TestBoard(unittest.TestCase):

    def test_empty_board_should_have_49_nodes(self):
        board = Board()
        self.assertEqual(board.graph.number_of_nodes(), 49)

    def test_empty_board_upper_borders_should_have_no_upper_neighbours(self):
        board = Board()
        # up border
        for y in range(7):
            print(y)
            print(board.graph.has_node((0, y)))
        # down border


if __name__ == '__main__':
    unittest.main()
