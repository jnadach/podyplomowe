# autor: Jan Nadachowski

#        A  B  C  D  E  F  G  H
#     1  #  #  #  #  #  #  #  #
#     2  #  #  #  #  #  #  #  #
#     3  #  #  #  #  #  #  #  #
#     4  #  #  #  #  #  #  #  #
#     5  #  #  #  #  #  #  #  #
#     6  #  #  #  #  #  #  #  #
#     7  #  #  #  #  #  #  #  #
#     8  #  #  #  #  #  #  #  #

import random

#Creating empty chess board
chess_row = ["--" for i in range(8)]
chess_board = [chess_row[:] for i in range(8)]

# "B_" -> biale
# "C_" -> czarne
# "_W" -> wieza, "_k" -> kon, "_L" -> laufer, "_K" -> krol, "_H" -> hetman, "_P" -> pion

FIGURY = ["BW", "Bk", "BL", "BK", "BH", "BL", "Bk", "BW",
          "CW", "Ck", "CL", "CK", "CH", "CL", "Ck", "CW"]

PIONY = ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP",
         "CP", "CP", "CP", "CP", "CP", "CP", "CP", "CP"]

wybrane_figury = random.sample(FIGURY, 2)
wybrane_piony = random.sample(PIONY, 3)
wybrane_wszystkie = wybrane_figury + wybrane_piony

for i in wybrane_wszystkie:
    counter = 0
    while not counter:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if chess_board[x][y] == "--":
            chess_board[x][y] = i
            counter = True

for chess_row in chess_board:
    for chess_square in chess_row:
        print(chess_square, end=" ")
    print()
