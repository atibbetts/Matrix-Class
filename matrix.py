import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        #The determinant of a  1×1  matrix is just the value of the matrice's only element.
        if self.h == 1:
            matrixDet1 = self.g[0]
            return matrixDet1
        
        #The determinant of a  2×2  matrix is given by ad - bc where [[a b], [c d]]
        if self.h == 2:
            matrixDet2 = (self.g[0][0] * self.g[1][1]) - (self.g[0][1] * self.g[1][0])
            return matrixDet2

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        #Initialize grid
        gridTrace = 0
        
        #The trace of an  𝑛×𝑛  square matrix  𝐀  is the sum of the elements on the main diagonal of the matrix
        for i in range(self.h):
            gridTrace += self.g[i][i]
        return gridTrace
        
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        # Declare variable for the determinant and Initialize inverse matrix
        det = self.determinant()
        matrixInv1 = []
        
        #For a  1×1  matrix with a single element with value  𝑎 , the inverse is simlpy  1/𝑎
        if self.h == 1:
            matrixInv1.append([1 / self.g[0][0]])
            return Matrix(matrixInv1)
        
        #For a  2×2  matrix the inverse is [[a b], [c d]]^-1 = (1 / determinant) * [[d -b], [-c a]]
        matrixInv2 = zeroes(self.h, self.w)
        
        #For matrix of size 2x2
        if self.h == 2:
            matrixInv2[0][0] = (1 / det) * self.g[1][1]
            matrixInv2[0][1] = (1 / det) * (-1 * self.g[0][1])
            matrixInv2[1][0] = (1 / det) * (-1 * self.g[1][0])
            matrixInv2[1][1] = (1 / det) * self.g[0][0]
        return matrixInv2
            
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        # initialize matrix to hold the results
        # For the transpose each row becomes the new column and vice versa [𝐀𝐓]𝑖𝑗=[𝐀]𝑗𝑖
        matrixTrans = zeroes(self.w, self.h)
           # Loop through columns on outside loop
        for c in range(self.w):
            # Loop through columns on inner loop
            for r in range(self.h):
                # Column values will be filled by what were each row before
                matrixTrans[r][c] = self.g[c][r]
        return matrixTrans

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 

        # initialize matrix to hold the results
        matrixSum = zeroes(self.h, self.w)
    
        # For loop within a for loop to iterate over the matrices
        for r in range(self.h):
            for c in range(self.w):
                # add the matrices
                matrixSum[r][c] = self[r][c] + other[r][c] 
        return matrixSum

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        # initialize matrix to hold the results
        matrixNeg = zeroes(self.h, self.w)
        
        ## For loop within a for loop to iterate over the matrix
        for r in range(self.h):
            for c in range(self.w):
                #Multiply matrix values by -1
                matrixNeg[r][c] = (-1 * self.g[r][c])
        return matrixNeg

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        # initialize matrix to hold the results
        matrixSub = zeroes(self.h, self.w)
    
        # For loop within a for loop to iterate over the matrices
        for r in range(self.h):
            for c in range(self.w):
                # subtract the matrices
                matrixSub[r][c] = self[r][c] - other[r][c] 
    
        return matrixSub

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        # initialize matrix to hold the results
        # An MxN matrix multiplied by an NxP matrix results in an MxP matrix
        matrixMul = zeroes(self.h, other.w)
        # row[r] x column[c] = newValueLocation[r][c]
        for r in range(matrixMul.h):
            for c in range(matrixMul.w):
                result = 0
                for i in range(self.w):
                    # An MxN matrix multiplied by an NxP matrix results in an MxP matrix
                    result += self[r][i]*other[i][c]
                    # replace the new values in the matrix
                matrixMul[r][c] = result
        return matrixMul

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            # initialize matrix to hold the results
            matrixrMul = zeroes(self.h, self.w)
            # A vector is a 1xN or Mx1 matrix and a scalar is a single element/value
            for r in range(self.h):
                for c in range(self.w):
                    # Take values from self input (left of * operator) and multiple by other
                    matrixrMul[r][c] = self.g[r][c] * other
            return matrixrMul
            