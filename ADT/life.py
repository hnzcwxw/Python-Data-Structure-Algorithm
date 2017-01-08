# Implements the LifeGrid ADT for use with the game of life
from arrayy import Array2D

class LifeGrid:
    # Defines contents to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Create the game grid and initializes the cell to dead
    def __init__(self, numRows, numCols):
        # Allocate the the 2-D array for the grid
        self._grid = Array2D(numRows, numCols)
        # Clear the grid and set all cell to dead
        self.configure(list())

    # Return the number of the rows in the grid
    def numRows(self):
        return self._grid.numRows()

    # Return the number of the cols in the grid
    def numCols(self):
        return self._grid.numCols()

    # Configures the grid to contain the given live cells
    def configure(self, coordList):
        # Clear the game grid
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

        # Set the indicated cell to be alive
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    # Does the indicated cell contain a live organism
    def isLiveCell(self, row, col):
        return self._grid[row, col] == LifeGrid.LIVE_CELL

    # Clear the indicated cell by setting it to dead
    def clearCell(self, row, col):
        self._grid[row, col] = LifeGrid.DEAD_CELL

    # Set the indicated cell to be a live
    def setCell(self, row, col):
        self._grid[row, col] = LifeGrid.LIVE_CELL

    # Return the number of live neighbors for the given cell
    def numLiveNeighbors(self, row, col):
        numLife = 0

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if ((i >= 0 and i < self.numCols()) and (j >= 0 and j < self.numCols())):
                    if self.isLiveCell(i, j):
                        numLife += 1
        if self.isLiveCell(row, col):
            numLife -= 1
        return numLife

    # Does the grid is a alive
    def isLive(self):
        numLife = 0
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                if self.numLiveNeighbors(i, j):
                    numLife += 1
        if numLife > 0:
            return True
        else:
            return False

    # Draw the screen of the game grid
    def draw(self):
        for r in range(self.numRows()):
            strList = ''
            for c in range(self.numCols()):
                if self.isLiveCell(r, c):
                    strList += '@' + ' '
                else:
                    strList += '.' + ' '
            print strList



