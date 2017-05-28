from building import *

# speed test - use "python optimizer.py" to run
if __name__ == "__main__":
    import timeit
    test_size = 1000 # set to 100 to check time for speed race
    t1 = timeit.repeat(stmt="optimizer.max_food(b)", setup="import gc, building, optimizer; b = building.random_building({0}, True); gc.collect()".format(test_size), repeat=3, number=1)
    t2 = timeit.repeat(stmt="optimizer.max_supplies(b)", setup="import gc, building, optimizer; b = building.random_building({0}, False); gc.collect()".format(test_size), repeat=3, number=1)
    # some calculation that takes ~1 sec on my machine
    tref = timeit.repeat(stmt="for i in range(1000000): a=i^2", setup="import gc; gc.collect()", repeat=3, number=19)
    print("max_food(n={0}) = {1} ({3} normalized), max_supplies(n={0}) = {2} ({4} normalized)".format(test_size, min(t1), min(t2), min(t1) / min(tref), min(t2) / min(tref)))


def split( grid ):
	length = len(grid[0])
	topleft = []
	for ind in range(0,(length//2)+1):
		topleft.append(grid[ind][:(length//2)+1])
	topright = []
	for ind in range(0,(length//2)+1):
		topright.append(grid[ind][(length//2):])
	bottomleft = []
	for ind in range((length//2), length):
		bottomleft.append(grid[ind][:(length//2)+1])
	bottomright = []
	for ind in range((length//2), length):
		bottomright.append(grid[ind][(length//2):])

	return topleft, topright, bottomleft, bottomright

def trans_BL(inp):
	output = []
	for row in inp:
		row.reverse()
		output.append(row)
	return output

def trans_TL(inp):
	output = []
	inp.reverse()
	for row in inp:
		row.reverse()
		output.append(row)
	return output

def trans_TR(inp):
	inp.reverse()
	return inp

def max_food(building):
    """returns the maximum number of food that can be collected from given building"""
    grid = building.rooms
   # n = building.size*2 + 1
    #size = building.size

    #S = grid
    #S[size][size] = Supplies( -float('infinity' ))
    #max_food_quadrant( building, split_grid( grid, 0, size ), size )

    S = [[ item.food for item in row ] for row in grid]
    lists = split(S)
    topleft = trans_TL(lists[0])
    topright = trans_TR(lists[1])
    bottomleft = trans_BL(lists[2])
    bottomright = lists[3]

    """for i in topleft:
        print([item.food for item in i])
        
    print("")
    for i in topright:
        print([item.food for item in i])

    print("")
    for i in bottomleft:
        print([item.food for item in i])

    print("") 
    for i in bottomright:
        print([item.food for item in i])"""


    #print( split_grid( grid, 0, size ) )
    """
   for i in topleft:
        print( [item for item in i] )
    print("")
    """



    tl = max_food_quadrant( topleft )
    tr = max_food_quadrant( topright )
    bl = max_food_quadrant( bottomleft )
    br = max_food_quadrant( bottomright )
    return max( tl, tr, bl, br )
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
    return building.size * 5 # dummy implementation - replace
