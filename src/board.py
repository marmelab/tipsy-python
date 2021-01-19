import networkx as nx


class Board:
    [WEST, NORTH, EAST, SOUTH] = ["west", "north", "east", "south"]

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
