from building import *

# speed test - use "python optimizer.py" to run
if __name__ == "__main__":
    import timeit
    test_size = 100  # set to 100 to check time for speed race
    t1 = timeit.repeat(stmt="optimizer.max_food(b)", setup="import gc, building, optimizer; b = building.random_building({0}, True); gc.collect()".format(test_size), repeat=3, number=1)
    t2 = timeit.repeat(stmt="optimizer.max_supplies(b)", setup="import gc, building, optimizer; b = building.random_building({0}, False); gc.collect()".format(test_size), repeat=3, number=1)
    # some calculation that takes ~1 sec on my machine
    tref = timeit.repeat(stmt="for i in range(1000000): a=i^2", setup="import gc; gc.collect()", repeat=3, number=19)
    print("max_food(n={0}) = {1} ({3} normalized), max_supplies(n={0}) = {2} ({4} normalized)".format(test_size, min(t1), min(t2), min(t1) / min(tref), min(t2) / min(tref)))


"""
    METHOD: Breaks the grid into four quadrants so that each quadrant may be 

"""

def getQuadrants( grid, size ):

    length = len(grid[0])

    tl = []
    for i in range( size + 1 ):
        tl.append(grid[i][:size + 1])

    tr = []
    for i in range( size + 1):
        tr.append(grid[i][size:])

    bl = []
    for i in range( size, length ):
        bl.append( grid[i][:size + 1] )

    br = []
    for i in range( size, length):
        br.append(grid[i][size:])

    return tl, tr, bl, br


"""
    METHODS: to normalize the quadrant such that
    they're all in the same form, with @ at row 0, column 0
    Bottom right is already in the right form.

"""

def normalizeBottomLeft( quad ):
    normal = []

    for row in quad:
        """
            The bottom left needs its columns
            reversed such that @ is at 0,0
        """
        row.reverse()
        normal.append( row )
    
    return normal

def normalizeTopLeft( quad ):

    normal = []

    """
        The top left needs its rows and columns are reversed
        such that @ is at 0,0
    """

    quad.reverse()

    for row in quad:
        row.reverse()
        normal.append( row )

    return normal

def normalizeTopRight( quad ):

    """
        Simply reversing the rows will place @ at 0,0
    """
    quad.reverse()


    return quad


def max_food(building):
    """returns the maximum number of food that can be collected from given building"""
    grid = building.rooms
   # n = building.size*2 + 1
    size = building.size

    #S = grid
    #S[size][size] = Supplies( -float('infinity' ))
    #max_food_quadrant( building, split_grid( grid, 0, size ), size )

    S = [[ item.food for item in row ] for row in grid]

    # Split the quadrants up
    lists = getQuadrants( S, size )

    # Transform the quadrants, br already in form
    br = lists[3]
    tl = normalizeTopLeft( lists[0] )
    tr = normalizeTopRight( lists[1] )
    bl = normalizeBottomLeft( lists[2] )


    # Get the best solution in the form [(food,water),...]
    poss_tl = max_food_quadrant( tl )
    poss_tr = max_food_quadrant( tr )
    poss_bl = max_food_quadrant( bl )
    poss_br = max_food_quadrant( br )
    return max( poss_tl, poss_tr, poss_bl, poss_br )
   # return building.size * 10 # dummy implementation - replace


def max_food_quadrant(quad):

    """
        1. For each cell in row 0 or column 0: cell.food = this.food + previous.food
        2. For each cell in row > 0 and column > 0: cell.food = cell.food + max( above.food, previous.food )
        3. Do not touch cell at (0,0)

    """


        
    for row in range( 0, len( quad ) ):
        for col in range( 0, len( quad ) ):

            if( row is 0 and col is 0 ):
                continue

            if( row == 0 ):
                if( col == 1 ):
                    continue # Nothing to compute (first from @)

                quad[row][col] += quad[row][col - 1]
                continue

            if( col == 0 ):
                if( row == 1 ):
                    continue # Nothing to compute (first from @)

                quad[row][col] += quad[row - 1][col]
                continue

            else:
                quad[row][col] += max( quad[row][col - 1], quad[row - 1][col] )



    return quad[-1][-1]



    

def max_supplies(building):
    """returns the maximum of min(food,water) that can be collected from given building"""

    grid = building.rooms
    size = building.size

    S = [[ [item.food, item.water] for item in row ] for row in grid]

    # Split the quadrants up
    lists = getQuadrants( S, size )

    # Transform the quadrants, br already in form
    br = lists[3]
    tl = normalizeTopLeft( lists[0] )
    tr = normalizeTopRight( lists[1] )
    bl = normalizeBottomLeft( lists[2] )

    poss_tl = max_supplies_quadrant( tl )
    poss_tr = max_supplies_quadrant( tr )
    poss_bl = max_supplies_quadrant( bl )
    poss_br = max_supplies_quadrant( br )
    best = bestTuple( poss_tl + poss_tr + poss_bl + poss_br  )
    print( best )
    return min( best[0], best[1] )


def max_supplies_quadrant(quad):
    #for i in quad:
    #    print( i )
    possibilities = {}

    for row in range( 0, len( quad ) ):
        for col in range( 0, len( quad ) ):
            if( row is 0 and col is 0 ):
                continue

            if( row == 0 ):
                if( col == 1 ):
                    # Row 0, Col 1: initial possibility
                    possibilities[(row,col)] = [
                        (quad[row][col][0],quad[row][col][1])
                    ]
                    continue

                # Add the food and water up along the first row, store as cell's single possibility
                possibilities[(row,col)] = [
                    (quad[row][col][0] + quad[row][col - 1][0], quad[row][col][1] + quad[row][col - 1][1])
                ]
                continue


            if( col == 0 ):
                if( row == 1 ):
                    possibilities[(row,col)] = [
                        (quad[row][col][0],quad[row][col][1])
                    ]
                    continue

                # Add the food and water up along the first column, store as cell's single possibility
                possibilities[(row,col)] = [
                    (quad[row][col][0] + quad[row - 1][col][0], quad[row][col][1] + quad[row - 1][col][1])
                ]
                continue

            else:
              previous = possibilities[(row, col - 1)]
              above = possibilities[(row - 1, col)]
              #print( above )

              tmp = []

              possible_list = previous + above
          
              for supplies in possible_list:
                   add = True
                   adding = (supplies[0] + quad[row][col][0], supplies[1] + quad[row][col][1] )
                      
                   for option in tmp:
                       if( adding[0] <= option[0] and adding[1] <= option[1] ):
                           add = False
                           break
                       elif( adding[0] <= option[0] and adding[1] >= option[1] ):
                           tmp.remove( option )
                   if( add ):
                       tmp.append( adding )
              possibilities[(row,col)] = tmp
   
    return possibilities[(len(quad)-1,(len(quad)-1))]
    #print("Final square possibilities:", possibilities[(len(quad)-1,(len(quad)-1))])

    
def bestTuple( list ):
    best = (0,0)
    for i in range( 0, len( list ) ):
        if min( list[i][0], list[i][1] ) > min( best[0], best[1] ):
            best = list[i]
    return best