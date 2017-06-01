graph = [
    [(1,2), (2,1)], # A
    [(3,2)], # B
    [(4,1)], # C
    [(5,1)], # D
    [(3,1)], # E
    [(3,2), (4,2)], # F
];




def walkEx( G, root, distances: list, firstWeight: int ):
    visited = [False for each in G]
    fifo = [root]
    distances[root] = firstWeight

    while len( fifo ) >= 1:
        v = fifo[0]
        fifo.remove( v )

        for n in range( len( G[v] ) ):
            neighbour = G[v][n][0]

            if( visited[neighbour] is True ):
                break

            print( neighbour )
            alt = distances[v] + G[v][n][1] + firstWeight
            print( "distance:", alt)
            if alt < distances[neighbour]:
                distances[neighbour] = alt

            visited[neighbour] = True
            fifo.append( neighbour )

    return distances

def shortest_paths( G, root ):

    distances = [float('inf') for each in G]

    for neighbour in G[root]:
        print( neighbour )
        addition = neighbour[1]
        distances = walkEx( G, neighbour[0], distances, addition )

    return distances



# expected: [0, 2, 1, 3, 2, 4]
print(shortest_paths(graph, 0))