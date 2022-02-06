from game import Game

root = Game()
root.ui.loading_screen()
root.ui.after(2500, root.start)

root.ui.mainloop()