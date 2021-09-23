import SubGrid
#import Cell
import copy



class Grid:
    """
    A class used to represent a sudogu grid.
    attribute:
        rows: list of the values in the grid rows
        column: list of the values in the grid columnss
        sub_grids : a list with the subgrids of the sudoku grid
    """
    
    def __init__(self,sub_grids=None):
        """
        Constructor for vector class.
        param sub_gris: a list with the subgrids of the sudoku grid
        """
        self.rows = neslist_factory(9)
        self.columns = neslist_factory(9)
        subs =[]
        #build sub_grids list with initialized sub_grid
        for i in range(9):
                subs.append(SubGrid.SubGrid(i))
        if sub_grids == None:
             self.sub_grids = subs
        else:#update the sub_grids by the input
            for sub in sub_grids:
                subs[sub.i] = sub
                self.sub_grids = subs
                    
    def update_values(self):
        '''
        function that update the rows and columns
        
        '''
        for mini in self.sub_grids:
            for r in range(3):#rows in subgrid
                for c in range(3):#columns in subgrid
                    if len(mini.grid[r][c].values) == 1:
                        #add value to column
                        if (mini.i)%3 == 0:
                            #subgrid num 0/3/6 - same column
                            if mini.grid[r][c].values[0] not in self.columns[c] and [mini.grid[r][c].values[0]] not in self.columns[c]:
                                self.columns[c].append(mini.grid[r][c].values)
                        elif (mini.i)%3 == 1:#subgrid options 1/4/7
                            if mini.grid[r][c].values[0] not in self.columns[c+3] and [mini.grid[r][c].values[0]] not in self.columns[c+3]:
                                self.columns[c+3].append(mini.grid[r][c].values)
                        else:#subgrid 2/5/8
                            if mini.grid[r][c].values[0] not in self.columns[c+6] and [mini.grid[r][c].values[0]] not in self.columns[c+6] :
                                self.columns[c+6].append(mini.grid[r][c].values)
                        #add value to rows
                        if (mini.i)>=0 and (mini.i)<=2:
                            #subgrid 0/1/2 - same rows
                            if mini.grid[r][c].values[0] not in self.rows[r] and [mini.grid[r][c].values[0]] not in self.rows[r]:
                                self.rows[r].append(mini.grid[r][c].values)
                        elif (mini.i)>=3 and (mini.i)<=5:
                            #subgrid 3/4/5
                            if mini.grid[r][c].values[0] not in self.rows[r+3] and [mini.grid[r][c].values[0]] not in self.rows[r+3]:
                                self.rows[r+3].append(mini.grid[r][c].values)
                        else:#subgrid 6/7/8
                            if mini.grid[r][c].values[0] not in self.rows[r+6] and [mini.grid[r][c].values[0]] not in self.rows[r+6] :
                                self.rows[r+6].append(mini.grid[r][c].values)
                            
                            
    def remove_values(self,cell,grid_num):
        '''
        function that remove redundant or impossible values
        remove and then upadate
        '''
        if len(cell.values) == 1:
            return#no values to remove
        #check column
        cellvalues = copy.deepcopy(cell.values)#prevent skipping
        if grid_num%3 == 0 :#subgrid 0/3/6
            for val in cellvalues:
                if [val] in self.columns[cell.j]:
                    cell.values.remove(val)
        elif grid_num%3 ==1:#subgrid 1/4/7
            for val in cellvalues:
                if [val] in self.columns[(cell.j)+3]:
                    cell.values.remove(val)
        else:#subgrif 2/5/8
            for val in cellvalues:
                if [val] in self.columns[(cell.j)+6]:
                    cell.values.remove(val)
        #check row
        cellvalues = copy.deepcopy(cell.values)#cell.values has been change so need to #prevent skipping again
        if grid_num>=0 and grid_num<=2:#subgrid 0/1/2
            for val in cellvalues:
                if [val] in self.rows[cell.i]:
                    cell.values.remove(val)
        elif grid_num>=3 and grid_num<=5:#subgrid 3/4/5
            for val in cellvalues:
                if [val] in self.rows[(cell.i)+3]:
                    cell.values.remove(val)
        else:#subgrid 6/7/8
            for val in cellvalues:
                if [val] in self.rows[(cell.i)+6]:
                    cell.values.remove(val)
        self.update_values()

        
        
    def check_possibilities(self):
        '''
        check,remove and update the cell.values
        '''
        for square in self.sub_grids:
            square.check_cells_possibilities()
        self.update_values()
        for sub in self.sub_grids:
            for r in range(3):#רץ על השורה בריבוע הקטן
                for c in range(3):#
                    self.remove_values(sub.grid[r][c] , sub.i)
        
                    
    
    def is_solved(self):
        '''
        return True if the sudoku gris is full-game over
        return False if the sudoku grid isnt full-game continue
        '''
        solved = True
        for sq in self.sub_grids:
            for r in range(3):
                for c in range(3):
                    if len(sq.grid[r][c].values) != 1:
                        solved = False
                        return solved
                    else:
                        continue
        return solved

    def solve(self):
        '''
        start the solution process
        '''
        solve_or_not = Grid.is_solved(self)
        while solve_or_not == False: 
            Grid.check_possibilities(self)
            solve_or_not = Grid.is_solved(self)
                        

    def __repr__(self):
        res = ''
        for i in range(9):
            if i % 3 == 0:
                res = res + '\n\n'
            for j in range(9):
                if j % 3 == 0:
                    res = res + '    '
                res = res + str(self.sub_grids[3 * int(i / 3)+ int(j / 3)].grid[i % 3][j % 3]) + ' '
            res = res + '\n'
        return res
    
    def getGrid(self):
        matrix = []
        for i in range(9):
            matrix.append([])
            for j in range(9):
                if(str(self.sub_grids[3 * int(i / 3)+ int(j / 3)].grid[i % 3][j % 3])=='_'):
                    matrix[i].append('')
                    continue
                matrix[i].append(str(self.sub_grids[3 * int(i / 3)+ int(j / 3)].grid[i % 3][j % 3]))
        return matrix

def neslist_factory(size):#auxiliary function for Grid init
    '''
    function that build a nested list
    return list taht all element in this list is empty list
    '''
    listx = []
    listx = [ [] for emp in range(size)]
    return listx

