#----------------------------------------------------
#
# CMPUT 175
# Lab 3
#
# First name: Yi
# Last name: Yang
# Lab section: D04
#
# Description: This program prints out a square and checks whether or not it belongs to
# a magic square
#
#
#
#----------------------------------------------------


class MagicSquare:
    def __init__(self, n):
        '''
        Initializes an empty square with n*n cells.
        Inputs:  
           n (int) - number of rows in square, or equivalently, the number of columns
        Returns: None
        '''       
        self.square = []  # list of lists, where each internal list represents a row
        self.size = n  # number of columns and rows of square

        # Testing a non-zero square
        self.square = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 14, 15, 1]]
        self.size = n

        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.square.append(row)

        self.calculate = self.square

        self.isMagic()
        # For testing if the square is magic
        #if self.isMagic():
            #print('MAGIC SQUARE')
        #else:
            #print('nothing magic')

        self.drawSquare()


    def drawSquare(self):
        '''
        Displays the current state of the square, formatted with column and row 
        indices shown along the top and left side, respectively.
        Inputs: self.square
        Returns: None
        '''

        self.listofSquare = []
        for rowNum in range(self.size * 2 + 2):
            self.row = []
            for colNum in range(self.size):
                if rowNum == 0:   # First Row (indices)
                    self.row.append(" " * 4 + str(colNum))
                else:
                    if rowNum % 2 == 1:   # Every even number Row (+-----+)
                        if colNum == 0:
                            self.row.append("  +--")
                        if 0 < colNum < self.size:
                            self.row.append("-" * 5)
                        if colNum + 1 == self.size:
                            self.row.append("--+")
                    else:                          # Every odd number Row
                        numList = self.square[int((rowNum - 2) / 2)]
                        if colNum == 0:            # First Column (indices)
                            self.row.append(str(round((rowNum - 2) / 2)) + " ")
                        if 0 < colNum < self.size:   # Middle columns
                                cellPos = colNum - 1
                                cellNum = numList[cellPos]
                                #cellNum = int(cellNum)
                                #print(type(cellNum))
                                if cellNum != 0:
                                    if self.update(rowNum, colNum, cellNum):
                                        if cellNum >= 10:
                                            self.row.append("| " + str(cellNum) + " ")
                                        else:
                                            self.row.append("| " + str(cellNum) + "  ")
                                        self.listofSquare.append(cellNum)
                                    else:
                                        self.row.append("| .  ")
                                else:
                                    self.row.append("| .  ")
                        if colNum + 1 == self.size:   # Last column
                            if self.cellIsEmpty(rowNum, colNum) == False:   # Check if a cell is empty
                                cellNum = numList[colNum]
                                #cellNum = int(cellNum)
                                #print(type(cellNum))
                                if cellNum != 0:
                                    if self.update(rowNum, colNum, cellNum):
                                        if cellNum >= 10:
                                            self.row.append("| " + str(cellNum) + " |")
                                        else:
                                            self.row.append("| " + str(cellNum) + "  |")
                                        self.listofSquare.append(cellNum)
                                    else:
                                        self.row.append("| .  |")
                                else:
                                    self.row.append("| .  |")
                            else:
                                self.row.append("|    |")
            self.square.append(self.row)

        if self.square[0][1] == 0:
            del self.square[0:self.size]
        else:
            del self.square[0:self.size]

        for i in self.square:   # Print out the square
            for item in i:
                print(item, end="")
            print()

    def cellIsEmpty(self, row, col):
        '''
        Checks if a given cell is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of cell to check
           col (int) - column index of cell to check
        Returns: True if cell is empty; False otherwise
        '''
        rowNum = int((row - 2) / 2)
        self.listatRow = self.square[rowNum]
        self.isFull()

        if len(self.listatRow) < self.size:
            print("empty")
            return True
        else:
            return False


    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the cell at the provided row and column, 
        but only if that cell is empty and only if the number isn't already 
        in another cell in the square (i.e. it is unique)
        Inputs:
           row (int) - row index of cell to update
           col (int) - column index of cell to update
           num (int) - entry to place in cell
        Returns: True if attempted update was successful; False otherwise
        '''

        if num not in self.listofSquare:
            return True
        else:
            return False
    
    
    def isFull(self):
        '''
        Checks if the square has any remaining empty cells.
        Inputs: N/A
        Returns: True if the square has no empty cells (full); False otherwise
        '''

        if int(len(self.listofSquare) + 1) == self.size:
            return True
        else:
            return False

           
    def isMagic(self):
        '''
        Checks whether the square is a complete, magic square:
          1. All cells contain a unique number
          2. All lines sum up to the same value (horizontals, verticals, diagonals)
          
        Inputs: N/A
        Returns: True if square is magic; False otherwise
        '''

        del self.calculate[self.size:self.size * 2]
        #print(self.calculate)
        checking = 0
        horizontal = 0
        for i in range(len(self.calculate)):
            checking = checking + self.calculate[0][i]

        for i in range(len(self.calculate)):
            for j in range(len(self.calculate)):
                horizontal = horizontal + self.calculate[j][i]
            if horizontal == checking:
                return True
            else:
                return False

        vertical = 0
        for i in range(len(self.calculate)):
            for j in range(len(self.calculate)):
                vertical = vertical + self.calculate[i][j]
            if vertical == checking:
                return True
            else:
                return False

        diagonal1 = 0
        for i in range(len(self.calculate)):
            for j in range(len(self.calculate)):
                if i + 1 < len(self.calculate):
                    diagonal1 = diagonal1 + self.calculate[j][i + 1]
            if diagonal1 == checking:
                return True
            else:
                return False

        diagonal2 = 0
        for i in range(len(self.calculate)):
            for j in range(len(self.calculate)):
                if i + 1 < len(self.calculate):
                    diagonal2 = diagonal2 + self.calculate[len(self.calculate) - j][i]
            if diagonal2 == checking:
                return True
            else:
                return False


if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # complete the suggested tests; more tests may be required
    
    # start by creating empty square and checking the contents of the square attribute
    mySquare = MagicSquare(4)
    #mySquare.update(2,2,3)
    #mySquare.drawSquare()
    # print(mySquare.square)
    
    # does the empty Magic Square display properly?
    

    # assign a number to an empty cell and display
    
    
    # try to assign a number to a non-empty cell. What happens?
        
    
    # check if the square is a magic square. Should it be after only 1 entry?
    
    
    # check if the square is full. Should it be full after only 1 entry?
    
    
    # add values to the square so that every line adds up to 21. Display
    
    
    # check if the square is magic
    
    
    # check if the square is full
    
    
    # write additional tests, as needed

