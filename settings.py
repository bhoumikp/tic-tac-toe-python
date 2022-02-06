from os import path

# Loading
WAIT_TIME = 3000
LOAD_DELAY = 500


# UI
BG = "#14bdac"
WINDOW_SIZE = 370
CELL_SIZE = WINDOW_SIZE / 3
SYMBOL_SIZE = 0.375
SYMBOL_WIDTH = WINDOW_SIZE/50
X_COLOR = '#545454'
O_COLOR = '#f2ebd3'
GRID_LINE_WIDTH = 6
DRAW_SCREEN_COLOR = 'light sea green'
GRID_COLOR = '#0da192'
LOGO_PATH = path.join(path.dirname(__file__), 'logo.png')

# Game 
FIRST_PLAYER = 'O'
EMPTY = 0
GAME_MODE = '2P'