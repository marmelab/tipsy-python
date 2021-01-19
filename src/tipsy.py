from board import Board

board = Board()

while True:
    board.display()
    input_command = ''

    while (input_command.lower() not in [Board.EAST, Board.WEST, Board.NORTH, Board.SOUTH]):
        input_command = input('Use ' + Board.NORTH + ', ' + Board.SOUTH + ', ' + Board.EAST + ', ' + Board.WEST + ' to tilt the board: ')
    print('move to ' + input_command)

    board.tilt(input_command);
