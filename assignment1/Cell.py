# This is a cell in a sudoku, consisting of row, column coordinates and a value. 
# row and column parameters are integers between 1..9,
# values are integers between 0 .. 9, with 0 indicating that the value is still unknown.

class cell:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val

        self.possible = []
        for p in range( 1, 10 ):
            self.possible.append( p )

    def getPossible(self):
        return self.possible

    def removePossible(self, val ):
        for p in range( 0, len( self.possible ) ):
            if( self.possible[p] == val ):
                self.possible.pop( p )



    def getRow(self):
        return self.row
    
    def setRow(self, row):
        self.row = row
        
    def getCol(self):
        return self.col
    
    def setCol(self, col):
        self.col = col
        
    def getVal(self):
        return self.val
    
    def setVal(self, val):
        self.val = val  
        
    def clone(self): 
        return cell(self.row, self.col, self.val)
