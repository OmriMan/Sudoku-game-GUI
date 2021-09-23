from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wrapprStartScreen import NewGame

import Grid
import Cell
import SubGrid
import copy
from random import randint
import open_pickle_file_of_dict_tables_to_python_dict

from tkinter import Tk, Label, StringVar, Button, Entry,messagebox,StringVar,Menu
from collections import deque

class GlowButton(Button):
    def __init__(self, master, **kwargs):
        Button.__init__(self, master, **kwargs)
        # store background color
        self.bg_idle = self.cget('background')

        # list of glow colors to cycle through
        self.colors = ['#aa88aa', '#aa99aa', '#aaaaaa', '#aabbaa', '#aaccaa', '#aaddaa', '#aaeeaa', '#aaffaa']
        # deque to use as an offset
        self.col_index = deque(range(len(self.colors)))
        # eventual reference to after
        self.glow = None

        # add MouseOver, MouseOut events
        self.bind('<Enter>', lambda e: self.__glow(True))
        self.bind('<Leave>', lambda e: self.__glow(False))

    def __glow(self, hover):
        if hover:
            # get rotation offset
            ofs = self.col_index.index(0)
            # apply color from rotation offset
            self.configure(background=self.colors[ofs])
            # if the offset has not reached the end of the color list
            if ofs != len(self.colors) - 1:
                # rotate
                self.col_index.rotate(1)
                # do all of this again in 50ms
                self.glow = self.after(50, self.__glow, hover)
        else:
            # kill any expected after
            self.after_cancel(self.glow)
            # rewind
            self.col_index.rotate(-self.col_index.index(0))
            # reset to idle color
            self.configure(background=self.bg_idle)

class GlowEntry(Entry):
    def __init__(self, master, **kwargs):
        Entry.__init__(self, master, **kwargs)
        # store background color
        self.bg_idle = self.cget('background')

        # list of glow colors to cycle through
        self.colors = ['#aa88aa', '#aa99aa', '#aaaaaa', '#aabbaa', '#aaccaa', '#aaddaa', '#aaeeaa', '#aaffaa']
        # deque to use as an offset
        self.col_index = deque(range(len(self.colors)))
        # eventual reference to after
        self.glow = None

        # add MouseOver, MouseOut events
        self.bind('<Enter>', lambda e: self.__glow(True))
        self.bind('<Leave>', lambda e: self.__glow(False))

    def __glow(self, hover):
        if hover:
            # get rotation offset
            ofs = self.col_index.index(0)
            # apply color from rotation offset
            self.configure(background=self.colors[ofs])
            # if the offset has not reached the end of the color list
            if ofs != len(self.colors) - 1:
                # rotate
                self.col_index.rotate(1)
                # do all of this again in 50ms
                self.glow = self.after(50, self.__glow, hover)
        else:
            # kill any expected after
            self.after_cancel(self.glow)
            # rewind
            self.col_index.rotate(-self.col_index.index(0))
            # reset to idle color
            self.configure(background=self.bg_idle)
