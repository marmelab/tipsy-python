import networkx as nx


class Board:
    width = 7
    height = 7
    [WEST, NORTH, EAST, SOUTH] = ["west","north","east","south"]

    def __init__(self):
        self.graph = nx.Graph()

        for x in range(Board.width):
            for y in range(Board.height):
                self.graph.add_node((x, y))

        for (x, y) in self.graph.nodes:
            if (x > 0):
                self.graph.add_edge((x, y), (x-1, y), direction=Board.WEST)
            if (x < Board.width - 1):
                self.graph.add_edge((x, y), (x+1, y), direction=Board.EAST)
            if (y > 0):
                self.graph.add_edge((x, y), (x, y-1), direction=Board.SOUTH)
            if (y < Board.height - 1):
                self.graph.add_edge((x, y), (x, y+1), direction=Board.NORTH)
