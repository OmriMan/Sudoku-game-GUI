import Grid
import Cell
import SubGrid
import copy

import SudokuGUI
from tkinter import Tk, Label, StringVar, Button, Entry,messagebox

class SubGUI:

    def __init__(self,matrix=None):
        window = Tk()
        window.title("Sudoku")
        window.geometry("800x600+120+12")
        window.configure(bg='Ivory')
        window.resizable(False, False)
        window.attributes
        Label(window, text="Sudoku", font=('arial', 50, 'bold'),
              bg="Ivory").place(x=265, y=20)

        sg1 = SubGrid.SubGrid(0, [Cell.Cell(0, 0, 3), Cell.Cell(0, 1, 7), Cell.Cell(0, 2, 4), Cell.Cell(1, 0, 1),
                                  Cell.Cell(1, 1, 8), Cell.Cell(1, 2, 5), Cell.Cell(2, 0, 9), Cell.Cell(2, 1, 6),
                                  Cell.Cell(2, 2, 2)])
        sg2 = SubGrid.SubGrid(1, [Cell.Cell(0, 0, 1), Cell.Cell(0, 1, 6), Cell.Cell(0, 2, 5), Cell.Cell(1, 0, 9),
                                  Cell.Cell(1, 1, 2), Cell.Cell(1, 2, 4), Cell.Cell(2, 0, 8), Cell.Cell(2, 1, 7)])
        sg3 = SubGrid.SubGrid(2, [Cell.Cell(0, 0, 9), Cell.Cell(0, 1, 2), Cell.Cell(0, 2, 8), Cell.Cell(1, 0, 7),
                                  Cell.Cell(1, 1, 6), Cell.Cell(1, 2, 3), Cell.Cell(2, 0, 4), Cell.Cell(2, 1, 1),
                                  Cell.Cell(2, 2, 5)])
        sg4 = SubGrid.SubGrid(3, [Cell.Cell(0, 0, 5), Cell.Cell(0, 1, 3), Cell.Cell(0, 2, 1), Cell.Cell(1, 0, 6),
                                  Cell.Cell(1, 1, 4), Cell.Cell(1, 2, 9), Cell.Cell(2, 0, 8), Cell.Cell(2, 1, 2),
                                  Cell.Cell(2, 2, 7)])
        sg5 = SubGrid.SubGrid(4, [Cell.Cell(0, 0, 4), Cell.Cell(0, 1, 8), Cell.Cell(0, 2, 9), Cell.Cell(1, 0, 7),
                                  Cell.Cell(1, 1, 5), Cell.Cell(1, 2, 2), Cell.Cell(2, 0, 3), Cell.Cell(2, 1, 1),
                                  Cell.Cell(2, 2, 6)])
        sg6 = SubGrid.SubGrid(5, [Cell.Cell(0, 0, 6), Cell.Cell(0, 1, 7), Cell.Cell(0, 2, 2), Cell.Cell(1, 0, 8),
                                  Cell.Cell(1, 1, 3), Cell.Cell(1, 2, 1), Cell.Cell(2, 0, 5), Cell.Cell(2, 1, 4),
                                  Cell.Cell(2, 2, 9)])
        sg7 = SubGrid.SubGrid(6, [Cell.Cell(0, 0, 4), Cell.Cell(0, 1, 9), Cell.Cell(0, 2, 6), Cell.Cell(1, 0, 2),
                                  Cell.Cell(1, 1, 1), Cell.Cell(1, 2, 8), Cell.Cell(2, 0, 7), Cell.Cell(2, 1, 5)])
        sg8 = SubGrid.SubGrid(7, [Cell.Cell(0, 0, 2), Cell.Cell(0, 1, 3), Cell.Cell(0, 2, 8), Cell.Cell(1, 0, 5),
                                  Cell.Cell(1, 1, 4), Cell.Cell(1, 2, 7), Cell.Cell(2, 0, 6), Cell.Cell(2, 1, 9),
                                  Cell.Cell(2, 2, 1)])
        sg9 = SubGrid.SubGrid(8, [Cell.Cell(0, 0, 1), Cell.Cell(0, 1, 5), Cell.Cell(0, 2, 7), Cell.Cell(1, 0, 3),
                                  Cell.Cell(1, 1, 9), Cell.Cell(1, 2, 6), Cell.Cell(2, 1, 8), Cell.Cell(2, 0, 2),
                                  Cell.Cell(2, 2, 4)])

        self.g = Grid.Grid([sg1, sg2, sg3, sg4, sg5, sg6, sg7, sg8, sg9])
        copy_g = copy.deepcopy(self.g)
        copy_g.solve()
        self.sol_matrix = copy_g.getGrid()
        self.matrix = self.g.getGrid()
        self.window = window
        button= SudokuGUI.GlowButton(window,text="Play", font=('arial', 35), bg="LightCyan", width=15, command=self.play_)
        button.place(x=180,y=140)
        button= SudokuGUI.GlowButton(window,text="How to play", font=('arial', 25), bg="Ivory", width=15, command=self.how_to_play)
        button.place(x=245,y=240)
        button= SudokuGUI.GlowButton(window,text="About", font=('arial', 25), bg="Ivory", width=15, command=self.play_)
        button.place(x=245,y=310)
        button= SudokuGUI.GlowButton(window,text="Help", font=('arial', 25), bg="Ivory", width=15, command=self.play_)
        button.place(x=245,y=380)


        self.window.mainloop()


    def play_(self):
        g = self.g
        self.window.destroy()
        SudokuGUI.SudokuGUI(g,my_first=True)

    def how_to_play(self):
        messagebox.showinfo("How to play","First of all, if you do not know the rules please learn them (you can read them in the \"Help\" tab)\n\nYou must fill in all the blank squares (painted pink) in the digits.\nIf you made a mistake, the square will be painted red\n\nYou can use the small and white squares, they will be used as a draft and are not considered part of the game\n\n\nit's important to remember ! If you do not succeed you can always use the \"Solve\" button but this is a loser's action!")


SubGUI()