class SudokuGUI:

        def __init__(self,g,copy_g = None,my_first=None):
                window = Tk()
                window.title("Sudoku")
                window.geometry("900x600+120+12")
                window.configure(bg='Ivory')
                window.resizable(False, False)
                window.attributes
                Label(window, text="Sudoku", font=('arial', 25, 'bold'),
                      bg="Ivory").place(x=70, y=20)
                self.error_matrix = []
                for i in range(9):
                    self.error_matrix.append([])
                    for j in range(9):
                        self.error_matrix[i].append(0)
                self.text_var = []
                self.entries =[]
                self.help_window = []
                self.rows=9
                self.cols=9
                self.g = g #main grid
                if (copy_g == None):
                    self.copy_g = copy.deepcopy(self.g)
                    self.copy_g.solve()
                else:
                    self.copy_g = copy_g
                self.window = window #main window

                self.matrix = self.g.getGrid()
                self.sol_matrix = self.copy_g.getGrid()
                self.window = window
                global me
                me = self
                global time_counter
                global minute
                time_counter = 0
                minute = 0
                global finish
                finish = False
                def button_count(i, label_sec, label_minute):
                    global time_counter
                    global minute
                    global finish
                    if (time_counter == 60):
                        time_counter = 0
                        minute += 1
                    if (finish == True):
                        label_sec.set(0)
                        label_minute.set(0)
                    else:
                        time_counter += 1
                        label_sec.set(time_counter)
                        label_minute.set(minute)
                        timer = window.after(1000, lambda: button_count(time_counter, label_sec, label_minute))

                button_label_minute = StringVar()
                button_label_minute.set(0)
                button_label = StringVar()
                button_label.set(0)
                Label(window, text="Time:", font=('arial', 22), bg="Ivory").place(x=555, y=25)
                GlowButton(window, textvariable=button_label,font=('arial', 18, 'bold'), bg="Ivory",width = 3).place(x=690, y=20)
                GlowButton(window, textvariable=button_label_minute, font=('arial', 18, 'bold'), bg="Ivory",width = 3).place(x=635, y=20)

                button_count(time_counter, button_label, button_label_minute)
                '''
                sg1 = SubGrid.SubGrid(0,[Cell.Cell(0, 0, 3), Cell.Cell(0, 1, 7), Cell.Cell(0, 2, 4), Cell.Cell(1, 0, 1),
                                       Cell.Cell(1, 1, 8), Cell.Cell(1, 2, 5), Cell.Cell(2, 0, 9), Cell.Cell(2, 1, 6),
                                       Cell.Cell(2, 2, 2)])
                sg2 = SubGrid.SubGrid(1,[Cell.Cell(0, 0, 1), Cell.Cell(0, 1, 6), Cell.Cell(0, 2, 5), Cell.Cell(1, 0, 9),
                                       Cell.Cell(1, 1, 2), Cell.Cell(1, 2, 4), Cell.Cell(2, 0, 8), Cell.Cell(2, 1, 7)])
                sg3 = SubGrid.SubGrid(2,[Cell.Cell(0, 0, 9), Cell.Cell(0, 1, 2), Cell.Cell(0, 2, 8), Cell.Cell(1, 0, 7),Cell.Cell(1, 1, 6), Cell.Cell(1, 2, 3), Cell.Cell(2, 0, 4), Cell.Cell(2, 1, 1),Cell.Cell(2, 2, 5)])
                sg4 = SubGrid.SubGrid(3,[Cell.Cell(0, 0, 5), Cell.Cell(0, 1, 3), Cell.Cell(0, 2, 1), Cell.Cell(1, 0, 6),
                                       Cell.Cell(1, 1, 4), Cell.Cell(1, 2, 9), Cell.Cell(2, 0, 8), Cell.Cell(2, 1, 2),
                                       Cell.Cell(2, 2, 7)])
                sg5 = SubGrid.SubGrid(4,
                                      [Cell.Cell(0, 0, 4), Cell.Cell(0, 1, 8), Cell.Cell(0, 2, 9), Cell.Cell(1, 0, 7),
                                       Cell.Cell(1, 1, 5), Cell.Cell(1, 2, 2), Cell.Cell(2, 0, 3), Cell.Cell(2, 1, 1),
                                       Cell.Cell(2, 2, 6)])
                sg6 = SubGrid.SubGrid(5,
                                      [Cell.Cell(0, 0, 6), Cell.Cell(0, 1, 7), Cell.Cell(0, 2, 2), Cell.Cell(1, 0, 8),
                                       Cell.Cell(1, 1, 3), Cell.Cell(1, 2, 1), Cell.Cell(2, 0, 5), Cell.Cell(2, 1, 4),
                                       Cell.Cell(2, 2, 9)])
                sg7 = SubGrid.SubGrid(6,
                                      [Cell.Cell(0, 0, 4), Cell.Cell(0, 1, 9), Cell.Cell(0, 2, 6), Cell.Cell(1, 0, 2),
                                       Cell.Cell(1, 1, 1), Cell.Cell(1, 2, 8), Cell.Cell(2, 0, 7), Cell.Cell(2, 1, 5)])
                sg8 = SubGrid.SubGrid(7,
                                      [Cell.Cell(0, 0, 2), Cell.Cell(0, 1, 3), Cell.Cell(0, 2, 8), Cell.Cell(1, 0, 5),
                                       Cell.Cell(1, 1, 4), Cell.Cell(1, 2, 7), Cell.Cell(2, 0, 6), Cell.Cell(2, 1, 9),
                                       Cell.Cell(2, 2, 1)])
                sg9 = SubGrid.SubGrid(8,
                                      [Cell.Cell(0, 0, 1), Cell.Cell(0, 1, 5), Cell.Cell(0, 2, 7), Cell.Cell(1, 0, 3),
                                       Cell.Cell(1, 1, 9), Cell.Cell(1, 2, 6), Cell.Cell(2, 1, 8), Cell.Cell(2, 0, 2),
                                       Cell.Cell(2, 2, 4)])
                
                self.subgrid_dict={}
                self.subgrid_dict['11'] = (0,[Cell.Cell(0, 0, 3), Cell.Cell(0, 1, 7), Cell.Cell(0, 2, 4), Cell.Cell(1, 0, 1),Cell.Cell(1, 1, 8), Cell.Cell(1, 2, 5), Cell.Cell(2, 0, 9), Cell.Cell(2, 1, 6), Cell.Cell(2, 2, 2)])
                self.subgrid_dict['12'] =(1,[Cell.Cell(0, 0, 1), Cell.Cell(0, 1, 6), Cell.Cell(0, 2, 5), Cell.Cell(1, 0, 9),Cell.Cell(1, 1, 2), Cell.Cell(1, 2, 4), Cell.Cell(2, 0, 8), Cell.Cell(2, 1, 7)])
                self.subgrid_dict['13'] =(2,[Cell.Cell(0, 0, 9), Cell.Cell(0, 1, 2), Cell.Cell(0, 2, 8), Cell.Cell(1, 0, 7),Cell.Cell(1, 1, 6), Cell.Cell(1, 2, 3), Cell.Cell(2, 0, 4), Cell.Cell(2, 1, 1),Cell.Cell(2, 2, 5)])
                self.subgrid_dict['14'] =(3,[Cell.Cell(0, 0, 5), Cell.Cell(0, 1, 3), Cell.Cell(0, 2, 1), Cell.Cell(1, 0, 6),
                                       Cell.Cell(1, 1, 4), Cell.Cell(1, 2, 9), Cell.Cell(2, 0, 8), Cell.Cell(2, 1, 2),
                                       Cell.Cell(2, 2, 7)])
                self.subgrid_dict['15'] =(4,
                                      [Cell.Cell(0, 0, 4), Cell.Cell(0, 1, 8), Cell.Cell(0, 2, 9), Cell.Cell(1, 0, 7),
                                       Cell.Cell(1, 1, 5), Cell.Cell(1, 2, 2), Cell.Cell(2, 0, 3), Cell.Cell(2, 1, 1),
                                       Cell.Cell(2, 2, 6)])
                self.subgrid_dict['16'] =(5,
                                      [Cell.Cell(0, 0, 6), Cell.Cell(0, 1, 7), Cell.Cell(0, 2, 2), Cell.Cell(1, 0, 8),
                                       Cell.Cell(1, 1, 3), Cell.Cell(1, 2, 1), Cell.Cell(2, 0, 5), Cell.Cell(2, 1, 4),
                                       Cell.Cell(2, 2, 9)])
                self.subgrid_dict['17'] =(6,
                                      [Cell.Cell(0, 0, 4), Cell.Cell(0, 1, 9), Cell.Cell(0, 2, 6), Cell.Cell(1, 0, 2),
                                       Cell.Cell(1, 1, 1), Cell.Cell(1, 2, 8), Cell.Cell(2, 0, 7), Cell.Cell(2, 1, 5)])
                self.subgrid_dict['18'] =(7,
                                      [Cell.Cell(0, 0, 2), Cell.Cell(0, 1, 3), Cell.Cell(0, 2, 8), Cell.Cell(1, 0, 5),
                                       Cell.Cell(1, 1, 4), Cell.Cell(1, 2, 7), Cell.Cell(2, 0, 6), Cell.Cell(2, 1, 9),
                                       Cell.Cell(2, 2, 1)])
                self.subgrid_dict['19'] =(8,
                                      [Cell.Cell(0, 0, 1), Cell.Cell(0, 1, 5), Cell.Cell(0, 2, 7), Cell.Cell(1, 0, 3),
                                       Cell.Cell(1, 1, 9), Cell.Cell(1, 2, 6), Cell.Cell(2, 1, 8), Cell.Cell(2, 0, 2),
                                       Cell.Cell(2, 2, 4)])
                '''

                #def donothing():
                #    messagebox.showinfo("What are you doing here ?!","Hi !\nApologies for the temporary inconvenience, we are working very hard on this game but we have not yet managed to implement this function ... :-(\n\nMaybe a small donation will help us upgrade and succeed in realizing this function ;-)")


                menubar = Menu(self.window)
                filemenu = Menu(menubar, tearoff=0)
                filemenu.add_command(label="New", command=self.new_game)
                filemenu.add_command(label="Open", command=self.donothing)
                filemenu.add_command(label="Save", command=self.donothing)
                filemenu.add_command(label="Save as...", command=self.donothing)
                filemenu.add_command(label="Close", command=self.new_game)

                filemenu.add_separator()

                filemenu.add_command(label="Exit", command=self.window.quit)
                menubar.add_cascade(label="File", menu=filemenu)
                helpmenu = Menu(menubar, tearoff=0)
                helpmenu.add_command(label="Rules", command=self.rules)
                helpmenu.add_command(label="How to play", command=self.how_to_play)
                helpmenu.add_command(label="About...", command=self.donothing)
                menubar.add_cascade(label="Help", menu=helpmenu)
                editmenu = Menu(menubar, tearoff=0)
                editmenu.add_command(label="Save & Exit", command=self.donothing)
                editmenu.add_separator()
                editmenu.add_command(label="Exit", command=self.donothing)

                menubar.add_cascade(label="Exit", menu=editmenu)
                self.hide_sol(first=my_first)
                self.window.config(menu=menubar)
                self.window.mainloop()


        def donothing(self):
            messagebox.showinfo("What are you doing here ?!","Hi !\nApologies for the temporary inconvenience, we are working very hard on this game but we have not yet managed to implement this function ... :-(\n\nMaybe a small donation will help us upgrade and succeed in realizing this function ;-)")

        def how_to_play(self):
            messagebox.showinfo("How to play",
                                "First of all, if you do not know the rules please learn them (you can read them in the \"Help\" tab)\n\nYou must fill in all the blank squares (painted pink) in the digits.\nIf you made a mistake, the square will be painted red\n\nYou can use the small and white squares, they will be used as a draft and are not considered part of the game\n\n\nit's important to remember ! If you do not succeed you can always use the \"Solve\" button but this is a loser's action!")

        def rules(self):
            messagebox.showinfo("Rules","Sudoku is a puzzle based on a small number of very simple rules:\nEvery square has to contain a single number\nOnly the numbers from 1 through to 9 can be used\nEach 3×3 box can only contain each number from 1 to 9 once\nEach vertical column can only contain each number from 1 to 9 once\nEach horizontal row can only contain each number from 1 to 9 once\nOnce the puzzle is solved, this means that every row, column, and 3×3 box will contain every number from 1 to 9 exactly once.\nIn other words, no number can be repeated in any 3×3 box, row, or column. ")

        def new_game(self,first_temp=None):
            if first_temp==None:
                messagebox.showinfo("Generate a new Sudoku","You will not be able to return to the game you just played!\nHope you have a good memory or you took a screenshot ;-)")
            self.window.destroy()
            window = Tk()
            window.title("Sudoku")
            window.geometry("800x600+120+12")
            window.configure(bg='Ivory')
            window.resizable(False, False)
            window.attributes
            Label(window, text="Sudoku", font=('arial', 50, 'bold'),
                  bg="Ivory").place(x=265, y=20)
            '''
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
            '''
            self.window = window
            button = GlowButton(window, text="Easy", font=('arial', 15), bg="LightCyan", width=15, command=self.play_easy)
            button.place(x=300, y=120)
            button = GlowButton(window, text="Medium", font=('arial', 15), bg="LightCyan", width=15, command=self.play_med)
            button.place(x=300, y=200)
            button = GlowButton(window, text="Hard", font=('arial', 15), bg="LightCyan", width=15, command=self.play_hard)
            button.place(x=300, y=280)
            button = GlowButton(window, text="Expert", font=('arial', 15), bg="LightCyan", width=15, command=self.play_expert)
            button.place(x=300, y=360)
            button = GlowButton(window, text="Invisible", font=('arial', 15), bg="LightCyan", width=15,  command=self.play_Invisible)
            button.place(x=300, y=440)
            menubar = Menu(self.window)
            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="New", command=self.new_game)
            filemenu.add_command(label="Open", command=self.donothing)
            filemenu.add_command(label="Save", command=self.donothing)
            filemenu.add_command(label="Save as...", command=self.donothing)
            filemenu.add_command(label="Close", command=self.new_game)

            filemenu.add_separator()

            filemenu.add_command(label="Exit", command=self.window.quit)
            menubar.add_cascade(label="File", menu=filemenu)
            helpmenu = Menu(menubar, tearoff=0)
            helpmenu.add_command(label="Rules", command=self.rules)
            helpmenu.add_command(label="How to play", command=self.how_to_play)
            helpmenu.add_command(label="About...", command=self.donothing)
            menubar.add_cascade(label="Help", menu=helpmenu)
            editmenu = Menu(menubar, tearoff=0)
            editmenu.add_command(label="Save & Exit", command=self.donothing)
            editmenu.add_separator()
            editmenu.add_command(label="Exit", command=self.donothing)

            menubar.add_cascade(label="Exit", menu=editmenu)

            self.window.config(menu=menubar)

            self.window.mainloop()

        def play_easy(self):
            big_list_of_grids = open_pickle_file_of_dict_tables_to_python_dict.give_me_list_of_grid_dict()
            self.subgrid_dict = big_list_of_grids[(randint(0, len(big_list_of_grids)-1))]
            subgrid_list=[]
            for i in self.subgrid_dict.keys():
                copy_subgrid= self.subgrid_dict[i][1]
                subgrid_list.append(SubGrid.SubGrid(self.subgrid_dict[i][0], copy_subgrid))
            copy_g = Grid.Grid(subgrid_list)
            copy_g.solve()
            self.sol_matrix = copy_g.getGrid()
            subgrid_list=[]
            for i in self.subgrid_dict.keys():
                copy_subgrid= copy.deepcopy(self.subgrid_dict[i][1])
                for j in range(2):
                    copy_subgrid.pop(randint(0, len(copy_subgrid)-1))
                subgrid_list.append(SubGrid.SubGrid(self.subgrid_dict[i][0],copy_subgrid))
            self.g = Grid.Grid(subgrid_list)
            self.matrix = self.g.getGrid()
            self.window.destroy()
            SudokuGUI(self.g,copy_g)

        def play_med(self):
            big_list_of_grids = open_pickle_file_of_dict_tables_to_python_dict.give_me_list_of_grid_dict()
            self.subgrid_dict = big_list_of_grids[(randint(0, len(big_list_of_grids)-1))]
            subgrid_list=[]
            for i in self.subgrid_dict.keys():
                copy_subgrid= self.subgrid_dict[i][1]
                subgrid_list.append(SubGrid.SubGrid(self.subgrid_dict[i][0], copy_subgrid))
            copy_g = Grid.Grid(subgrid_list)
            copy_g.solve()
            self.sol_matrix = copy_g.getGrid()
            subgrid_list=[]
            for i in self.subgrid_dict.keys():
                copy_subgrid= copy.deepcopy(self.subgrid_dict[i][1])
                for j in range(4):
                    copy_subgrid.pop(randint(0, len(copy_subgrid)-1))
                subgrid_list.append(SubGrid.SubGrid(self.subgrid_dict[i][0],copy_subgrid))
            self.g = Grid.Grid(subgrid_list)
            self.window.destroy()
            SudokuGUI(self.g,copy_g)

        def play_hard(self):
            big_list_of_grids = open_pickle_file_of_dict_tables_to_python_dict.give_me_list_of_grid_dict()
            self.subgrid_dict = big_list_of_grids[(randint(0, len(big_list_of_grids)-1))]
            subgrid_list=[]
            for i in self.subgrid_dict.keys():
                copy_subgrid= self.subgrid_dict[i][1]
                subgrid_list.append(SubGrid.SubGrid(self.subgrid_dict[i][0], copy_subgrid))
            copy_g = Grid.Grid(subgrid_list)
            copy_g.solve()
            self.sol_matrix = copy_g.getGrid()
            subgrid_list=[]
            for i in self.subgrid_dict.keys():
                copy_subgrid= copy.deepcopy(self.subgrid_dict[i][1])
                for j in range(5):
                    copy_subgrid.pop(randint(0, len(copy_subgrid)-1))
                subgrid_list.append(SubGrid.SubGrid(self.subgrid_dict[i][0],copy_subgrid))
            self.g = Grid.Grid(subgrid_list)
            self.window.destroy()
            SudokuGUI(self.g,copy_g)

        def play_expert(self):
            big_list_of_grids = open_pickle_file_of_dict_tables_to_python_dict.give_me_list_of_grid_dict()
            self.subgrid_dict = big_list_of_grids[(randint(0, len(big_list_of_grids)-1))]
            subgrid_list=[]
            for i in self.subgrid_dict.keys():
                copy_subgrid= self.subgrid_dict[i][1]
                subgrid_list.append(SubGrid.SubGrid(self.subgrid_dict[i][0], copy_subgrid))
            copy_g = Grid.Grid(subgrid_list)
            copy_g.solve()
            self.sol_matrix = copy_g.getGrid()
            subgrid_list=[]
            for i in self.subgrid_dict.keys():
                copy_subgrid= copy.deepcopy(self.subgrid_dict[i][1])
                for j in range(7):
                    copy_subgrid.pop(randint(0, len(copy_subgrid)-1))
                subgrid_list.append(SubGrid.SubGrid(self.subgrid_dict[i][0],copy_subgrid))
            self.g = Grid.Grid(subgrid_list)
            self.window.destroy()
            SudokuGUI(self.g,copy_g)

        def play_Invisible(self):
            big_list_of_grids = open_pickle_file_of_dict_tables_to_python_dict.give_me_list_of_grid_dict()
            self.subgrid_dict = big_list_of_grids[(randint(0, len(big_list_of_grids)-1))]
            subgrid_list=[]
            for i in self.subgrid_dict.keys():
                copy_subgrid= self.subgrid_dict[i][1]
                subgrid_list.append(SubGrid.SubGrid(self.subgrid_dict[i][0], copy_subgrid))
            copy_g = Grid.Grid(subgrid_list)
            copy_g.solve()
            self.sol_matrix = copy_g.getGrid()
            subgrid_list=[]
            for i in self.subgrid_dict.keys():
                copy_subgrid= copy.deepcopy(self.subgrid_dict[i][1])
                range_j = len(copy_subgrid)
                for j in range(range_j ):
                    copy_subgrid.pop(randint(0, len(copy_subgrid)-1))
                subgrid_list.append(SubGrid.SubGrid(self.subgrid_dict[i][0],copy_subgrid))
            self.g = Grid.Grid(subgrid_list)
            self.window.destroy()
            SudokuGUI(self.g,copy_g)



        def getMatrix(self):
            return self.matrix


        # Getters and setters
        def getMatrixAtIndex(self, i, j):
            return self.matrix[i][j]

        def getSolMatrix(self):
            return self.sol_matrix


        def getSolMatrixAtIndex(self, i, j):
            return self.sol_matrix[i][j]

        def setMatrixATIndexWithVal(self,i, j, val):
            self.matrix[i][j] = val

        def setErrorMatrix_With_Zero(self,i, j):
            self.error_matrix[i][j] = 0

        def setErrorMatrix_With_Val(self,i, j, val):
            self.error_matrix[i][j] = val

        def setOriginalMatrix_With_SolMatrixVal(self,i, j):
            self.matrix[i][j] = self.sol_matrix[i][j]
            if (self.matrix == self.sol_matrix):
                # messagebox.showinfo("Winner", "You managed to solve the sudoku! Time for solution:{} minute and {} seconds ! ".format(minute, time_counter))
                global finish
                finish=True
                messagebox.showinfo("Winner",
                                        "You managed to solve the sudoku! Time for solution:\n --- {} : {} --- \n".format(
                                            minute, time_counter))
                print("0{} : 0{}".format(minute, time_counter))
                """              
                def getName():
                    pname = ''
                    Label(window, text=f'{pname}, Cool !', pady=50, bg='#ffbf00').pack()
                    pname = player_name.get()
                    # try_save_list_as_file.add_easy_player(pname,20,1)
                    add_easy_player(pname, minute, time_counter)
                    show_Easy_Table()

                player_name = GlowEntry(me.window)
                player_name.pack(pady=30)
                GlowButton(self.window, text="that's my name", padx=10, pady=5, command=getName).pack()
                """
                # TODO
                # win_game()

        def show_sol(self):
            self.text_var = []
            self.entries = []
            #self.copy_g = copy.deepcopy(self.g)
            #self.copy_g.solve()
            self.sol_matrix = self.copy_g.getGrid()
            x2 = 0
            y2 = 0
            rows, cols = (9, 9)
            for i in range(self.rows):
                # append an empty list to your two arrays
                # so you can append to those later
                if i % 3 == 0:
                    y2 += 10
                self.text_var.append([])
                self.entries.append([])
                for j in range(self.cols):
                    if j % 3 == 0:
                        x2 += 15
                    CellText = StringVar()
                    CellText.set(self.sol_matrix[i][j])
                    self.text_var[i].append(CellText)
                    # append your StringVar and Entry
                    self.entries[i].append(GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 25", justify="center", width=4,
                                  bg="LightBlue", fg="black", bd=3, cursor="dot"))
                    self.entries[i][j].place(x=60 + x2, y=70 + y2)
                    x2 += 80
                y2 += 50
                x2 = 0
                button = GlowButton(self.window, text="Back", font="arial 15 bold", justify="center", bg="Ivory", fg="DarkRed", width=11, command=self.hide_sol)
                button.place(x=380, y=25)
                button = GlowButton(self.window, text="New Game", font="arial 15 bold", justify="center", bg="Ivory", fg="MediumSeaGreen", width=11, command=self.new_game)
                button.place(x=230, y=25)



        def user_good_sol(self):
            self.text_var = []
            self.entries = []
            #self.copy_g = copy.deepcopy(self.g)
            #self.copy_g.solve()
            self.sol_matrix = self.copy_g.getGrid()
            self.window.title("WINNER")
            #self.window.geometry("650x500+120+120")
            self.window.configure(bg='Ivory')
            button_label_minute = StringVar()
            button_label_minute.set(minute)
            button_label = StringVar()
            button_label.set(time_counter)
            x2 = 0
            y2 = 0
            rows, cols = (9, 9)
            for i in range(self.rows):
                # append an empty list to your two arrays
                # so you can append to those later
                if i % 3 == 0:
                    y2 += 10
                self.text_var.append([])
                self.entries.append([])
                for j in range(self.cols):
                    if j % 3 == 0:
                        x2 += 15
                    CellText = StringVar()
                    CellText.set(self.sol_matrix[i][j])
                    self.text_var[i].append(CellText)
                    # append your StringVar and Entry
                    self.entries[i].append(GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 25 bold", justify="center", width=4,
                                  bg="Cornsilk", fg="DarkBlue", bd=3, cursor="dot"))
                    self.entries[i][j].place(x=60 + x2, y=70 + y2)
                    x2 += 80
                y2 += 50
                x2 = 0
                button = GlowButton(self.window, text="Solve", font="arial 15 bold", justify="center", bg="Ivory", fg="DarkRed", width=11, command=self.show_sol)
                button.place(x=380, y=25)
                button = GlowButton(self.window, text="New Game", font="arial 15 bold", justify="center", bg="Ivory", fg="MediumSeaGreen", width=11, command=self.new_game)
                button.place(x=230, y=25)


        def user_wrong_sol(self,r, c, val):
            self.text_var = []
            self.entries = []
            self.help_window = []
            x2 = 0
            y2 = 0
            rows, cols = (9, 9)
            for i in range(self.rows):
                # append an empty list to your two arrays
                # so you can append to those later
                self.text_var.append([])
                self.entries.append([])
                self.help_window.append([])
                if i % 3 == 0:
                    y2 += 10
                for j in range(self.cols):
                    # append your StringVar and Entry
                    if j % 3 == 0:
                        x2 += 15
                    func_name = "Key_Press{}{}".format(i, j)
                    func_to_run = globals()[func_name]
                    if (i == r and j == c):
                        CellText = StringVar()
                        CellText.set(val)
                        self.text_var[i].append(CellText)
                        self.entries[i].append(
                            GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 25", justify="center",
                                      width=4, bg="Red", fg="black", bd=3, cursor="dot"))
                        self.entries[i][j].place(x=60 + x2, y=70 + y2)
                        self.help_window[i].append(GlowEntry(self.window, font="arial 7", justify="center", width=10,
                                                             bg="Ivory", fg="black", bd=3, cursor="arrow"))
                        #self.help_window[i][j].place(x=55 + x2, y=100 + y2)
                        # func = f"Key_Press{i}{j}"
                        # func_name = "Key_Press{}{}".format(i,j)
                        # func_to_run = globals()[func_name]
                        self.entries[i][j].bind("<KeyPress>", func_to_run)
                    else:
                        CellText = StringVar()
                        CellText.set(self.matrix[i][j])
                        self.text_var[i].append(CellText)
                        if (self.matrix[i][j] == ''):
                            self.entries[i].append(
                                GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 25",
                                          justify="center", width=4, bg="Pink", fg="black", bd=3, cursor="dot"))
                            self.entries[i][j].place(x=60 + x2, y=70 + y2)
                            self.help_window[i].append(
                                GlowEntry(self.window, font="arial 7", justify="center", width=10,
                                          bg="Ivory", fg="black", bd=3, cursor="arrow"))
                            self.help_window[i][j].place(x=60 + x2, y=95 + y2)
                            # func_name = "Key_Press{}{}".format(i,j)
                            # func_to_run = globals()[func_name]
                            self.entries[i][j].bind("<KeyPress>", func_to_run)
                            # entries[i][j].pack()
                        else:
                            self.entries[i].append(
                                GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 25",
                                          justify="center", width=4, bg="LightBlue", fg="black", bd=3, cursor="dot"))
                            self.entries[i][j].place(x=60 + x2, y=70 + y2)
                            self.help_window[i].append(
                                GlowEntry(self.window, font="arial 7", justify="center", width=10,
                                          bg="Ivory", fg="black", bd=3, cursor="arrow"))

                    if ((self.error_matrix[i][j] != 0)):
                        CellText = StringVar()
                        CellText.set(str(self.error_matrix[i][j]))
                        self.text_var[i][j] = CellText
                        self.entries[i][j] = (
                            GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 25", justify="center",
                                      width=4, bg="Red", fg="black", bd=3, cursor="dot"))
                        self.entries[i][j].place(x=60 + x2, y=70 + y2)
                        self.help_window[i][j] = (GlowEntry(self.window, font="arial 7", justify="center", width=4, bg="Ivory", fg="black", bd=3, cursor="arrow"))
                        # func = f"Key_Press{i}{j}"
                        # func_name = "Key_Press{}{}".format(i,j)
                        # func_to_run = globals()[func_name]
                        self.entries[i][j].bind("<KeyPress>", func_to_run)
                        self.help_window[i][j].place(x=60 + x2, y=95 + y2)
                    #GlowEntry(self.window, font="arial 8", justify="center", width=4,bg="Ivory", fg="black", bd=3, cursor="arrow").place(x=50+x2, y=95 + y2)
                    x2 += 80
                y2 += 50
                x2 = 0
                button = GlowButton(self.window, text="Solve", font="arial 15 bold", justify="center", bg="Ivory", fg="DarkRed", width=11, command=self.show_sol)
                button.place(x=380, y=25)
                button = GlowButton(self.window, text="New Game", font="arial 15 bold", justify="center", bg="Ivory", fg="MediumSeaGreen", width=11, command=self.new_game)
                button.place(x=230, y=25)



        def user_wrong_sol_what(self,r, c, val):
            self.text_var = []
            self.entries = []
            x2 = 0
            y2 = 0
            rows, cols = (9, 9)
            for i in range(self.rows):
                # append an empty list to your two arrays
                # so you can append to those later
                self.text_var.append([])
                self.entries.append([])
                if i % 3 == 0:
                    y2 += 8
                for j in range(self.cols):
                    # append your StringVar and Entry
                    if j % 3 == 0:
                        x2 += 15
                    func_name = "Key_Press{}{}".format(i, j)
                    func_to_run = globals()[func_name]
                    if (i == r and j == c):
                        CellText = StringVar()
                        CellText.set(val)
                        self.text_var[i].append(CellText)
                        self.entries[i].append(
                            GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 15 bold", justify="center", width=3,
                                  bg="red", fg="white", bd=3, cursor="dot"))
                        self.entries[i][j].place(x=60 + x2, y=50 + y2)
                        # func = f"Key_Press{i}{j}"
                        # func_name = "Key_Press{}{}".format(i,j)
                        # func_to_run = globals()[func_name]
                        self.entries[i][j].bind("<KeyPress>", func_to_run)
                    else:
                        CellText = StringVar()
                        CellText.set(self.matrix[i][j])
                        self.text_var[i].append(CellText)
                        if (self.matrix[i][j] == ''):
                            self.entries[i].append(
                                GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 15 bold", justify="center",
                                      width=3, bg="LightCyan", fg="black", bd=3, cursor="dot"))
                            # entries[i].append(Entry(window,width=3,bg="LightCyan",bd=3,cursor="dot"))
                            self.entries[i][j].place(x=60 + x2, y=50 + y2)
                            # func_name = "Key_Press{}{}".format(i,j)
                            # func_to_run = globals()[func_name]
                            self.entries[i][j].bind("<KeyPress>", func_to_run)
                            # entries[i][j].pack()
                        else:
                            self.entries[i].append(
                                GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 15 bold", justify="center",
                                      width=3, bg="LightBlue", fg="black", bd=3, cursor="dot"))
                            self.entries[i][j].place(x=60 + x2, y=50 + y2)
                            self.help_window[i].append(
                                GlowEntry(self.window, font="arial 7 bold", justify="center", width=7,
                                          bg="Ivory", fg="black", bd=3, cursor="arrow"))
                    if ((self.error_matrix[i][j] != 0)):
                        CellText = StringVar()
                        CellText.set(str(self.error_matrix[i][j]))
                        self.text_var[i][j] = CellText
                        self.entries[i][j] = (
                            GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 15 bold", justify="center", width=3,
                                  bg="red", fg="white", bd=3, cursor="dot"))
                        self.entries[i][j].place(x=60 + x2, y=50 + y2)
                        # func = f"Key_Press{i}{j}"
                        # func_name = "Key_Press{}{}".format(i,j)
                        # func_to_run = globals()[func_name]
                        self.entries[i][j].bind("<KeyPress>", func_to_run)

                    x2 += 35
                y2 += 35
                x2 = 0
                button = GlowButton(self.window, text="Solve", bg="LightCyan", width=15, command=self.show_sol)
                button.place(x=100, y=400)

        def hide_sol(self,first=None):
            global func_name
            if(first!=None):
                self.new_game(first_temp = first)
            self.text_var = []
            self.entries = []
            self.help_window =[]
            x2 = 0
            y2 = 0
            self.rows, self.cols = (9, 9)
            for i in range(self.rows):
                # append an empty list to your two arrays
                # so you can append to those later
                self.text_var.append([])
                self.entries.append([])
                self.help_window.append([])
                if i % 3 == 0:
                    y2 += 10
                for j in range(self.cols):
                    # append your StringVar and Entry
                    if j % 3 == 0:
                        x2 += 15
                    CellText = StringVar()
                    CellText.set(self.matrix[i][j])
                    self.text_var[i].append(CellText)
                    func_name = "Key_Press{}{}".format(i, j)
                    func_to_run = globals()[func_name]
                    if (self.matrix[i][j] == ''):
                        self.entries[i].append(
                            GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 25 ", justify="center", width=4,
                                  bg="Pink", fg="black", bd=3, cursor="dot"))
                        # entries[i].append(Entry(window,width=3,bg="LightCyan",bd=3,cursor="dot"))
                        self.entries[i][j].place(x=60 + x2, y=70 + y2)
                        self.help_window[i].append(GlowEntry(self.window, font="arial 7", justify="center", width=10,bg="Ivory", fg="black", bd=3, cursor="arrow"))
                        self.help_window[i][j].place(x=60+x2, y=95 + y2)
                        # func_name = "Key_Press{}{}".format(i,j)
                        # func_to_run = globals()[func_name]
                        self.entries[i][j].bind("<KeyPress>", func_to_run)
                        # entries[i][j].bind("<KeyPress>", func_list.get('Key_Press{}{}'.format(i,j)) )
                        # entries[i][j].pack()
                    else:
                        self.entries[i].append(
                            GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 25", justify="center", width=4,
                                  bg="LightBlue", fg="black", bd=3, cursor="dot"))
                        self.entries[i][j].place(x=60 + x2, y=70 + y2)
                        self.help_window[i].append(GlowEntry(self.window, font="arial 7 bold", justify="center", width=7,
                              bg="Ivory", fg="black", bd=3, cursor="arrow"))
                        # func_name = "Key_Press{}{}".format(i,j)
                        # func_to_run = globals()[func_name]
                        self.entries[i][j].bind("<KeyPress>", func_to_run)
                    if (self.error_matrix[i][j] != 0):
                        CellText = StringVar()
                        CellText.set(str(self.error_matrix[i][j]))
                        self.text_var[i][j] = CellText
                        self.entries[i][j] = GlowEntry(self.window, textvariable=self.text_var[i][j], font="arial 25", justify="center",
                                                   width=4, bg="red", fg="white", bd=3, cursor="dot")
                        self.entries[i][j].place(x=60 + x2, y=70 + y2)
                        # func = f"Key_Press{i}{j}"
                        # func_name = "Key_Press{}{}".format(i,j)
                        # func_to_run = globals()[func_name]
                        self.entries[i][j].bind("<KeyPress>", func_to_run)
                    #GlowEntry(self.window, font="arial 7 bold", justify="center", width=7,bg="Ivory", fg="black", bd=3, cursor="arrow").place(x=50+x2, y=100 + y2)
                    x2 += 80
                y2 += 50
                x2 = 0
                button = GlowButton(self.window, text="Solve", font="arial 15 bold", justify="center", bg="Ivory", fg="DarkRed", width=11, command=self.show_sol)
                button.place(x=380, y=25)
                button = GlowButton(self.window, text="New Game", font="arial 15 bold", justify="center", bg="Ivory", fg="MediumSeaGreen", width=11, command=self.new_game)
                button.place(x=230, y=25)
                me = self

