from settings import *
from game import Game

root = Game()
root.ui.loading_screen()
root.ui.after(WAIT_TIME, root.start)

root.ui.mainloop()

