


def path( G ):

    topo = []

    while len( G ) is not None:

        node = 0
        topo.append ( visit( node, G ) )
    print( topo )


def visit( node, G, marks = [False], ordered = [] ):
    if len( marks ) < 2:
        marks = [False]*len( G )

    print( node )
    if marks[node]:
        print( "ERROR: The grah is directed acyclic graph." )
        exit()

    marks[node] = True
    
    for neighbour in range( len( G[node] ) ):
        visit( G[node][neighbour][0], G, marks )

    ordered.append( G[node] )
    G.remove( G[node] )
    return ordered

graph = [
    [(1,2), (2,1)], # A
    [(3,2)], # B
    [(4,1)], # C
    [(5,1)], # D
    [(3,1)], # E
    [(4,2)], # F
];

path( graph )