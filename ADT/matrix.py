# Implementation of the Matrix ATD using 2-D array
from arrayy import Array2D

class Matrix:
    # Create a matrix of size numRows x numCols initialized to 0
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    # Return the number of the rows in the matrix
    def numRows(self):
        return self._theGrid.numRows()

    # Return the number of the columns in the matrix
    def numCols(self):
        return self._theGrid.numCols()

    # Return the value of element (i, j): x[i, j]
    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    # Sets the value of element (i, j) to the value s : x[i, j] = s
    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    # Scales the matrix by given scalar
    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scalar

    # Create and returns a new matrix that is the transpose of this matrix
    def transpose(self):
        # Create a new matrix
        newMatrix = Matrix(self.numCols(), self.numRows())
        # transpose the matrix
        for r in range(self.numCols()):
            for c in range(self.numRows()):
                newMatrix[r, c] = self[c, r]
        return newMatrix

    # Create and return a new matrix that result from matrix addition
    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and     \
               rhsMatrix.numCols() == self.numCols(),        \
            "Matrix sizes not compatible in the two matrices"
        # Create a new matrix
        newMatrix = Matrix(self.numRows(), self.numCols())
        # add the corresponding elements in the two matrix
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]
        return newMatrix

    # Create and returns a new matrix that result from matrix subtraction
    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and     \
               rhsMatrix.numCols() == self.numCols(),        \
            "Matrix sizes not compatible in the two matrices"
        # Create a new matrix
        newMatrix = Matrix(self.numRows(), self.numCols())
        # add the corresponding elements in the two matrix
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]
        return newMatrix

    # Create and returns a new matrix that result from matrix multiplication
    def __mul__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numCols(), "Matrix sizes not compatible in the two matrices"
        # Create a new matrix
        newMatrix = Matrix(self.numRows(), rhsMatrix.numCols())
        # multiplication the corresponding elements in the two matrix
        for r in range(self.numRows()):
            for c in range(rhsMatrix.numCols()):
                for j in range(self.numCols()):
                    newMatrix[r, c] += self[r, j] * rhsMatrix[j, c]

        return newMatrix

    def maPrint(self):
        return self._theGrid.arPrint()