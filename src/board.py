import networkx as nx


class Board:
    PUCK_KEY = 'puck'
    EXIT_KEY = 'exit'
    DIRECTION_KEY = 'direction'
    BLUE_KEY = 'blue'
    RED_KEY = 'red'
    BLACK_KEY = 'black'

    [WEST, NORTH, EAST, SOUTH] = ["w", "n", "e", "s"]

    DEFAULT_OBSTACLES = [(0, 3), (1, 1), (1, 5), (2, 2),
                         (2, 4), (3, 0), (3, 6), (4, 2), (4, 4), (5, 1), (5, 5), (6, 3)]
    PUCK_EXITS = 'puck_exit'
    DEFAULT_EXITS = [(1, -1), (7, 1), (-1, 5), (5, 7)]
    DEFAULT_PUCKS = {BLUE_KEY: [(1, 2), (3, 2), (5, 2), (1, 4), (3, 4), (5, 4)],
                     RED_KEY: [(2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)],
                     BLACK_KEY: [(3, 3)]}

    MODIFICATOR = {EAST: (1, 0), NORTH: (0, -1), WEST: (-1, 0), SOUTH: (0, 1)}

    PUCK_EXITS = 'puck_exits'

    def __init__(self, width=7, height=7, obstacles=DEFAULT_OBSTACLES, exits=DEFAULT_EXITS, pucks=DEFAULT_PUCKS):
        self.WIDTH = width
        self.HEIGHT = height
        self.graph = nx.DiGraph()
        self.__initialize_empty_board()
        self.__initialize_pucks(pucks)
        self.__initialize_exits(exits)
        self.__initialize_obstacles(obstacles)

    def tilt(self, direction):
        pucks = [node for node, attributes in self.graph.nodes(
            data=True) if attributes.get(Board.PUCK_KEY)]
        fallen_pucks = 0
        for puck in pucks:
            if self.__move_puck_to(puck, direction):
                fallen_pucks += 1
        return fallen_pucks

    def __get_coordinate_by_direction(self, node, direction):
        (node_x, node_y) = node
        (direction_x, direction_y) = Board.MODIFICATOR.get(direction)

        return ((node_x + direction_x), (node_y + direction_y))

    def __initialize_pucks(self, pucks):
        for puck in pucks[Board.BLUE_KEY]:
            self.__add_puck(puck, Board.BLUE_KEY)
        for puck in pucks[Board.RED_KEY]:
            self.__add_puck(puck, Board.RED_KEY)

    def __initialize_obstacles(self, obstacles):
        self.graph.remove_nodes_from(obstacles)

    def __initialize_exits(self, exits):
        for (i, j) in exits:
            self.graph.add_node((i, j), exit=True)
            if i == -1:
                self.graph.add_edge((0, j), (i, j), direction=Board.WEST)
            if i == self.WIDTH:
                self.graph.add_edge((self.WIDTH-1, j),
                                    (i, j), direction=Board.EAST)
            if j == self.HEIGHT:
                self.graph.add_edge((i, j-1),
                                    (i, j), direction=Board.SOUTH)
            if j == -1:
                self.graph.add_edge((i, 0),
                                    (i, j), direction=Board.NORTH)

    def __initialize_empty_board(self):
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                if (x > 0):
                    self.graph.add_edge((x, y), (x-1, y), direction=Board.WEST)
                if (x < self.WIDTH - 1):
                    self.graph.add_edge((x, y), (x+1, y), direction=Board.EAST)
                if (y > 0):
                    self.graph.add_edge(
                        (x, y), (x, y-1), direction=Board.NORTH)
                if (y < self.HEIGHT - 1):
                    self.graph.add_edge(
                        (x, y), (x, y+1), direction=Board.SOUTH)

    def __get_next_free_node(self, node, direction):
        next_node = [next_node for start_node, next_node, edge_attrs in self.graph.out_edges(
            node, data=True) if (edge_attrs.get(Board.DIRECTION_KEY) == direction and not self.graph[next_node].get(Board.PUCK_KEY))]
        if next_node:
            return self.__get_next_free_node(next_node[0], direction)
        return node

    def __remove_puck(self, node):
        if self.graph.has_node(node):
            puck_color = self.graph.nodes[node].get(Board.PUCK_KEY)
            del self.graph.nodes[node][Board.PUCK_KEY]
            return puck_color

    def __add_puck(self, node, color):
        if self.graph.has_node(node):
            self.graph.nodes[node][Board.PUCK_KEY] = color

    def __move_puck_to(self, node, direction):
        # Get next position of puck
        next_free_node = self.__get_next_free_node(node, direction)
        # Remove puck attribute from current node
        puck_color = self.__remove_puck(node)
        # Add puck attribute in next position
        if self.graph.nodes[next_free_node].get(Board.EXIT_KEY):
            return Board.PUCK_EXITS
        else:
            self.__add_puck(next_free_node, puck_color)