def Key_Press00(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(0,0)):
        me.setErrorMatrix_With_Zero(0,0)
        me.setOriginalMatrix_With_SolMatrixVal(0,0)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(0,0,(str)(event.keycode - 48))
        me.user_wrong_sol(0,0,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press01(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(0,1)):
        me.setErrorMatrix_With_Zero(0,1)
        me.setOriginalMatrix_With_SolMatrixVal(0,1)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(0,1,(str)(event.keycode - 48))
        me.user_wrong_sol(0,1,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press02(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(0,2)):
        me.setErrorMatrix_With_Zero(0,2)
        me.setOriginalMatrix_With_SolMatrixVal(0,2)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(0,2,(str)(event.keycode - 48))
        me.user_wrong_sol(0,2,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press03(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(0,3)):
        me.setErrorMatrix_With_Zero(0,3)
        me.setOriginalMatrix_With_SolMatrixVal(0,3)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(0,3,(str)(event.keycode - 48))
        me.user_wrong_sol(0,3,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press04(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(0,4)):
        me.setErrorMatrix_With_Zero(0,4)
        me.setOriginalMatrix_With_SolMatrixVal(0,4)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(0,4,(str)(event.keycode - 48))
        me.user_wrong_sol(0,4,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press05(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(0,5)):
        me.setErrorMatrix_With_Zero(0,5)
        me.setOriginalMatrix_With_SolMatrixVal(0,5)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(0,5,(str)(event.keycode - 48))
        me.user_wrong_sol(0,5,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press06(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(0,6)):
        me.setErrorMatrix_With_Zero(0,6)
        me.setOriginalMatrix_With_SolMatrixVal(0,6)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(0,6,(str)(event.keycode - 48))
        me.user_wrong_sol(0,6,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press07(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(0,7)):
        me.setErrorMatrix_With_Zero(0,7)
        me.setOriginalMatrix_With_SolMatrixVal(0,7)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(0,7,(str)(event.keycode - 48))
        me.user_wrong_sol(0,7,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press08(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(0,8)):
        me.setErrorMatrix_With_Zero(0,8)
        me.setOriginalMatrix_With_SolMatrixVal(0,8)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(0,8,(str)(event.keycode - 48))
        me.user_wrong_sol(0,8,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press10(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(1,0)):
        me.setErrorMatrix_With_Zero(1,0)
        me.setOriginalMatrix_With_SolMatrixVal(1,0)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(1,0,(str)(event.keycode - 48))
        me.user_wrong_sol(1,0,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press11(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(1,1)):
        me.setErrorMatrix_With_Zero(1,1)
        me.setOriginalMatrix_With_SolMatrixVal(1,1)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(1,1,(str)(event.keycode - 48))
        me.user_wrong_sol(1,1,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press12(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(1,2)):
        me.setErrorMatrix_With_Zero(1,2)
        me.setOriginalMatrix_With_SolMatrixVal(1,2)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(1,2,(str)(event.keycode - 48))
        me.user_wrong_sol(1,2,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press13(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(1,3)):
        me.setErrorMatrix_With_Zero(1,3)
        me.setOriginalMatrix_With_SolMatrixVal(1,3)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(1,3,(str)(event.keycode - 48))
        me.user_wrong_sol(1,3,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press14(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(1,4)):
        me.setErrorMatrix_With_Zero(1,4)
        me.setOriginalMatrix_With_SolMatrixVal(1,4)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(1,4,(str)(event.keycode - 48))
        me.user_wrong_sol(1,4,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press15(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(1,5)):
        me.setErrorMatrix_With_Zero(1,5)
        me.setOriginalMatrix_With_SolMatrixVal(1,5)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(1,5,(str)(event.keycode - 48))
        me.user_wrong_sol(1,5,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press16(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(1,6)):
        me.setErrorMatrix_With_Zero(1,6)
        me.setOriginalMatrix_With_SolMatrixVal(1,6)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(1,6,(str)(event.keycode - 48))
        me.user_wrong_sol(1,6,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press17(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(1,7)):
        me.setErrorMatrix_With_Zero(1,7)
        me.setOriginalMatrix_With_SolMatrixVal(1,7)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(1,7,(str)(event.keycode - 48))
        me.user_wrong_sol(1,7,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press18(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(1,8)):
        me.setErrorMatrix_With_Zero(1,8)
        me.setOriginalMatrix_With_SolMatrixVal(1,8)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(1,8,(str)(event.keycode - 48))
        me.user_wrong_sol(1,8,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press20(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(2,0)):
        me.setErrorMatrix_With_Zero(2,0)
        me.setOriginalMatrix_With_SolMatrixVal(2,0)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(2,0,(str)(event.keycode - 48))
        me.user_wrong_sol(2,0,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press21(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(2,1)):
        me.setErrorMatrix_With_Zero(2,1)
        me.setOriginalMatrix_With_SolMatrixVal(2,1)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(2,1,(str)(event.keycode - 48))
        me.user_wrong_sol(2,1,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press22(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(2,2)):
        me.setErrorMatrix_With_Zero(2,2)
        me.setOriginalMatrix_With_SolMatrixVal(2,2)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(2,2,(str)(event.keycode - 48))
        me.user_wrong_sol(2,2,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press23(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(2,3)):
        me.setErrorMatrix_With_Zero(2,3)
        me.setOriginalMatrix_With_SolMatrixVal(2,3)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(2,3,(str)(event.keycode - 48))
        me.user_wrong_sol(2,3,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press24(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(2,4)):
        me.setErrorMatrix_With_Zero(2,4)
        me.setOriginalMatrix_With_SolMatrixVal(2,4)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(2,4,(str)(event.keycode - 48))
        me.user_wrong_sol(2,4,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press25(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(2,5)):
        me.setErrorMatrix_With_Zero(2,5)
        me.setOriginalMatrix_With_SolMatrixVal(2,5)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(2,5,(str)(event.keycode - 48))
        me.user_wrong_sol(2,5,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press26(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(2,6)):
        me.setErrorMatrix_With_Zero(2,6)
        me.setOriginalMatrix_With_SolMatrixVal(2,6)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(2,6,(str)(event.keycode - 48))
        me.user_wrong_sol(2,6,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press27(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(2,7)):
        me.setErrorMatrix_With_Zero(2,7)
        me.setOriginalMatrix_With_SolMatrixVal(2,7)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(2,7,(str)(event.keycode - 48))
        me.user_wrong_sol(2,7,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press28(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(2,8)):
        me.setErrorMatrix_With_Zero(2,8)
        me.setOriginalMatrix_With_SolMatrixVal(2,8)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(2,8,(str)(event.keycode - 48))
        me.user_wrong_sol(2,8,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press30(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(3,0)):
        me.setErrorMatrix_With_Zero(3,0)
        me.setOriginalMatrix_With_SolMatrixVal(3,0)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(3,0,(str)(event.keycode - 48))
        me.user_wrong_sol(3,0,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press31(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(3,1)):
        me.setErrorMatrix_With_Zero(3,1)
        me.setOriginalMatrix_With_SolMatrixVal(3,1)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(3,1,(str)(event.keycode - 48))
        me.user_wrong_sol(3,1,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press32(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(3,2)):
        me.setErrorMatrix_With_Zero(3,2)
        me.setOriginalMatrix_With_SolMatrixVal(3,2)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(3,2,(str)(event.keycode - 48))
        me.user_wrong_sol(3,2,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press33(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(3,3)):
        me.setErrorMatrix_With_Zero(3,3)
        me.setOriginalMatrix_With_SolMatrixVal(3,3)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(3,3,(str)(event.keycode - 48))
        me.user_wrong_sol(3,3,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press34(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(3,4)):
        me.setErrorMatrix_With_Zero(3,4)
        me.setOriginalMatrix_With_SolMatrixVal(3,4)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(3,4,(str)(event.keycode - 48))
        me.user_wrong_sol(3,4,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press35(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(3,5)):
        me.setErrorMatrix_With_Zero(3,5)
        me.setOriginalMatrix_With_SolMatrixVal(3,5)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(3,5,(str)(event.keycode - 48))
        me.user_wrong_sol(3,5,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press36(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(3,6)):
        me.setErrorMatrix_With_Zero(3,6)
        me.setOriginalMatrix_With_SolMatrixVal(3,6)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(3,6,(str)(event.keycode - 48))
        me.user_wrong_sol(3,6,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press37(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(3,7)):
        me.setErrorMatrix_With_Zero(3,7)
        me.setOriginalMatrix_With_SolMatrixVal(3,7)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(3,7,(str)(event.keycode - 48))
        me.user_wrong_sol(3,7,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press38(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(3,8)):
        me.setErrorMatrix_With_Zero(3,8)
        me.setOriginalMatrix_With_SolMatrixVal(3,8)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(3,8,(str)(event.keycode - 48))
        me.user_wrong_sol(3,8,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press40(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(4,0)):
        me.setErrorMatrix_With_Zero(4,0)
        me.setOriginalMatrix_With_SolMatrixVal(4,0)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(4,0,(str)(event.keycode - 48))
        me.user_wrong_sol(4,0,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press41(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(4,1)):
        me.setErrorMatrix_With_Zero(4,1)
        me.setOriginalMatrix_With_SolMatrixVal(4,1)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(4,1,(str)(event.keycode - 48))
        me.user_wrong_sol(4,1,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press42(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(4,2)):
        me.setErrorMatrix_With_Zero(4,2)
        me.setOriginalMatrix_With_SolMatrixVal(4,2)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(4,2,(str)(event.keycode - 48))
        me.user_wrong_sol(4,2,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press43(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(4,3)):
        me.setErrorMatrix_With_Zero(4,3)
        me.setOriginalMatrix_With_SolMatrixVal(4,3)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(4,3,(str)(event.keycode - 48))
        me.user_wrong_sol(4,3,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press44(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(4,4)):
        me.setErrorMatrix_With_Zero(4,4)
        me.setOriginalMatrix_With_SolMatrixVal(4,4)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(4,4,(str)(event.keycode - 48))
        me.user_wrong_sol(4,4,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press45(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(4,5)):
        me.setErrorMatrix_With_Zero(4,5)
        me.setOriginalMatrix_With_SolMatrixVal(4,5)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(4,5,(str)(event.keycode - 48))
        me.user_wrong_sol(4,5,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press46(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(4,6)):
        me.setErrorMatrix_With_Zero(4,6)
        me.setOriginalMatrix_With_SolMatrixVal(4,6)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(4,6,(str)(event.keycode - 48))
        me.user_wrong_sol(4,6,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press47(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(4,7)):
        me.setErrorMatrix_With_Zero(4,7)
        me.setOriginalMatrix_With_SolMatrixVal(4,7)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(4,7,(str)(event.keycode - 48))
        me.user_wrong_sol(4,7,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press48(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(4,8)):
        me.setErrorMatrix_With_Zero(4,8)
        me.setOriginalMatrix_With_SolMatrixVal(4,8)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(4,8,(str)(event.keycode - 48))
        me.user_wrong_sol(4,8,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press50(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(5,0)):
        me.setErrorMatrix_With_Zero(5,0)
        me.setOriginalMatrix_With_SolMatrixVal(5,0)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(5,0,(str)(event.keycode - 48))
        me.user_wrong_sol(5,0,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press51(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(5,1)):
        me.setErrorMatrix_With_Zero(5,1)
        me.setOriginalMatrix_With_SolMatrixVal(5,1)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(5,1,(str)(event.keycode - 48))
        me.user_wrong_sol(5,1,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press52(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(5,2)):
        me.setErrorMatrix_With_Zero(5,2)
        me.setOriginalMatrix_With_SolMatrixVal(5,2)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(5,2,(str)(event.keycode - 48))
        me.user_wrong_sol(5,2,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press53(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(5,3)):
        me.setErrorMatrix_With_Zero(5,3)
        me.setOriginalMatrix_With_SolMatrixVal(5,3)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(5,3,(str)(event.keycode - 48))
        me.user_wrong_sol(5,3,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press54(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(5,4)):
        me.setErrorMatrix_With_Zero(5,4)
        me.setOriginalMatrix_With_SolMatrixVal(5,4)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(5,4,(str)(event.keycode - 48))
        me.user_wrong_sol(5,4,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press55(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(5,5)):
        me.setErrorMatrix_With_Zero(5,5)
        me.setOriginalMatrix_With_SolMatrixVal(5,5)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(5,5,(str)(event.keycode - 48))
        me.user_wrong_sol(5,5,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press56(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(5,6)):
        me.setErrorMatrix_With_Zero(5,6)
        me.setOriginalMatrix_With_SolMatrixVal(5,6)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(5,6,(str)(event.keycode - 48))
        me.user_wrong_sol(5,6,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press57(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(5,7)):
        me.setErrorMatrix_With_Zero(5,7)
        me.setOriginalMatrix_With_SolMatrixVal(5,7)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(5,7,(str)(event.keycode - 48))
        me.user_wrong_sol(5,7,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press58(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(5,8)):
        me.setErrorMatrix_With_Zero(5,8)
        me.setOriginalMatrix_With_SolMatrixVal(5,8)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(5,8,(str)(event.keycode - 48))
        me.user_wrong_sol(5,8,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press60(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(6,0)):
        me.setErrorMatrix_With_Zero(6,0)
        me.setOriginalMatrix_With_SolMatrixVal(6,0)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(6,0,(str)(event.keycode - 48))
        me.user_wrong_sol(6,0,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press61(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(6,1)):
        me.setErrorMatrix_With_Zero(6,1)
        me.setOriginalMatrix_With_SolMatrixVal(6,1)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(6,1,(str)(event.keycode - 48))
        me.user_wrong_sol(6,1,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press62(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(6,2)):
        me.setErrorMatrix_With_Zero(6,2)
        me.setOriginalMatrix_With_SolMatrixVal(6,2)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(6,2,(str)(event.keycode - 48))
        me.user_wrong_sol(6,2,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press63(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(6,3)):
        me.setErrorMatrix_With_Zero(6,3)
        me.setOriginalMatrix_With_SolMatrixVal(6,3)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(6,3,(str)(event.keycode - 48))
        me.user_wrong_sol(6,3,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press64(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(6,4)):
        me.setErrorMatrix_With_Zero(6,4)
        me.setOriginalMatrix_With_SolMatrixVal(6,4)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(6,4,(str)(event.keycode - 48))
        me.user_wrong_sol(6,4,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press65(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(6,5)):
        me.setErrorMatrix_With_Zero(6,5)
        me.setOriginalMatrix_With_SolMatrixVal(6,5)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(6,5,(str)(event.keycode - 48))
        me.user_wrong_sol(6,5,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press66(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(6,6)):
        me.setErrorMatrix_With_Zero(6,6)
        me.setOriginalMatrix_With_SolMatrixVal(6,6)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(6,6,(str)(event.keycode - 48))
        me.user_wrong_sol(6,6,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press67(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(6,7)):
        me.setErrorMatrix_With_Zero(6,7)
        me.setOriginalMatrix_With_SolMatrixVal(6,7)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(6,7,(str)(event.keycode - 48))
        me.user_wrong_sol(6,7,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press68(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(6,8)):
        me.setErrorMatrix_With_Zero(6,8)
        me.setOriginalMatrix_With_SolMatrixVal(6,8)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(6,8,(str)(event.keycode - 48))
        me.user_wrong_sol(6,8,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press70(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(7,0)):
        me.setErrorMatrix_With_Zero(7,0)
        me.setOriginalMatrix_With_SolMatrixVal(7,0)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(7,0,(str)(event.keycode - 48))
        me.user_wrong_sol(7,0,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press71(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(7,1)):
        me.setErrorMatrix_With_Zero(7,1)
        me.setOriginalMatrix_With_SolMatrixVal(7,1)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(7,1,(str)(event.keycode - 48))
        me.user_wrong_sol(7,1,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press72(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(7,2)):
        me.setErrorMatrix_With_Zero(7,2)
        me.setOriginalMatrix_With_SolMatrixVal(7,2)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(7,2,(str)(event.keycode - 48))
        me.user_wrong_sol(7,2,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press73(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(7,3)):
        me.setErrorMatrix_With_Zero(7,3)
        me.setOriginalMatrix_With_SolMatrixVal(7,3)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(7,3,(str)(event.keycode - 48))
        me.user_wrong_sol(7,3,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press74(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(7,4)):
        me.setErrorMatrix_With_Zero(7,4)
        me.setOriginalMatrix_With_SolMatrixVal(7,4)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(7,4,(str)(event.keycode - 48))
        me.user_wrong_sol(7,4,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press75(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(7,5)):
        me.setErrorMatrix_With_Zero(7,5)
        me.setOriginalMatrix_With_SolMatrixVal(7,5)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(7,5,(str)(event.keycode - 48))
        me.user_wrong_sol(7,5,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press76(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(7,6)):
        me.setErrorMatrix_With_Zero(7,6)
        me.setOriginalMatrix_With_SolMatrixVal(7,6)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(7,6,(str)(event.keycode - 48))
        me.user_wrong_sol(7,6,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press77(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(7,7)):
        me.setErrorMatrix_With_Zero(7,7)
        me.setOriginalMatrix_With_SolMatrixVal(7,7)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(7,7,(str)(event.keycode - 48))
        me.user_wrong_sol(7,7,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press78(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(7,8)):
        me.setErrorMatrix_With_Zero(7,8)
        me.setOriginalMatrix_With_SolMatrixVal(7,8)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(7,8,(str)(event.keycode - 48))
        me.user_wrong_sol(7,8,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press80(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(8,0)):
        me.setErrorMatrix_With_Zero(8,0)
        me.setOriginalMatrix_With_SolMatrixVal(8,0)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(8,0,(str)(event.keycode - 48))
        me.user_wrong_sol(8,0,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press81(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(8,1)):
        me.setErrorMatrix_With_Zero(8,1)
        me.setOriginalMatrix_With_SolMatrixVal(8,1)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(8,1,(str)(event.keycode - 48))
        me.user_wrong_sol(8,1,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press82(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(8,2)):
        me.setErrorMatrix_With_Zero(8,2)
        me.setOriginalMatrix_With_SolMatrixVal(8,2)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(8,2,(str)(event.keycode - 48))
        me.user_wrong_sol(8,2,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press83(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(8,3)):
        me.setErrorMatrix_With_Zero(8,3)
        me.setOriginalMatrix_With_SolMatrixVal(8,3)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(8,3,(str)(event.keycode - 48))
        me.user_wrong_sol(8,3,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press84(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(8,4)):
        me.setErrorMatrix_With_Zero(8,4)
        me.setOriginalMatrix_With_SolMatrixVal(8,4)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(8,4,(str)(event.keycode - 48))
        me.user_wrong_sol(8,4,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press85(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(8,5)):
        me.setErrorMatrix_With_Zero(8,5)
        me.setOriginalMatrix_With_SolMatrixVal(8,5)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(8,5,(str)(event.keycode - 48))
        me.user_wrong_sol(8,5,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press86(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(8,6)):
        me.setErrorMatrix_With_Zero(8,6)
        me.setOriginalMatrix_With_SolMatrixVal(8,6)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(8,6,(str)(event.keycode - 48))
        me.user_wrong_sol(8,6,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press87(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(8,7)):
        me.setErrorMatrix_With_Zero(8,7)
        me.setOriginalMatrix_With_SolMatrixVal(8,7)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(8,7,(str)(event.keycode - 48))
        me.user_wrong_sol(8,7,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
def Key_Press88(event):
    if((event.keycode!= 8) and (event.keycode - 48)<1 or (event.keycode - 48)>9):
        messagebox.showinfo("Error", "Only numbers between 1 and 9!\nIf you do not know the rules of the game please click Help")
        me.hide_sol()
    elif((str)(event.keycode - 48) == me.getSolMatrixAtIndex(8,8)):
        me.setErrorMatrix_With_Zero(8,8)
        me.setOriginalMatrix_With_SolMatrixVal(8,8)
        me.hide_sol()
    elif (event.keycode!= 8):
        me.setErrorMatrix_With_Val(8,8,(str)(event.keycode - 48))
        me.user_wrong_sol(8,8,(str)(event.keycode - 48))
    if(me.matrix==me.sol_matrix):
        me.user_good_sol()
