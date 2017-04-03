# Template for the algorithm to solve a sudoku. Builds a recursive backtracking solution
# that branches on possible values that could be placed in the next empty cell. 
# Initial pruning of the recursion tree - 
#       we don't continue on any branch that has already produced an inconsistent solution
#       we stop and return a complete solution once one has been found

import pygame, Sudoku_IO

def solve(snapshot, screen ):
    # display current snapshot
    pygame.time.delay(1)
    Sudoku_IO.displayPuzzle(snapshot, screen)
    pygame.display.flip()

    if( isComplete( snapshot ) ):
        return True

    else:
        clone = snapshot.clone()
        cell = clone.getUnsolvedCell()
        for i in range( 1, 10 ):

            cell.setVal(i)

            if( IsConsistent( snapshot, cell ) ):
                if( solve( clone, screen ) ):
                    return True

        return False



    # if current snapshot is complete ... return a value
    # if current snapshot not complete ...
    # for each possible value for an empty cell
    #    clone current snapshot and update it,
    #    if new snapshot is consistent, perform recursive call
    # return a value




    

# Check whether a snapshot is consistent, i.e. all cell values comply 
# with the sudoku rules (each number occurs only once in each block, row and column). 
     
def IsConsistent(snapshot, cell):
    row = cell.getRow()
    col = cell.getCol()
    number = cell.getVal()

    block_values = snapshot.cellsByBlock( row, col )
    row_values = snapshot.cellsByRow( row )
    col_values = snapshot.cellsByCol( col )

    for i in range( 9 ):
        if( block_values[i].getVal() == number ):
            return False
        if( row_values[i].getVal() == number ):
            return False
        if( col_values[i].getVal() == number ):
            return False


    return True

# Check whether a puzzle is solved. 
# return true if the sudoku is solved, false otherwise
     
def isComplete(snapshot):
    if not( snapshot.getUnsolvedCell() == 0 ):
        return False
    return True

