board_size = int(input("What size of game board? "))
horiz_line = " ---" * board_size
vert_line = "|   " * (board_size + 1)

for x in range(board_size):
  print(horiz_line)
  print(vert_line)
print(horiz_line)