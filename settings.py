from os import path

# Loading
WAIT_TIME = 3000
LOAD_DELAY = 500

# UI
FONT_SIZE = 10
BG = "#14bdac"
CANVAS_SIZE = 370
CELL_SIZE = CANVAS_SIZE / 3
SYMBOL_SIZE = 0.375
SYMBOL_WIDTH = CANVAS_SIZE/50
X_COLOR = '#545454'
O_COLOR = '#f2ebd3'
GRID_LINE_WIDTH = 6
DRAW_SCREEN_COLOR = 'light sea green'
GRID_COLOR = '#0da192'
LOGO_PATH = path.join(path.dirname(__file__), 'logo.png')
GAME_MODES = ['Easy', 'Medium', 'Hard', '2P']

# Game 
FIRST_PLAYER = 'X'
EMPTY = 0
GAME_MODE = 'Medium'
ROWS = 3
COLS = 3