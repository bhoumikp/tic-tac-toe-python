from tkinter import *
from tkinter import ttk
from settings import *
from time import time


class UI(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.logo = PhotoImage(file=LOGO_PATH)
		self.title('Tic Tac Toe')
		self.iconphoto(True, self.logo)
		self.config(bg='white')
		self.bind('<x>', lambda event : self.destroy())
		self.window_height = CANVAS_SIZE
		self.geometry(F"{CANVAS_SIZE}x{self.window_height}+700+160")

		# Canvas
		self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg=BG, cursor='arrow')
		self.canvas.grid(row=1, column=0, columnspan=3)

		# Window Labels
		self.resizable(False, False)
		self.whose_turn = Label(bg='white', font=('Monospace', FONT_SIZE, 'bold'))
		self.xscore = Label(bg='white', pady=5, font=('Monospace', FONT_SIZE))
		self.oscore = Label(bg='white', font=('Monospace', FONT_SIZE))
		self.new_game = Label(text='New Game', bg='white', cursor='hand2', font=('Monospace', FONT_SIZE, 'bold'))
		self.restart = Label(text='Restart', bg='white', cursor='hand2', font=('Monospace', FONT_SIZE, 'bold'))
		self.alert_msg = Label(text='', bg='white')

		# OptionMenu
		self.level = StringVar(self)
		self.game_modes = None


	
	def loading_screen(self):
		self.canvas.create_rectangle(0, 0, CANVAS_SIZE, CANVAS_SIZE, fill='white', outline='')
		self.canvas.create_rectangle(int(CANVAS_SIZE/15), int(CANVAS_SIZE/15), int(CANVAS_SIZE*14/15), int(CANVAS_SIZE*14/15), outline='')
		self.canvas.create_rectangle(int(CANVAS_SIZE/10), int(CANVAS_SIZE/10), int(CANVAS_SIZE*9/10), int(CANVAS_SIZE*9/10), fill=BG, outline='')
		self.canvas.create_text(CANVAS_SIZE/2, CANVAS_SIZE/3, text='Tic Tac Toe', fill='black', font=('Roboto', int(-CANVAS_SIZE/12), 'bold'))
		self.draw_XO('O', ((CANVAS_SIZE/2)+30, int(CANVAS_SIZE/2)), True, 2)
		self.draw_XO('X', ((CANVAS_SIZE/2)-30, int(CANVAS_SIZE/2)), True, 2)
		self.canvas.create_text(CANVAS_SIZE/2, CANVAS_SIZE/1.5, text='loading', fill=X_COLOR, font=('Monospace', int(-CANVAS_SIZE/20)), tag='loader')
		def loader(dots, sec):
			if sec > WAIT_TIME-500: return
			if len(dots) > 2: dots = ''
			dots+='.'
			loader(dots, sec+LOAD_DELAY)
			self.after(sec, lambda : self.canvas.itemconfig('loader', text=f'loading{dots}'))
		loader('', 0)


	def create_widgets(self, game_mode, game_mode_func):
		# Top row labels
		self.xscore.grid(row=0, column=0)
		self.whose_turn.grid(row=0, column=1)
		self.oscore.grid(row=0, column=2)
		
		# Bottom row labels
		self.game_modes = ttk.OptionMenu(self, self.level, game_mode, *GAME_MODES, direction='above', command=game_mode_func)
		self.game_modes.grid(row=2, column=0)
		self.restart.grid(row=2, column=1, pady=0)
		self.restart.config(text='Restart')
		self.new_game.grid(row=2, column=2)
		self.new_game.config(text='New Game')


	def draw_board_lines(self):
		for n in range(1, 3):
			self.canvas.create_line(CELL_SIZE*n, 0, CELL_SIZE*n, CANVAS_SIZE, width=GRID_LINE_WIDTH, fill=GRID_COLOR)
			self.canvas.create_line(0, CELL_SIZE*n, CANVAS_SIZE, CELL_SIZE*n, width=GRID_LINE_WIDTH, fill=GRID_COLOR) 
			d = ((CANVAS_SIZE/6)*1)


	def draw_XO(self, symbol, grid_cords, anime: bool, ext=0):
		pixel_cords = self.grid_to_pixel(grid_cords)
		x = pixel_cords[0] if not anime else grid_cords[0]
		y = pixel_cords[1] if not anime else grid_cords[1]
		delta = CELL_SIZE/2*SYMBOL_SIZE

		if symbol == 'X':
			self.canvas.create_line( x+delta, y-delta, x-delta, y+delta, width=SYMBOL_WIDTH+ext, fill=X_COLOR)
			self.canvas.create_line( x-delta, y-delta, x+delta, y+delta, width=SYMBOL_WIDTH+ext, fill=X_COLOR)
		else:
			self.canvas.create_oval(x-delta, y-delta, x+delta, y+delta, width=SYMBOL_WIDTH+ext, outline=O_COLOR)


	def grid_to_pixel(self, grid_cords:tuple):
		x = grid_cords[0] * CELL_SIZE + CELL_SIZE / 2
		y = grid_cords[1] * CELL_SIZE + CELL_SIZE / 2
		return (x,y)


	def pixel_to_grid(self, pixel_cords:tuple):
		if pixel_cords[0] < CANVAS_SIZE and pixel_cords[1] < CANVAS_SIZE:
			grid_cord = (int(pixel_cords[0] / CELL_SIZE),int(pixel_cords[1] / CELL_SIZE))
			return grid_cord


	def gameover_anime(self, winner, play_again_func):
		wintext = 'WINNER!' if winner != 'draw' else 'DRAW!'
		x = CANVAS_SIZE/2
		y = CANVAS_SIZE/3

		self.canvas.delete('all')
		if winner == 'draw':
			self.draw_XO('O', ((CANVAS_SIZE/2)+30,y), True, 2)
			self.draw_XO('X', ((CANVAS_SIZE/2)-30,y), True, 2)
		else:
			self.draw_XO(winner, (x,y), True, 2)

		self.whose_turn.config(text="Game Over", cursor='arrow')
		self.canvas.create_text(int(CANVAS_SIZE/2), int(CANVAS_SIZE/1.8), text=wintext, fill=X_COLOR, font=('Ariel', int(-CANVAS_SIZE/7), 'bold'))
		self.game_modes.destroy()
		self.new_game.config(text='', cursor='arrow')
		self.restart.config(text='Play Again')
		self.restart.grid(pady=5)
		self.restart.bind('<Button-1>', play_again_func)


	def gameover(self, winner, play_again_func):
		self.unbind_widgets()
		self.after(1000, self.gameover_anime, winner, play_again_func)


	def unbind_widgets(self):
		self.canvas.config(cursor='arrow')
		self.canvas.unbind('<Button-1>')
		self.new_game.unbind('<Button-1>')
		self.restart.unbind('<Button-1>')


	def alert(self, text, pos):
		self.alert_msg = Label(text=text, bg='white', font=('Monospace', 10, 'bold'))
		if pos == 'top':
			self.alert_msg.grid(row=0, column=0, columnspan=3)
		elif pos == 'bottom': 
			self.alert_msg.grid(row=2, column=0, columnspan=3)
		self.whose_turn.unbind('Button-1')
		self.after(1500, self.alert_msg.destroy)



	