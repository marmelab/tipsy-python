import networkx as nx


class Board:
    [WEST, NORTH, EAST, SOUTH] = ["w", "n", "e", "s"]
    DEFAULT_OBSTACLES = [(0, 3), (1, 1), (1, 5), (2, 2),
                         (2, 4), (3, 0), (3, 6), (4, 2), (4, 4), (5, 1), (5, 5), (6, 3)]
    PUCK_EXITS = 'puck_exit'
    DEFAULT_EXITS = [(1, -1), (7, 1), (-1, 5), (5, 7)]
    DEFAULT_PUCKS = {'blue': [(1, 2), (3, 2), (5, 2), (1, 4), (3, 4), (5, 4)],
                     'red': [(2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)]}

    def __init__(self, width=7, height=7, obstacles=DEFAULT_OBSTACLES, exits=DEFAULT_EXITS, pucks=DEFAULT_PUCKS):
        self.WIDTH = width
        self.HEIGHT = height
        self.graph = nx.DiGraph()
        self.__initialize_empty_board()
        self.__initialize_pucks(pucks)
        self.__initialize_exits(exits)
        self.__initialize_obstacles(obstacles)

    def __initialize_pucks(self, pucks):
        for puck in pucks['blue']:
            self.__add_puck(puck, 'blue')
        for puck in pucks['red']:
            self.__add_puck(puck, 'red')

    def __initialize_obstacles(self, obstacles):
        # TODO mention this in the blog note?
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

    def tilt(self, direction):
        pucks = [node for node, attributes in self.graph.nodes(
            data=True) if attributes.get('puck')]
        fallen_pucks = 0
        for puck in pucks:
            if self.__move_puck_to(puck, direction) == Board.PUCK_EXITS:
                fallen_pucks += 1
        return fallen_pucks

    def __get_next_free_node(self, node, direction):
        next_node = [next_node for start_node, next_node, edge_attrs in self.graph.out_edges(
            node, data=True) if (edge_attrs.get('direction') == direction)]
        if next_node:
            return self.__get_next_free_node(next_node[0], direction)
        return node

    def __remove_puck(self, node):
        if self.graph.has_node(node):
            puck_color = self.graph.nodes[node].get('puck')
            del self.graph.nodes[node]['puck']
            return puck_color

    def __add_puck(self, node, color):
        if self.graph.has_node(node):
            self.graph.nodes[node]["puck"] = color

    def __move_puck_to(self, node, direction):
        # Get next position of puck
        next_free_node = self.__get_next_free_node(node, direction)
        # Remove puck attribute from current node
        puck_color = self.__remove_puck(node)
        # Add puck attribute in next position
        if self.graph.nodes[next_free_node].get('exit'):
            return Board.PUCK_EXITS
        else:
            self.__add_puck(next_free_node)
