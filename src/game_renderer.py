from board import Board
from os import get_terminal_size


class GameRenderer:
    TOP_PADDING = int(get_terminal_size()[1]*0.20)
    LEFT_PADING = int((get_terminal_size()[0]-50) / 2)
    WHITE_BG = '\033[47m'
    GREY_BG = '\033[47m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    END_COLOR = '\033[0m'
    OBSTACLE = WHITE_BG + '\033[90m# ' + END_COLOR
    EXIT = WHITE_BG + '  ' + END_COLOR
    EMPTY_CELL = WHITE_BG + '  ' + END_COLOR
    PUCK = {Board.RED: WHITE_BG + '\033[31mO ' + END_COLOR,
            Board.BLUE: WHITE_BG + '\033[34mO ' + END_COLOR,
            Board.RED+Board.FLIPPED_KEY: WHITE_BG + '\033[31m0 ' + END_COLOR,
            Board.BLUE+Board.FLIPPED_KEY: WHITE_BG + '\033[34m0 ' + END_COLOR,
            Board.BLACK: WHITE_BG + '\033[90m0 ' + END_COLOR}
    PLAYERS = {
        Board.RED: RED + ' RED ' + END_COLOR,
        Board.BLUE: BLUE + ' BLUE ' + END_COLOR,
    }

    def draw_board(self, game):
        board = GameRenderer.OBSTACLE
        for i in range(game.board.WIDTH):
            if game.board.graph.has_node((i, -1)) and game.board.graph.nodes[(i, -1)].get(Board.EXIT_KEY):
                board += GameRenderer.EXIT
            else:
                board += GameRenderer.OBSTACLE
        board += GameRenderer.OBSTACLE + '\n'
        for j in range(game.board.HEIGHT):
            if game.board.graph.has_node((-1, j)) and game.board.graph.nodes[(-1, j)].get(Board.EXIT_KEY):
                board += GameRenderer.EXIT
            else:
                board += GameRenderer.OBSTACLE
            for i in range(game.board.WIDTH):
                if (not game.board.graph.has_node((i, j))):
                    board += GameRenderer.OBSTACLE
                elif (game.board.graph.nodes[(i, j)].get(Board.PUCK_KEY)):
                    puck_color = game.board.graph.nodes[(i, j)].get(Board.PUCK_KEY)
                    flipped = Board.FLIPPED_KEY if game.board.graph.nodes[(i, j)].get(Board.FLIPPED_KEY) else ''
                    board += GameRenderer.PUCK[puck_color+flipped]
                else:
                    board += GameRenderer.EMPTY_CELL
            if game.board.graph.has_node((game.board.WIDTH, j)) and game.board.graph.nodes[(game.board.WIDTH, j)].get(Board.EXIT_KEY):
                board += GameRenderer.EXIT
            else:
                board += GameRenderer.OBSTACLE
            board += '\n'
        board += GameRenderer.OBSTACLE
        for i in range(game.board.WIDTH):
            if game.board.graph.has_node((i, game.board.HEIGHT)) and game.board.graph.nodes[(i, game.board.HEIGHT)].get(Board.EXIT_KEY):
                board += GameRenderer.EXIT
            else:
                board += GameRenderer.OBSTACLE
        board += GameRenderer.OBSTACLE
        return board

    def display_board(self, game):
        print('\n' * GameRenderer.TOP_PADDING)
        for line in self.draw_board(game).split('\n'):
            print(' ' * GameRenderer.LEFT_PADING + line)

    def input_message(self):
        return ' ' * GameRenderer.LEFT_PADING + 'Use ' + Board.NORTH + ', ' + Board.SOUTH +\
            ', ' + Board.EAST + ', ' + Board.WEST + ' to tilt the board: '

    def display_title(self):
        print('\n' * GameRenderer.TOP_PADDING)
        print(' ' * GameRenderer.LEFT_PADING + "    .    o8o")
        print(' ' * GameRenderer.LEFT_PADING + "  .o8    `\"'")
        print(' ' * GameRenderer.LEFT_PADING +
              ".o888oo oooo  oo.ooooo.   .oooo.o oooo    ooo")
        print(' ' * GameRenderer.LEFT_PADING +
              "  888   `888   888' `88b d88(  \"8  `88.  .8'")
        print(' ' * GameRenderer.LEFT_PADING +
              "  888    888   888   888 `\"Y88b.    `88..8'")
        print(' ' * GameRenderer.LEFT_PADING +
              "  888 .  888   888   888 o.  )88b    `888'")
        print(' ' * GameRenderer.LEFT_PADING +
              "  \"888\" o888o  888bod8P' 8\"\"888P'     .8'")
        print(' ' * GameRenderer.LEFT_PADING +
              "               888                .o..P'")
        print(' ' * GameRenderer.LEFT_PADING +
              "              o888o               `Y8P'")
        print(' ' * GameRenderer.LEFT_PADING + "")
        print(' ' * GameRenderer.LEFT_PADING + "")
        input(' ' * GameRenderer.LEFT_PADING +
              "Welcome to Tipsy game. Type Enter to start")

    def display_instructions(self):
        print(' ' * GameRenderer.LEFT_PADING + "     ^")
        print(' ' * GameRenderer.LEFT_PADING + "     n")
        print(' ' * GameRenderer.LEFT_PADING + " < w * e >")
        print(' ' * GameRenderer.LEFT_PADING + "     s")
        print(' ' * GameRenderer.LEFT_PADING + "     v")

    def display_game_infos(self, game):
        print(' ' * GameRenderer.LEFT_PADING + '')
        print(' ' * GameRenderer.LEFT_PADING +
              'it\'s '+GameRenderer.PLAYERS[game.current_player]+' turn...')

    def display_winner(self, winner):
        COLOR_TAG = GameRenderer.RED if winner == Board.RED else GameRenderer.BLUE
        print( COLOR_TAG + ' ' * GameRenderer.LEFT_PADING + "                                           .''." + GameRenderer.END_COLOR)
        print( COLOR_TAG + ' ' * GameRenderer.LEFT_PADING + "       .''.      .        *''*    :_\/_:     ." + GameRenderer.END_COLOR)
        print( COLOR_TAG + ' ' * GameRenderer.LEFT_PADING + "      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'." + GameRenderer.END_COLOR)
        print( COLOR_TAG + ' ' * GameRenderer.LEFT_PADING + "  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-" + GameRenderer.END_COLOR)
        print( COLOR_TAG + ' ' * GameRenderer.LEFT_PADING + " :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'" + GameRenderer.END_COLOR)
        print( COLOR_TAG + ' ' * GameRenderer.LEFT_PADING + " : /\ : :::::     *_\/_*     -= o =-  /)\    '  *" + GameRenderer.END_COLOR)
        print( COLOR_TAG + ' ' * GameRenderer.LEFT_PADING + "  '..'  ':::'     * /\ *     .'/.\'.   '" + GameRenderer.END_COLOR)
        print( COLOR_TAG + ' ' * GameRenderer.LEFT_PADING + "      *            *..*         :" + GameRenderer.END_COLOR)
        print( COLOR_TAG + ' ' * GameRenderer.LEFT_PADING + "        *" + GameRenderer.END_COLOR)
        print( COLOR_TAG + ' ' * GameRenderer.LEFT_PADING + "        *" + GameRenderer.END_COLOR)
        print(GameRenderer.LEFT_PADING*' ' + GameRenderer.PLAYERS[winner] +
              " won the game! Congrats to the winner!")
