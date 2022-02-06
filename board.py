from settings import *


class Board:
	def __init__(self, ui):
		self.ui = ui
		self.layout = []


	def create_new_board(self):
		self.layout = [[EMPTY for _ in range(3)] for _ in range(3)]
		self.ui.canvas.delete('all')
		self.ui.draw_board_lines()
		

	def new_move(self, player, grid_cords):
		self.ui.draw_XO(player, (grid_cords), False)
		self.layout[grid_cords[1]][grid_cords[0]] = player


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



