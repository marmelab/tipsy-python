import networkx as nx


class Board:
    [WEST, NORTH, EAST, SOUTH] = ["w", "n", "e", "s"]

    def __init__(self, width=7, height=7):
        self.WIDTH = width
        self.HEIGHT = height
        self.graph = nx.DiGraph()
        self.__initialize_empty_board()
        self.__initialize_pucks_positions()

    def __initialize_pucks_positions(self):
        self.graph.nodes[(self.WIDTH//2, self.HEIGHT//2)]["puck"] = 'O'

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

    def display(self):
        print('# '*(self.WIDTH+2))
        for j in range(self.HEIGHT):
            line = '# '
            for i in range(self.WIDTH):
                if (self.graph.nodes[(i, j)].get('puck')):
                    line += 'o '
                else:
                    line += '  '
            line += '#'
            print(line)
        print('# '*(self.WIDTH+2))

    def tilt(self, direction):
        pucks = [node for node, attributes in self.graph.nodes(data=True) if attributes.get('puck')]
        for puck in pucks:
            self.__move_puck_to(puck, direction)

    def __get_next_free_node(self, node, direction):
        next_node = [next_node for start_node, next_node, edge_attrs in self.graph.out_edges(
            node, data=True) if edge_attrs.get('direction') == direction]
        if next_node:
            return self.__get_next_free_node(next_node[0], direction)
        return node

    def __remove_puck(self, node):
        del self.graph.nodes[node]['puck']

    def __add_puck(self, node):
        self.graph.nodes[node]["puck"] = 'o'

    def __move_puck_to(self, node, direction):
        # Get next position of puck
        next_free_node = self.__get_next_free_node(node, direction)
        # Remove puck attribute from current node
        self.__remove_puck(node)
        # Add puck attribute in next position
        self.__add_puck(next_free_node)
