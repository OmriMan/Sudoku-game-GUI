class Cell:
    """
    A class used to represent a cell in sudogu grid.
    attribute:
        i: row index in subgrid
        j: column index in subgrid
        values : a list with possible numbers to get into the cell
    """
    def __init__(self,i,j,value=None):
        """
        Constructor for cell class.
        param i:row index in subgrid
        param j:column
        param value: if none -list with possible numbers to get into the cell,not none-the number that already in this cell
        """
        self.i=i
        self.j=j
        if value == None:
            self.values = [1,2,3,4,5,6,7,8,9]
        else:
            self.values = [value]
           
    def __repr__(self):
        if len(self.values) == 1:
            return str(self.values[0])
        return '_'