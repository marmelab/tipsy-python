import unittest
from board import Board


class TestBoard(unittest.TestCase):

    def test_empty_board_should_have_width_x_height_nodes(self):
        # GIVEN
        board = Board()

        # THEN
        self.assertEqual(board.graph.number_of_nodes(),
                         board.WIDTH * board.HEIGHT)

    def test_empty_board_left_borders_should_have_no_left_neighbours(self):
        # GIVEN
        board = Board()

        # THEN
        for y in range(board.HEIGHT):
            current_node_neighbors = board.graph.neighbors(
                (0, y))
            left_neighbor = (-1, y)

            self.assertNotIn(left_neighbor,
                             current_node_neighbors)

    def test_empty_board_right_borders_should_have_no_right_neighbours(self):
        # GIVEN
        board = Board()

        # THEN
        for y in range(board.HEIGHT):
            current_node_neighbors = board.graph.neighbors(
                (board.WIDTH - 1, y))
            right_neighbor = (board.HEIGHT, y)

            self.assertNotIn(right_neighbor,
                             current_node_neighbors)

    def test_empty_board_upper_borders_should_have_no_upper_neighbours(self):
        # GIVEN
        board = Board()

        # THEN
        for x in range(board.WIDTH):
            current_node_neighbors = board.graph.neighbors(
                (x, 0))
            northest_neighbor = (x, -1)

            self.assertNotIn(northest_neighbor,
                             current_node_neighbors)

    def test_empty_board_lower_borders_should_have_no_lower_neighbours(self):
        # GIVEN
        board = Board()

        # THEN
        for x in range(board.WIDTH):
            current_node_neighbors = board.graph.neighbors(
                (x, board.HEIGHT-1))
            northest_neighbor = (x, board.HEIGHT)

            self.assertNotIn(northest_neighbor,
                             current_node_neighbors)

    def test_empty_board_middle_node_should_have_upper_lower_right_and_left_neighbours(self):
        # GIVEN
        board = Board(3, 3)

        # THEN
        middle_node = (1, 1)
        east_node = (2, 1)
        south_node = (1, 2)
        west_node = (0, 1)
        north_node = (1, 0)

        self.assertEqual(board.graph[middle_node][east_node]["direction"], Board.EAST)
        self.assertEqual(board.graph[middle_node][south_node]["direction"], Board.SOUTH)
        self.assertEqual(board.graph[middle_node][west_node]["direction"], Board.WEST)
        self.assertEqual(board.graph[middle_node][north_node]["direction"], Board.NORTH)

if __name__ == '__main__':
    unittest.main()
