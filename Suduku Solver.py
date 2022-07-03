board = [
    [0,7,0,5,0,0,0,0,0],
    [0,0,0,0,0,3,0,0,0],
    [5,0,0,6,2,7,9,8,0],
    [0,6,0,1,7,0,0,0,2],
    [2,0,1,0,0,9,7,4,0],
    [0,0,0,0,0,0,0,9,6],
    [9,0,0,0,0,0,0,0,0],
    [1,5,0,0,3,6,0,0,9],
    [0,0,0,0,0,2,0,6,0]
]


def Main(board):
	empty = EmptyCell(board)
	if not empty:
		return True
	else:
		row, column = empty 

	for num in range(1, 10):
		if valid(board, num, (row, column)):
			board[row][column] = num

			if Main(board):
				return True

			board[row][column] = 0

	return False
	

def valid(board, CurrentNum, CurrentPos):
	for i in range(len(board[0])):
		if board[CurrentPos[0]][i] == CurrentNum and i != CurrentPos[1]:
			return False
	
	for i in range(len(board)):
		if board[i][CurrentPos[1]] == CurrentNum and i != CurrentPos[0]:
			return False

	box_x = CurrentPos[1] // 3
	box_y = CurrentPos[0] // 3
	for i in range(box_y * 3, box_y * 3 + 3):
		for j in range(box_x * 3, box_x * 3 + 3):
			if board[i][j] == CurrentNum and (i, j) != CurrentPos:
				return False
	return True


def DisplayBoard(board):
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("---------------------")
		for j in range(len(board[0])):
			if j != 0 and j % 3 == 0:
				print("| ", end = "")

			print(str(board[i][j]), end = " ")
		print()
		

def EmptyCell(board):
	for i, row in enumerate(board):
		for j, column in enumerate(row):
			if board[i][j] == 0:
				return (i, j)
	return None


DisplayBoard(board)
Main(board)
print()
print()
DisplayBoard(board)
