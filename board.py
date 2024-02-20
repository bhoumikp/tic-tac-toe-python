from settings import *


class Board:
	def __init__(self, ui):
		self.ui = ui
		self.layout = []
		self.marked_sqrs = 0
		self.win_line_color = None


	def create_new_board(self):
		self.layout = [[EMPTY for _ in range(3)] for _ in range(3)]
		self.ui.canvas.delete('all')
		self.ui.draw_board_lines()
		

	def new_move(self, player, grid_cords):
		self.ui.draw_XO(player, (grid_cords), False)
		self.layout[grid_cords[1]][grid_cords[0]] = player


	def finalState(self, show=False, turn=None):
		fill_color = O_COLOR if turn == 'O' else X_COLOR

		#  Vertical win
		for col in range(3):
			if self.layout[0][col] == self.layout[1][col] == self.layout[2][col] != 0:
				if show:
					x = (CANVAS_SIZE/6) * (col+(col+1))
					self.ui.canvas.create_line(x, 0, x, CANVAS_SIZE, width=GRID_LINE_WIDTH, fill=fill_color)
				return self.layout[0][col]

		#  Horizontal win
		for row in range(3):
			if self.layout[row][0] == self.layout[row][1] == self.layout[row][2] != 0:
				if show:
					y = (CANVAS_SIZE/6) * (row+(row+1))
					self.ui.canvas.create_line(0, y, CANVAS_SIZE, y, width=GRID_LINE_WIDTH, fill=fill_color) 
				return self.layout[row][0]

		#  topLeft to bottomRight digonal
		if self.layout[0][0] == self.layout[1][1] == self.layout[2][2] != 0:
			if show:
				self.ui.canvas.create_line(0, 0, CANVAS_SIZE, CANVAS_SIZE, width=GRID_LINE_WIDTH, fill=fill_color)
			return self.layout[1][1]

		#  topRight to bottomLeft digonal
		if self.layout[2][0] == self.layout[1][1] == self.layout[0][2] != 0:
			if show:
				self.ui.canvas.create_line(0, CANVAS_SIZE, CANVAS_SIZE, 0, width=GRID_LINE_WIDTH, fill=fill_color) 
			return self.layout[1][1]

		# Check for Draw
		for row in self.layout:
			if EMPTY in row:
				# no result
				return 0
		return 'draw'


	def emptySquares(self):
		empty_sqrs = []
		for row in range(3):
			for col in range(3):
				if self.layout[row][col] == 0:
					empty_sqrs.append( (row, col) )
		return empty_sqrs


	def get_number_of_moves(self):
		moves = 0
		for row in self.layout:
			for col in row:
				if col != EMPTY:
					moves += 1
		return moves


	def isCellEmpty(self, cell_cords:tuple):
		if cell_cords != None:
			x = cell_cords[0]
			y = cell_cords[1]
			return not bool(self.layout[y][x])


	def isEmpty(self):
		return all(item == [EMPTY, EMPTY, EMPTY] for item in self.layout)




