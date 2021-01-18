import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def test_empty_board_should_have_49_nodes(self):
        board=Board()
        self.assertEqual(board.graph.number_of_nodes(), 49)


if __name__ == '__main__':
    unittest.main()