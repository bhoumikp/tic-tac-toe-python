from ui import UI
from random import *
from settings import *
from board import Board
import time

class Game():
	def __init__(self):
		self.ui = UI()
		self.turn = FIRST_PLAYER
		self.board = Board(self.ui)
		self.game_mode = GAME_MODE
		self.isPlaying = False
		self.ai = 'O' if FIRST_PLAYER == 'X' else 'X'
		self.scores = {'X': 10, 'O': 0}


	def start(self):
		self.board.create_new_board()
		self.ui.whose_turn.config(text=f'{self.turn} Turn', cursor='hand2')
		self.ui.players.config(text=f'{self.game_mode}', cursor='hand2')
		self.bind_labels()
		self.ui.create_labels()
		self.update_score()
		self.isPlaying = True
		if self.game_mode == '1P' and self.board.isEmpty():
			self.turn = self.ai
			self.computer()
		

	def run(self, event):
		if self.isPlaying:
			self.ui.alert_msg.destroy()
			grid_cords = self.ui.pixel_to_grid((event.x, event.y))
			if grid_cords != None and self.board.isCellEmpty(grid_cords):
				self.board.new_move(self.turn, grid_cords)
				self.check_result()


	def computer(self):
		x = choice((0, 1, 2))
		y = choice((0, 1, 2))

		if self.board.isCellEmpty((x,y)):
			self.ui.unbind_labels()
			self.ui.after(400, lambda : self.board.new_move(self.turn, (x, y)))
			self.ui.after(400, self.check_result)
			self.ui.after(400, self.bind_labels)
			return
		self.computer()


	def check_result(self):
		if self.has_won(self.turn):
			self.isPlaying = False 
			self.scores[self.turn] += 1
			self.update_score()
			self.ui.gameover(self.turn, lambda event : self.start())
		elif self.is_a_draw():
			self.isPlaying = False
			self.ui.gameover('DRAW', lambda event : self.start())
		else:
			self.turn = 'O' if self.turn == 'X' else 'X'
			self.ui.whose_turn.config(text=f'{self.turn} Turn')
			if self.game_mode == '1P' and self.turn == self.ai:
				self.computer()


	def has_won(self, symbol):
		for y in range(3):
			if self.board.layout[y] == [symbol, symbol, symbol]:
				return True
		for x in range(3):
			if self.board.layout[0][x] == self.board.layout[1][x] == self.board.layout[2][x] == symbol:
				return True
		if self.board.layout [0][0] ==self.board.layout [1][1] ==self.board.layout [2][2]== symbol:
			return True
		elif self.board.layout [0][2] == self.board.layout[1][1]== self.board.layout [2][0]== symbol:
			return True
		return False


	def is_a_draw(self):
		for row in self.board.layout:
			if EMPTY in row:
				return False
		return True


	def change_turn(self):
		if self.game_mode == '2P' and self.board.isEmpty():
			self.turn = 'O' if self.turn == 'X' else 'X'
			self.ui.whose_turn.config(text=f'{self.turn} Turn')
		else:
			if self.board.get_number_of_moves() == 1:
				self.ai = self.turn
				self.new_game()


	def new_game(self):
		if self.scores != {'X': 0, 'O': 0}: 
			self.reset_scores()
			self.start()
			self.ui.alert('New Game Started!', 'bottom')


	def change_game_mode(self):
		if self.scores != {'X': 0, 'O': 0}: self.reset_scores()
		if self.game_mode == '2P': 
			self.ai = FIRST_PLAYER
		else: 
			self.turn = FIRST_PLAYER
		self.game_mode = '2P' if self.game_mode == '1P' else '1P'
		self.start()
		self.ui.alert(f'Game mode: {self.game_mode}', 'bottom')


	def update_score(self):
		scores = list(self.scores.values())
		self.ui.xscore.config(text=f'X - {scores[0]}')
		self.ui.oscore.config(text=f'O - {scores[1]}')


	def bind_labels(self):
		self.ui.whose_turn.bind('<Button-1>', lambda event : self.change_turn())
		self.ui.new_game.bind('<Button-1>', lambda event : self.new_game())
		self.ui.restart.bind('<Button-1>', lambda event : self.start())
		self.ui.canvas.bind('<Button-1>', self.run)
		self.ui.players.bind('<Button-1>', lambda event : self.change_game_mode())
		self.ui.canvas.bind('<Motion>', self.mouse_motion)
		self.ui.canvas.config(cursor='hand2')


	def mouse_motion(self, event):
		
		if self.isPlaying:
			grid_cords = self.ui.pixel_to_grid((event.x, event.y))

			cursor = 'hand2' if self.board.isCellEmpty(grid_cords) else 'arrow'
			self.ui.canvas.config(cursor=cursor)


	def reset_scores(self):
		self.turn = FIRST_PLAYER
		# self.scores = {'X': 0, 'O': 0}
		# self.ui.xscore.config(text='X - 0')
		# self.ui.oscore.config(text='O - 0')
	


	


	

