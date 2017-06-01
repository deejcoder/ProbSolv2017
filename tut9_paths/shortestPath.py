"""

    Tutorial 9 - Shortest Paths
    Student ID 16058989
"""

graph = [
    [(1,2), (2,1)], # A
    [(3,2)], # B
    [(4,1)], # C
    [(5,1)], # D
    [(3,1)], # E
    [(3,2), (4,2)], # F
];



def shortest_paths( G, root ):    """        - distances stores the current known distance between root and node A.        - fifo is a temporary `queue` which stores the current nodes being/to be explored    """    distances = [float('inf') for each in G]    fifo = []    fifo.insert( 0, root )    distances[root] = 0    while len( fifo ) >= 1:        v = fifo[0]        fifo.remove( v )                 for n in range( len( G[v] ) ):             neighbour = G[v][n][0]            weight = G[v][n][1]            cur_distance = distances[v] + weight            """                Set of all counting numbers between 1,2 inclusive, treating a weight of two as two nodes.            """            if distances[neighbour] == float('inf') or distances[neighbour] > cur_distance:                distances[neighbour] = cur_distance                #insert at the front of the list                fifo.insert( 0, neighbour )    return distancesprint( shortest_paths( graph, 0 ))