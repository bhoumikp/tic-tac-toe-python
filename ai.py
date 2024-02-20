from ui import UI
from random import *
from settings import *


class AI:
	def __init__(self):
		self.ai = 'X' if FIRST_PLAYER == 'O' else 'O'
		self.player = 'X' if self.ai == 'O' else 'O'
		

	def easy(self, board):
		x, y = choice(board.emptySquares())
		return x, y


	def bestMove(self, board, level): 
		bestScore = -100
		move = None

		for (row, col) in board.emptySquares():
			board.layout[row][col] = self.ai
			score = self.minimax(board, 0, level, False)
			board.layout[row][col] = 0
			if score > bestScore:
				bestScore = score
				move = (row, col)
		return move


	def minimax(self, board, depth, level, isMaximizing):
		result = board.finalState()
		if result:
			scores = {	'X': 1 if self.ai == 'X' else -1, 
						'O': 1 if self.ai == 'O' else -1, 
						'draw': 0 }
			return scores[result]

		if isMaximizing:
			bestScore = -100
			if(depth>=2 and level=='Medium'): 
				return bestScore
			for (row, col) in board.emptySquares():
				board.layout[row][col] = self.ai
				score = self.minimax(board, depth+1, level, False)
				board.layout[row][col] = 0
				bestScore = max(score, bestScore)
			return bestScore
		else:
			bestScore = 100
			if(depth>=2 and level=='Medium'): 
				return bestScore
			for (row, col) in board.emptySquares():
				board.layout[row][col] = self.player
				score = self.minimax(board, depth+1, level, True)
				board.layout[row][col] = 0
				bestScore = min(score, bestScore)
			return bestScore

