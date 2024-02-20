from ui import UI
from settings import *
from board import Board
from ai import AI


class Game():
	def __init__(self):
		self.ui = UI()
		self.turn = FIRST_PLAYER
		self.board = Board(self.ui)
		self.ai = AI()
		self.game_mode = GAME_MODE
		self.isPlaying = False
		self.scores = {'X': 0, 'O': 0}


	def start(self):
		self.ui.geometry("370x430")
		self.board.create_new_board()
		cursor = 'hand2' if self.game_mode == 'Easy' or self.game_mode == 'Medium' else 'arrow'
		self.ui.whose_turn.config(text=f'{self.turn} Turn', cursor=cursor)
		self.bind_widgets()
		self.ui.create_widgets(self.game_mode, self.change_game_mode)
		self.update_score()
		print(self.game_mode)
		self.isPlaying = True
		if self.game_mode != '2P' and self.ai.ai == self.turn:
			self.computer()
		

	def run(self, event):
		if self.isPlaying:
			self.ui.alert_msg.destroy()
			self.ui.whose_turn.config(cursor='arrow')
			grid_cords = self.ui.pixel_to_grid((event.x, event.y))
			if grid_cords != None and self.board.isCellEmpty(grid_cords):
				self.board.new_move(self.turn, grid_cords)
				self.check_result()


	def computer(self):
		if self.game_mode == 'Easy':
			y, x = self.ai.easy(self.board)
		else:
			y, x = self.ai.bestMove(self.board, self.game_mode)

		self.ui.unbind_widgets()
		self.ui.after(400, lambda : self.board.new_move(self.turn, (x, y)))
		self.ui.after(400, self.check_result)
		self.ui.after(400, self.bind_widgets)


	def check_result(self):
		winner = self.board.finalState(show=True, turn=self.turn)
		if winner:
			if winner != 'draw':
				print(winner)
				self.scores[self.turn] += 1
				self.update_score()

			if self.game_mode == '2P':
				self.turn = 'O' if self.turn == 'X' else 'X'
			else:
				self.turn = FIRST_PLAYER
			self.isPlaying = False 
			self.ui.gameover(winner, lambda event : self.start())
		else:
			self.turn = 'O' if self.turn == 'X' else 'X'
			self.ui.whose_turn.config(text=f'{self.turn} Turn')
			if self.game_mode != '2P' and self.turn == self.ai.ai:
				self.computer()


	def change_turn(self):
		if not self.game_mode == '2P' and not self.game_mode == 'Hard':
			moves = self.board.get_number_of_moves()
			if moves == 1 or self.board.isEmpty():
				self.reset_scores()
				self.ai.ai = self.turn
				self.ai.player = 'X' if self.ai.ai == 'O' else 'O'
				self.ui.game_modes.destroy()
				self.start()
				

	def new_game(self):
		if self.scores != {'X': 0, 'O': 0}: 
			self.reset_scores()
			self.ui.game_modes.destroy()
			self.start()
			self.ui.alert('New Game Started!', 'bottom')


	def change_game_mode(self, *args):
		shouldChange = 1 if self.game_mode != self.ui.level.get() else 0
		self.game_mode = self.ui.level.get()

		if shouldChange and self.scores != {'X': 0, 'O': 0}: 
			self.reset_scores()

		self.turn = FIRST_PLAYER
		self.ai.ai = 'X' if FIRST_PLAYER == 'O' else 'O'
		self.ui.game_modes.destroy()
		self.start()


	def update_score(self):
		scores = list(self.scores.values())
		self.ui.xscore.config(text=f'X - {scores[0]}')
		self.ui.oscore.config(text=f'O - {scores[1]}')


	def bind_widgets(self):
		cursor = 'arrow' if (self.scores == {'X': 0, 'O': 0}) else 'hand2'
		self.ui.new_game.config(cursor=cursor)
		self.ui.new_game.bind('<Button-1>', lambda event : self.new_game())
		self.ui.whose_turn.bind('<Button-1>', lambda event : self.change_turn())
		self.ui.restart.bind('<Button-1>', lambda event : self.start())
		self.ui.canvas.bind('<Button-1>', self.run)
		self.ui.canvas.bind('<Motion>', self.mouse_motion)
		self.ui.canvas.config(cursor='hand2')


	def mouse_motion(self, event):
		if self.isPlaying:
			grid_cords = self.ui.pixel_to_grid((event.x, event.y))
			cursor = 'hand2' if self.board.isCellEmpty(grid_cords) else 'arrow'
			self.ui.canvas.config(cursor=cursor)


	def reset_scores(self):
		self.turn = FIRST_PLAYER
		self.scores = {'X': 0, 'O': 0}
		self.ui.xscore.config(text='X - 0')
		self.ui.oscore.config(text='O - 0')
	


	# def bind_keys(self):
	# 	self.ui.bind('<t>', lambda event : self.change_turn())
	# 	self.ui.bind('<p>', lambda event : self.change_game_mode())
	# 	self.ui.bind('<r>', lambda event : self.start())
	# 	self.ui.bind('<n>', lambda event : self.new_game())
	


	

