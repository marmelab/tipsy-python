import unittest
from board import Board


class TestBoard(unittest.TestCase):

    def test_empty_board_should_have_width_x_height_nodes(self):
        # GIVEN
        board = Board(obstacles=[])

        # THEN
        self.assertEqual(board.graph.number_of_nodes(),
                         board.WIDTH * board.HEIGHT)

    def test_node_with_puck_on_it_should_have_puck_attribute(self):
        # GIVEN
        board = Board(obstacles=[])
        known_node_with_puck = (board.WIDTH//2, board.HEIGHT//2)

        # THEN
        nodes_with_puck_attribute = [node for node, data in board.graph.nodes(
            data=True) if data.get('puck')]
        self.assertIn(known_node_with_puck, nodes_with_puck_attribute)

    def test_node_without_puck_on_it_should_not_have_puck_attribute(self):
        # GIVEN
        board = Board(obstacles=[])
        known_node_with_puck = (board.WIDTH//2, board.HEIGHT//2)

        # THEN
        nodes_with_no_puck_attribute = [node for node, data in board.graph.nodes(
            data=True) if not data.get('puck')]
        self.assertNotIn(known_node_with_puck, nodes_with_no_puck_attribute)

    def test_empty_board_left_borders_should_have_no_left_neighbours(self):
        # GIVEN
        board = Board(obstacles=[])

        # THEN
        for y in range(board.HEIGHT):
            current_node_neighbors = board.graph.neighbors(
                (0, y))
            left_neighbor = (-1, y)

            self.assertNotIn(left_neighbor,
                             current_node_neighbors)

    def test_empty_board_right_borders_should_have_no_right_neighbours(self):
        # GIVEN
        board = Board(obstacles=[])

        # THEN
        for y in range(board.HEIGHT):
            current_node_neighbors = board.graph.neighbors(
                (board.WIDTH - 1, y))
            right_neighbor = (board.HEIGHT, y)

            self.assertNotIn(right_neighbor,
                             current_node_neighbors)

    def test_empty_board_upper_borders_should_have_no_upper_neighbours(self):
        # GIVEN
        board = Board(obstacles=[])

        # THEN
        for x in range(board.WIDTH):
            current_node_neighbors = board.graph.neighbors(
                (x, 0))
            northest_neighbor = (x, -1)

            self.assertNotIn(northest_neighbor,
                             current_node_neighbors)

    def test_empty_board_lower_borders_should_have_no_lower_neighbours(self):
        # GIVEN
        board = Board(obstacles=[])

        # THEN
        for x in range(board.WIDTH):
            current_node_neighbors = board.graph.neighbors(
                (x, board.HEIGHT-1))
            northest_neighbor = (x, board.HEIGHT)

            self.assertNotIn(northest_neighbor,
                             current_node_neighbors)

    def test_empty_board_middle_node_should_have_upper_lower_right_and_left_neighbours(self):
        # GIVEN
        board = Board(3, 3, obstacles=[])

        # THEN
        middle_node = (1, 1)
        east_node = (2, 1)
        south_node = (1, 2)
        west_node = (0, 1)
        north_node = (1, 0)

        self.assertEqual(board.graph[middle_node]
                         [east_node]["direction"], Board.EAST)
        self.assertEqual(board.graph[middle_node]
                         [south_node]["direction"], Board.SOUTH)
        self.assertEqual(board.graph[middle_node]
                         [west_node]["direction"], Board.WEST)
        self.assertEqual(board.graph[middle_node]
                         [north_node]["direction"], Board.NORTH)

    def test_get_next_right_free_node(self):
        # GIVEN
        board = Board(obstacles=[])
        expected_puck_position = (board.WIDTH-1, board.HEIGHT//2)
        current_puck_position = (board.WIDTH//2, board.HEIGHT//2)

        # WHEN
        next_puck_position = board._Board__get_next_free_node(
            current_puck_position, Board.EAST)

        # THEN
        self.assertEqual(expected_puck_position, next_puck_position)

    def test_get_next_left_free_node(self):
        # GIVEN
        board = Board(obstacles=[])
        expected_puck_position = (0, board.HEIGHT//2)
        current_puck_position = (board.WIDTH//2, board.HEIGHT//2)

        # WHEN
        next_puck_position = board._Board__get_next_free_node(
            current_puck_position, Board.WEST)

        # THEN
        self.assertEqual(expected_puck_position, next_puck_position)

    def test_get_next_upper_free_node(self):
        # GIVEN
        board = Board(obstacles=[])
        expected_puck_position = (board.WIDTH//2, 0)
        current_puck_position = (board.WIDTH//2, board.HEIGHT//2)

        # WHEN
        next_puck_position = board._Board__get_next_free_node(
            current_puck_position, Board.NORTH)

        # THEN
        self.assertEqual(expected_puck_position, next_puck_position)

    def test_get_next_lower_free_node(self):
        # GIVEN
        board = Board(obstacles=[])
        expected_puck_position = (board.WIDTH//2, board.HEIGHT-1)
        current_puck_position = (board.WIDTH//2, board.HEIGHT//2)

        # WHEN
        next_puck_position = board._Board__get_next_free_node(
            current_puck_position, Board.SOUTH)

        # THEN
        self.assertEqual(expected_puck_position, next_puck_position)

    def test_move_puck_to_up(self):
        #GIVEN
        board= Board(obstacles=[])
        initial_puck_position = (board.WIDTH//2, board.HEIGHT//2)
        expected_puck_position = (board.WIDTH//2, 0)

        #WHEN
        board._Board__move_puck_to(initial_puck_position, Board.NORTH)

        #THEN
        pucks = [node for node, attributes in board.graph.nodes(data=True) if attributes.get('puck')]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)


    def test_move_puck_to_left(self):
        #GIVEN
        board= Board(obstacles=[])
        initial_puck_position = (board.WIDTH//2, board.HEIGHT//2)
        expected_puck_position = (0, board.HEIGHT//2)

        #WHEN
        board._Board__move_puck_to(initial_puck_position, Board.WEST)

        #THEN
        pucks = [node for node, attributes in board.graph.nodes(data=True) if attributes.get('puck')]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)

    def test_move_puck_to_right(self):
        #GIVEN
        board= Board(obstacles=[])
        initial_puck_position = (board.WIDTH//2, board.HEIGHT//2)
        expected_puck_position = (board.WIDTH-1, board.HEIGHT//2)

        #WHEN
        board._Board__move_puck_to(initial_puck_position, Board.EAST)

        #THEN
        pucks = [node for node, attributes in board.graph.nodes(data=True) if attributes.get('puck')]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)


    def test_move_puck_to_down(self):
        #GIVEN
        board= Board(obstacles=[])
        initial_puck_position = (board.WIDTH//2, board.HEIGHT//2)
        expected_puck_position = (board.WIDTH//2, board.HEIGHT-1)

        #WHEN
        board._Board__move_puck_to(initial_puck_position, Board.SOUTH)

        #THEN
        pucks = [node for node, attributes in board.graph.nodes(data=True) if attributes.get('puck')]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)

    def test_tilt_board_twice_in_the_same_direction(self):
        #GIVEN
        board= Board(obstacles=[])
        initial_puck_position = (board.WIDTH//2, board.HEIGHT//2)
        expected_puck_position = (board.WIDTH//2, board.HEIGHT-1)

        #WHEN
        board.tilt(Board.SOUTH)
        board.tilt(Board.SOUTH)

        #THEN
        pucks = [node for node, attributes in board.graph.nodes(data=True) if attributes.get('puck')]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)

    def test_puck_should_be_stopped_by_obstacle_when_moved_toward_it(self):
        #GIVEN
        board= Board(width=7,height=7,obstacles=[(6,3)])
        initial_puck_position = (3, 3)
        expected_puck_position = (5,3)

        #WHEN
        board._Board__move_puck_to(initial_puck_position, Board.EAST)

        #THEN
        pucks = [node for node, attributes in board.graph.nodes(data=True) if attributes.get('puck')]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)

    def test_obstacles_should_have_no_corresponding_nodes_in_the_board(self):
        #GIVEN
        obstacle = (6,3)
        board= Board(width=7,height=7,obstacles=[obstacle])

        #THEN
        self.assertFalse(board.graph.edges(obstacle))

if __name__ == '__main__':
    unittest.main()
