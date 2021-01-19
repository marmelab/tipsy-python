from board import Board

board = Board()

while True:
    board.display()
    input_command = ''
    while (input_command.lower() not in ['e', 'w', 'n', 's']):
        input_command = raw_input("Use N,S,E,W keys to tilt the board: ")
    print('move to ' + input_command)
