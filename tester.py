import Cell
import SubGrid
import Grid

sg1 = SubGrid.SubGrid(0, [Cell.Cell(1, 0, 1), Cell.Cell(1, 2, 5), Cell.Cell(2, 2, 2)])
sg2 = SubGrid.SubGrid(1, [Cell.Cell(0, 1, 6), Cell.Cell(0, 2, 5), Cell.Cell(1, 1, 2), Cell.Cell(2, 0, 8)])
sg3 = SubGrid.SubGrid(2, [Cell.Cell(0, 0, 9), Cell.Cell(0, 1, 2), Cell.Cell(0, 2, 8), Cell.Cell(1, 0, 7), Cell.Cell(1, 1, 6)])
sg4 = SubGrid.SubGrid(3, [Cell.Cell(0, 0, 5), Cell.Cell(0, 1, 3), Cell.Cell(1, 0, 6), Cell.Cell(1, 1, 4), Cell.Cell(2, 2, 7)])
sg5 = SubGrid.SubGrid(4, [Cell.Cell(0, 0, 4), Cell.Cell(0, 1, 8), Cell.Cell(0, 2, 9), Cell.Cell(1, 0, 7), Cell.Cell(2, 1, 1)])
sg6 = SubGrid.SubGrid(5, [Cell.Cell(1, 0, 8), Cell.Cell(1, 1, 3), Cell.Cell(2, 1, 4), Cell.Cell(2, 2, 9)])
sg7 = SubGrid.SubGrid(6, [Cell.Cell(0, 0, 4), Cell.Cell(0, 1, 9), Cell.Cell(1, 1, 1), Cell.Cell(1, 2, 8)])
sg8 = SubGrid.SubGrid(7, [Cell.Cell(0, 2, 8), Cell.Cell(2, 1, 9), Cell.Cell(2, 2, 1)])
sg9 = SubGrid.SubGrid(8, [Cell.Cell(0, 0, 1), Cell.Cell(0, 1, 5), Cell.Cell(0, 2, 7), Cell.Cell(1, 0, 3), Cell.Cell(2, 0, 2)])

g = Grid.Grid([sg1, sg2, sg3, sg4, sg5, sg6, sg7, sg8, sg9])
print(g)
g.getGrid()
g.solve()

print(g)

sg01 = SubGrid.SubGrid(0, [Cell.Cell(0, 0, 9), Cell.Cell(1, 0, 6), Cell.Cell(1, 1, 8),Cell.Cell(1, 2, 7),Cell.Cell(2, 2, 4)])
sg02 = SubGrid.SubGrid(1, [Cell.Cell(0, 0, 5), Cell.Cell(1, 0, 3), Cell.Cell(1, 1, 4), Cell.Cell(2, 0, 1),Cell.Cell(2, 2, 7)])
sg03 = SubGrid.SubGrid(2, [Cell.Cell(1, 1, 5), Cell.Cell(2, 1, 3)])
sg04 = SubGrid.SubGrid(3, [Cell.Cell(0, 1, 4), Cell.Cell(1, 1, 2), Cell.Cell(1, 2, 6), Cell.Cell(2, 1, 9), Cell.Cell(2, 2, 1)])
sg05 = SubGrid.SubGrid(4, [Cell.Cell(0, 1, 2), Cell.Cell(0, 2, 6), Cell.Cell(1, 1, 5), Cell.Cell(1, 2, 1), Cell.Cell(2, 0, 4),Cell.Cell(2, 2, 3)])
sg06 = SubGrid.SubGrid(5, [Cell.Cell(0, 2, 8), Cell.Cell(1, 0, 4), Cell.Cell(1, 1, 9),Cell.Cell(2, 1, 6), Cell.Cell(2, 2, 2)])
sg07 = SubGrid.SubGrid(6, [Cell.Cell(0, 2, 2), Cell.Cell(2, 0, 5)])
sg08 = SubGrid.SubGrid(7, [Cell.Cell(0, 0, 7), Cell.Cell(2, 2, 9)])
sg09 = SubGrid.SubGrid(8, [Cell.Cell(0, 0, 9), Cell.Cell(0, 2, 5), Cell.Cell(1, 0, 3), Cell.Cell(1, 2, 1), Cell.Cell(2, 0, 6),Cell.Cell(2, 2, 7)])

gg = Grid.Grid([sg01, sg02, sg03, sg04, sg05, sg06, sg07, sg08, sg09])
print(gg)
gg.solve()
print(gg)

for i in range(10):
    print("omri{}".format(i))
    
func = ""
for i in range(9):
    for j in range(9):
        strr=f"def Key_Press{i}{j}(event):\n    if((str)(event.keycode - 48) == sol_matrix[{i}][{j}]):\n        matrix[{i}][{j}] = sol_matrix[{i}][{j}]\n        hide_sol()\n    elif (event.keycode!= 8):\n        user_wrong_sol({i},{j},(str)(event.keycode - 48))\n        messagebox.showinfo(\"Warning", "Mistake !\nThink again and never repeat this mistake!\")"
        print(strr)
