#        A  B  C  D  E  F  G  H
#     1  #  #  #  #  #  #  #  #
#     2  #  #  #  #  #  #  #  #
#     3  #  #  #  #  #  #  #  #
#     4  #  #  #  #  #  #  #  #
#     5  #  #  #  #  #  #  #  #
#     6  #  #  #  #  #  #  #  #
#     7  #  #  #  #  #  #  #  #
#     8  #  #  #  #  #  #  #  #

WHITE_POWN = "WP"
BLACK_POWN = "BP"

chess_row = ["--" for i in range(8)]
chess_board = [chess_row[:] for i in range(8)]

chess_board[0][0] = WHITE_POWN
chess_board[3][5] = BLACK_POWN


for chess_row in chess_board:
    for chess_square in chess_row:
        print(chess_square, end=" ")
    print()



