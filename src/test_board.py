import unittest
from board import Board


class TestBoard(unittest.TestCase):

    def test_empty_board_should_have_width_x_height_nodes(self):
        # GIVEN
        board = Board()

        # THEN
        self.assertEqual(board.graph.number_of_nodes(),
                         Board.width * Board.height)

    def test_empty_board_left_borders_should_have_no_left_neighbours(self):
        # GIVEN
        board = Board()

        # THEN
        for y in range(Board.height):
            current_node_neighbors = board.graph.neighbors(
                (0, y))
            left_neighbor = (-1, y)

            self.assertNotIn(left_neighbor,
                             current_node_neighbors)

    def test_empty_board_right_borders_should_have_no_right_neighbours(self):
        # GIVEN
        board = Board()

        # THEN
        for y in range(Board.height):
            current_node_neighbors = board.graph.neighbors(
                (Board.width - 1, y))
            right_neighbor = (Board.height, y)

            self.assertNotIn(right_neighbor,
                             current_node_neighbors)

    def test_empty_board_upper_borders_should_have_no_upper_neighbours(self):
        # GIVEN
        board = Board()

        # THEN
        for x in range(Board.width):
            current_node_neighbors = board.graph.neighbors(
                (x, 0))
            northest_neighbor = (x, -1)

            self.assertNotIn(northest_neighbor,
                             current_node_neighbors)

    def test_empty_board_lower_borders_should_have_no_lower_neighbours(self):
        # GIVEN
        board = Board()

        # THEN
        for x in range(Board.width):
            current_node_neighbors = board.graph.neighbors(
                (x, Board.height-1))
            northest_neighbor = (x, Board.height)

            self.assertNotIn(northest_neighbor,
                             current_node_neighbors)


if __name__ == '__main__':
    unittest.main()
