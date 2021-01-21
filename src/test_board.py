import unittest
from board import Board


class TestBoard(unittest.TestCase):

    def test_empty_board_should_have_width_x_height_nodes(self):
        # GIVEN
        board = Board(obstacles=[], exits=[])

        # THEN
        self.assertEqual(board.graph.number_of_nodes(),
                         board.WIDTH * board.HEIGHT)

    def test_node_with_puck_on_it_should_have_puck_attribute(self):
        # GIVEN
        board = Board(obstacles=[], exits=[], pucks={Board.BLUE_KEY:[(3, 3)],Board.RED_KEY:[]})
        known_node_with_puck = (board.WIDTH//2, board.HEIGHT//2)

        # THEN
        nodes_with_puck_attribute = [node for node, data in board.graph.nodes(
            data=True) if data.get(Board.PUCK_KEY)]
        self.assertIn(known_node_with_puck, nodes_with_puck_attribute)

    def test_node_without_puck_on_it_should_not_have_puck_attribute(self):
        # GIVEN
        board = Board(obstacles=[], exits=[], pucks={Board.BLUE_KEY:[(3, 3)],Board.RED_KEY:[]})
        known_node_with_puck = (board.WIDTH//2, board.HEIGHT//2)

        # THEN
        nodes_with_no_puck_attribute = [node for node, data in board.graph.nodes(
            data=True) if not data.get(Board.PUCK_KEY)]
        self.assertNotIn(known_node_with_puck, nodes_with_no_puck_attribute)

    def test_empty_board_left_borders_should_have_no_left_neighbours(self):
        # GIVEN
        board = Board(obstacles=[], exits=[])

        # THEN
        for y in range(board.HEIGHT):
            current_node_neighbors = board.graph.neighbors(
                (0, y))
            left_neighbor = (-1, y)

            self.assertNotIn(left_neighbor,
                             current_node_neighbors)

    def test_empty_board_right_borders_should_have_no_right_neighbours(self):
        # GIVEN
        board = Board(obstacles=[], exits=[])

        # THEN
        for y in range(board.HEIGHT):
            current_node_neighbors = board.graph.neighbors(
                (board.WIDTH - 1, y))
            right_neighbor = (board.HEIGHT, y)

            self.assertNotIn(right_neighbor,
                             current_node_neighbors)

    def test_empty_board_upper_borders_should_have_no_upper_neighbours(self):
        # GIVEN
        board = Board(obstacles=[], exits=[])

        # THEN
        for x in range(board.WIDTH):
            current_node_neighbors = board.graph.neighbors(
                (x, 0))
            northest_neighbor = (x, -1)

            self.assertNotIn(northest_neighbor,
                             current_node_neighbors)

    def test_empty_board_lower_borders_should_have_no_lower_neighbours(self):
        # GIVEN
        board = Board(obstacles=[], exits=[])

        # THEN
        for x in range(board.WIDTH):
            current_node_neighbors = board.graph.neighbors(
                (x, board.HEIGHT-1))
            northest_neighbor = (x, board.HEIGHT)

            self.assertNotIn(northest_neighbor,
                             current_node_neighbors)

    def test_empty_board_middle_node_should_have_upper_lower_right_and_left_neighbours(self):
        # GIVEN
        board = Board(3, 3, obstacles=[], exits=[], pucks={Board.BLUE_KEY:[],Board.RED_KEY:[]})

        # THEN
        middle_node = (1, 1)
        east_node = (2, 1)
        south_node = (1, 2)
        west_node = (0, 1)
        north_node = (1, 0)

        self.assertEqual(board.graph[middle_node]
                         [east_node][Board.DIRECTION_KEY], Board.EAST)
        self.assertEqual(board.graph[middle_node]
                         [south_node][Board.DIRECTION_KEY], Board.SOUTH)
        self.assertEqual(board.graph[middle_node]
                         [west_node][Board.DIRECTION_KEY], Board.WEST)
        self.assertEqual(board.graph[middle_node]
                         [north_node][Board.DIRECTION_KEY], Board.NORTH)

    def test_get_next_right_free_node(self):
        # GIVEN
        board = Board(obstacles=[], exits=[])
        expected_puck_position = (board.WIDTH-1, board.HEIGHT//2)
        current_puck_position = (board.WIDTH//2, board.HEIGHT//2)

        # WHEN
        next_puck_position = board._Board__get_next_free_node(
            current_puck_position, Board.EAST)

        # THEN
        self.assertEqual(expected_puck_position, next_puck_position)

    def test_get_next_left_free_node(self):
        # GIVEN
        board = Board(obstacles=[], exits=[])
        expected_puck_position = (0, board.HEIGHT//2)
        current_puck_position = (board.WIDTH//2, board.HEIGHT//2)

        # WHEN
        next_puck_position = board._Board__get_next_free_node(
            current_puck_position, Board.WEST)

        # THEN
        self.assertEqual(expected_puck_position, next_puck_position)

    def test_get_next_upper_free_node(self):
        # GIVEN
        board = Board(obstacles=[], exits=[])
        expected_puck_position = (board.WIDTH//2, 0)
        current_puck_position = (board.WIDTH//2, board.HEIGHT//2)

        # WHEN
        next_puck_position = board._Board__get_next_free_node(
            current_puck_position, Board.NORTH)

        # THEN
        self.assertEqual(expected_puck_position, next_puck_position)

    def test_get_next_lower_free_node(self):
        # GIVEN
        board = Board(obstacles=[], exits=[])
        expected_puck_position = (board.WIDTH//2, board.HEIGHT-1)
        current_puck_position = (board.WIDTH//2, board.HEIGHT//2)

        # WHEN
        next_puck_position = board._Board__get_next_free_node(
            current_puck_position, Board.SOUTH)

        # THEN
        self.assertEqual(expected_puck_position, next_puck_position)

    def test_move_puck_to_up(self):
        # GIVEN
        board = Board(obstacles=[], exits=[], pucks={Board.BLUE_KEY:[(3, 3)],Board.RED_KEY:[]})
        initial_puck_position = (3, 3)
        expected_puck_position = (3, 0)

        # WHEN
        board._Board__move_puck_to(initial_puck_position, Board.NORTH)

        # THEN
        pucks = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.PUCK_KEY)]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)

    def test_move_puck_to_left(self):
        # GIVEN
        board = Board(obstacles=[], exits=[], pucks={Board.BLUE_KEY:[(3, 3)],Board.RED_KEY:[]})
        initial_puck_position = (board.WIDTH//2, board.HEIGHT//2)
        expected_puck_position = (0, board.HEIGHT//2)

        # WHEN
        board._Board__move_puck_to(initial_puck_position, Board.WEST)

        # THEN
        pucks = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.PUCK_KEY)]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)

    def test_move_puck_to_right(self):
        # GIVEN
        board = Board(obstacles=[], exits=[], pucks={Board.BLUE_KEY:[(3, 3)],Board.RED_KEY:[]})
        initial_puck_position = (board.WIDTH//2, board.HEIGHT//2)
        expected_puck_position = (board.WIDTH-1, board.HEIGHT//2)

        # WHEN
        board._Board__move_puck_to(initial_puck_position, Board.EAST)

        # THEN
        pucks = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.PUCK_KEY)]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)

    def test_move_puck_to_down(self):
        # GIVEN
        board = Board(obstacles=[], exits=[], pucks={Board.BLUE_KEY:[(3, 3)],Board.RED_KEY:[]})
        initial_puck_position = (board.WIDTH//2, board.HEIGHT//2)
        expected_puck_position = (board.WIDTH//2, board.HEIGHT-1)

        # WHEN
        board._Board__move_puck_to(initial_puck_position, Board.SOUTH)

        # THEN
        pucks = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.PUCK_KEY)]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)

    def test_puck_should_end_at_the_same_position_when_tilt_board_twice_in_the_same_direction(self):
        # GIVEN
        board = Board(obstacles=[], exits=[], pucks={Board.BLUE_KEY:[(3, 3)],Board.RED_KEY:[()]})
        initial_puck_position = (board.WIDTH//2, board.HEIGHT//2)
        expected_puck_position = (board.WIDTH//2, board.HEIGHT-1)

        # WHEN
        board.tilt(Board.SOUTH)
        board.tilt(Board.SOUTH)

        # THEN
        pucks = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.PUCK_KEY)]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)

    def test_puck_should_be_stopped_by_obstacle_when_moved_toward_it(self):
        # GIVEN
        board = Board(width=7, height=7, obstacles=[(6, 3)], exits=[], pucks={Board.BLUE_KEY:[(3, 3)],Board.RED_KEY:[]})
        initial_puck_position = (3, 3)
        expected_puck_position = (5, 3)

        # WHEN
        board._Board__move_puck_to(initial_puck_position, Board.EAST)

        # THEN
        pucks = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.PUCK_KEY)]
        self.assertIn(expected_puck_position, pucks)
        self.assertNotIn(initial_puck_position, pucks)

    def test_obstacles_should_have_no_corresponding_nodes_in_the_board(self):
        # GIVEN
        obstacle = (6, 3)
        board = Board(width=7, height=7, obstacles=[obstacle], exits=[])

        # THEN
        self.assertFalse(board.graph.edges(obstacle))

    def test_left_exit_should_have_attribute_exit_and_west_edge_with_right_node(self):
        # GIVEN
        exit_node = (-1, 0)
        right_node = (0, 0)
        board = Board(width=7, height=7, obstacles=[], exits=[exit_node])

        # THEN
        exits = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.EXIT_KEY)]

        self.assertIn(exit_node, exits)
        self.assertEqual(board.graph[right_node]
                         [exit_node][Board.DIRECTION_KEY], Board.WEST)

    def test_right_exit_should_have_attribute_exit_and_east_edge_with_left_node(self):
        # GIVEN
        width = 7
        exit_node = (width, 0)
        left_node = (width-1, 0)
        board = Board(width=width, height=width,
                      obstacles=[], exits=[exit_node])

        # THEN
        exits = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.EXIT_KEY)]

        self.assertIn(exit_node, exits)
        self.assertEqual(board.graph[left_node]
                         [exit_node][Board.DIRECTION_KEY], Board.EAST)

    def test_lower_exit_should_have_attribute_exit_and_south_edge_with_upper_node(self):
        # GIVEN
        height = 7
        exit_node = (0, height)
        upper_node = (0, height-1)
        board = Board(width=height, height=height,
                      obstacles=[], exits=[exit_node])

        # THEN
        exits = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.EXIT_KEY)]

        self.assertIn(exit_node, exits)
        self.assertEqual(board.graph[upper_node]
                         [exit_node][Board.DIRECTION_KEY], Board.SOUTH)

    def test_upper_exit_should_have_attribute_exit_and_north_edge_with_lower_node(self):
        # GIVEN
        exit_node = (0, -1)
        lower_node = (0, 0)
        board = Board(width=7, height=7,
                      obstacles=[], exits=[exit_node])

        # THEN
        exits = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.EXIT_KEY)]

        self.assertIn(exit_node, exits)
        self.assertEqual(board.graph[lower_node]
                         [exit_node][Board.DIRECTION_KEY], Board.NORTH)

    def test_tilt_board_with_puck_next_to_exit_should_push_the_puck_out(self):
        # GIVEN
        exit_node = (1, -1)
        puck_node = (1, 1)
        board = Board(3, 3,
                      obstacles=[], exits=[exit_node], pucks={Board.BLUE_KEY:[puck_node],Board.RED_KEY:[]})

        # WHEN
        fallen_pucks = board.tilt(Board.NORTH)

        # THEN
        self.assertEqual(fallen_pucks, 1)

    def test_when_trying_to_initialize_with_pucks_out_of_the_bounds_it_should_only_add_valid_ones(self):
        # GIVEN
        invalid_pucks = [(99, 12), (-25, -65)]
        valid_puck = (1, 1)

        # WHEN
        board = Board(3, 3,
                      obstacles=[], exits=[], pucks={Board.BLUE_KEY:invalid_pucks + [valid_puck],Board.RED_KEY:[]})

        # THEN
        pucks = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.PUCK_KEY)]
        self.assertIn(valid_puck, pucks)

    def test_when_trying_to_initialize_with_obstacles_out_of_bounds_it_should_only_remove_valid_ones(self):
        # GIVEN
        invalid_obstacles = [(99, 12), (-25, -65)]
        valid_obstacle = (1, 1)

        # WHEN
        board = Board(3, 3, exits=[],
                      obstacles=invalid_obstacles + [valid_obstacle])
        # THEN
        self.assertFalse(board.graph.has_node(valid_obstacle))

    def test_when_one_puck_move_toward_another_it_should_be_blocked(self):
        # # # # #    # # # # #
        # O   0 #    #   O 0 #
        #       # => #       #
        #       #    #       #
        # # # # #    # # # # #
        # GIVEN
        board = Board(3,3,obstacles=[],pucks={Board.BLUE_KEY:[(0,0)],Board.RED_KEY:[(2,0)]},exits=[])
        expected_blue_puck_position = (1,0)
        expected_red_puck_position = (2,0)

        # WHEN
        board.tilt(Board.EAST)

        # THEN
        pucks = [node for node, attributes in board.graph.nodes(
            data=True) if attributes.get(Board.PUCK_KEY)]

        self.assertIn(expected_blue_puck_position, pucks)
        self.assertIn(expected_red_puck_position, pucks)

if __name__ == '__main__':
    unittest.main()
