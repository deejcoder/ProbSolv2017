grid = [[]]
p = [[]]
def C( i, j ):
    return grid[i][j]

def computeShortestPathArrays(n):
    for x in range( 1, n ):
        q[1, x] = C( 1, x )

    for y in range( 1, n ):
        q[y, 0] = float('infinity')
        q[y, n + 1] = float( 'infinity' )

    """
        Go through the entire grid starting gat (2,1),
        working way down finding minimal path (per square).

    """
    for y in range( 2, n ):
        for x in range( 1, n ):
            m = min( 
                q[y - 1, x - 1],
                q[y - 1, x],
                q[y - 1, x + 1]
            )
            m += C(y, x)

            """
                Add the minimal path for this square, into p

            """
            if m is q[y - 1, x - 1]:
                p[y, x] = -1

            elif m is q[y - 1, x]:
                p[y, x] = 0

            else:
                p[y, x] = 1

def computeShortestPath(n):
    computeShortestPathArrays(n)
    minIndex = 1
    min = q[n, 1]

    """
        Find the index at the bottom of the grid,
        with the minimum path (or value)

    """
    for i in range(2, n):
        if q[n, i] < min:
            minIndex = i
            min = q[n, i]


def printPath(y, x ):
    print(x)
    print("<-")
    
    if y is 2:
        print( x + p[y, x] )
    else:
        printPath(y - 1, x + p[y, x] )