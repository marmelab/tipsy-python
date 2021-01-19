import networkx as nx


class Board:
    [WEST, NORTH, EAST, SOUTH] = ["west", "north", "east", "south"]

    def __init__(self, width=7, height=7):
        self.WIDTH = width
        self.HEIGHT = height
        self.graph = nx.Graph()

        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                self.graph.add_node((x, y))

        for (x, y) in self.graph.nodes:
            if (x > 0):
                self.graph.add_edge((x, y), (x-1, y), direction=Board.WEST)
            if (x < self.WIDTH - 1):
                self.graph.add_edge((x, y), (x+1, y), direction=Board.EAST)
            if (y > 0):
                self.graph.add_edge((x, y), (x, y-1), direction=Board.SOUTH)
            if (y < self.HEIGHT - 1):
                self.graph.add_edge((x, y), (x, y+1), direction=Board.NORTH)

    def display(self):
        print('# '*(self.WIDTH+2))
        for j in range(self.HEIGHT):
            line = '# '
            for i in range(self.WIDTH):
                line+='  '
            line+='#'
            print(line)
        print('# '*(self.WIDTH+2))
