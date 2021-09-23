import Cell
import copy
class SubGrid:
    """
    A class used to represent a sudogu sub grids.
    attribute:
        i: the number of the sudoku sub grid
        cells: list of the cell that own to the subgrid
        collected values : list that contain the values that in this subgrid
    """
    def __init__(self,i,cells=None):
        """
        Constructor for subgrid class.
        param:
        i: the number of the sudoku sub grid
        cells: list of the cell that own to the subgrid
        collected values : list that contain the values that in this subgrid
        """
        self.i = i
        matrix = []
        for k in range(3):
            matrix.append([])#add empty sublist inside the list
            for j in range(3):
                matrix[k].append(Cell.Cell(k,j))
        self.grid = matrix
        self.collected_values = []
        if cells == None:#no known cells to update
            pass
        else:
            for c in cells:
                self.grid[c.i][c.j] = c#add known Cells
                self.collected_values.append(c.values)
    
    def update_values(self):
        '''
        function that update the collected_values
        '''
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if len(self.grid[row][col].values) == 1:#if its only possible value
                    if self.grid[row][col].values[0] not in self.collected_values:#and this value not in collected values
                        self.collected_values.append(self.grid[row][col].values[0])
                    elif self.grid[row][col].values not in self.collected_values:#and this value not in collected values
                        self.collected_values.append(self.grid[row][col].values)
    
    def remove_values(self,cell):
        '''
        function that remove impossible values from the cell.values
        '''
        if len(cell.values)== 1:
            pass
        else:
            callvalues = copy.deepcopy(cell.values)
            for val in callvalues:
                if [val] in self.collected_values:
                    cell.values.remove(val)
                elif val in self.collected_values:
                    cell.values.remove(val)
                if len(cell.values)==1:
                    break
            SubGrid.update_values(self)
                    
            '''
            for val in self.collected_values:
                if len(cell.values) == 1:
                        break
                if type(val) == list:
                    if val == []:
                        continue
                    real = val[0]
                    if real in cell.values:
                        cell.values.remove(real)
                        if len(cell.values) == 1:
                            break
                    continue
                else:
                    if val in cell.values:
                        cell.values.remove(val)
                        if len(cell.values) == 1:
                            break
                    continue
            SubGrid.update_values(self)
            '''
    
    def check_cells_possibilities(self):
        '''
        the function that responsible to update the cells values
        '''
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                self.remove_values(self.grid[r][c])
                        