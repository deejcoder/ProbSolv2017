# Template for the algorithm to solve a sudoku. Builds a recursive backtracking solution
# that branches on possible values that could be placed in the next empty cell.
# Initial pruning of the recursion tree -
#       we don't continue on any branch that has already produced an inconsistent solution
#       we stop and return a complete solution once one has been found

import pygame, Sudoku_IO


def solve(snapshot, screen):
    # display current snapshot
    pygame.time.delay(200)
    Sudoku_IO.displayPuzzle(snapshot, screen)
    pygame.display.flip()

    # check if there are no more unsolved cells
    if (isComplete(snapshot)):
        return True

    else:
        clone = snapshot.clone()

        #minimize the possible solutions for each cell in current snapshot
        unsolved = checkSingletons(clone, screen)
        if( len( unsolved ) < 1 ): return True


        #select the first unsolved cell with minimal possibilities
        cell = unsolved[0]

        #get the list of all possible values for this cell
        possible = cell.getPossible()

        #if there are no possible values, solution is invalid
        if( len( possible ) < 1 ):
            return False

        #for all possible values for cell,
        for i in possible:

            cell.setVal(i)

            #check if the possible value is valid (pruning)
            if (IsConsistent(snapshot, cell)):

                #if valid, continue solution, move to the next cell (cell removed from unsolved cells),
                # if all friends return a valid solution, and therefore the puzzle is valid,
                # return the first solution found (pruning)
                if (solve(clone, screen)):
                    return True

        return False



        # if current snapshot is complete ... return a value
        # if current snapshot not complete ...
        # for each possible value for an empty cell
        #    clone current snapshot and update it,
        #    if new snapshot is consistent, perform recursive call
        # return a value

def checkSingletons( snapshot, screen ):

    #Pre condition: given the current state of the puzzle, snapshot, and screen for updating the screen
    #Post condition: all cells that are unsolved should have minimal possibilities of solutions

    unsolved = snapshot.unsolvedCells()

    for cell in unsolved:

        #loop invariant; for all cells till cell c, each cell should have minimal possibilities and if only 1 possibility,
            #set the cell to the only possibility (solution)

        row_values = snapshot.cellsByRow( cell.getRow() )
        col_values = snapshot.cellsByCol( cell.getCol() )
        block_values = snapshot.cellsByBlock( cell.getRow(), cell.getCol() )

        for i in range( 9 ):
            if row_values[i].getVal() in cell.possible:
                cell.possible.remove( row_values[i].getVal() )

            if col_values[i].getVal() in cell.possible:
                cell.possible.remove( col_values[i].getVal() )

            if block_values[i].getVal() in cell.possible:
                cell.possible.remove( block_values[i].getVal() )

        if( len( cell.possible ) == 1 ):
            cell.setVal( cell.possible[0] )
            #update the display if a cell has been set to its only possible solution

        if( len( cell.possible ) == 0 ):
            pass

    #sort the list of all unsolved, by their number of possible solutions
    unsolved = sorted( unsolved, key = lambda i:len(i.possible), reverse = False )
    Sudoku_IO.displayPuzzle(snapshot, screen)
    pygame.display.flip()

    return unsolved


# Check whether a snapshot is consistent, i.e. all cell values comply
# with the sudoku rules (each number occurs only once in each block, row and column).

def IsConsistent(snapshot, cell):
    # Precondition: snapshot: current state of puzzle, cell: current cell that has been given a possible solution
    # Postcondition: returns True if the current state follows the rules of Sudoku, else False

    row = cell.getRow()
    col = cell.getCol()
    number = cell.getVal()

    block_values = snapshot.cellsByBlock(row, col)
    row_values = snapshot.cellsByRow(row)
    col_values = snapshot.cellsByCol(col)

    # Assure for the solution assigned to cell, that there exists no cell in the same row, column or block that has the
    # same solution
    for i in range(9):
        if (block_values[i].getVal() == number):
            return False
        if (row_values[i].getVal() == number):
            return False
        if (col_values[i].getVal() == number):
            return False

    return True


# Check whether a puzzle is solved.
# return true if the sudoku is solved, false otherwise

def isComplete(snapshot):
    # If there is no single unsolved cell, return True (the puzzle is complete)
    if not (snapshot.getUnsolvedCell() == 0):
        return False
    return True

