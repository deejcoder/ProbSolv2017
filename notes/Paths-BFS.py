"""    Breadth-First Search Implmenetation    - O( V + E )    - Doesn't work on weighted graphs    - Isn't suitable for shortest distance    - Similar to Depth First Search (which uses a stack instead i.e taking last value).""""""              H
              ^
     +-->E+   |
 +>B +   ^--->G
 |       |    ^
A+------>D+   |
|   +---^ |   |
+->C+     +-->F
"""graph = [    # Node  | Successors (neighbours [uses indexes])    ('A', [1,2]),    ('B', [3,4]),    ('C', [3]),    ('D', [4,5]),    ('E', [6]),    ('F', [6]),    ('G', []),    ('H', [6])]def BFS( G, start = 0 ):    distances = [ float('inf') for v in range( len( G ) ) ]    distances[start] = 0    # stores neighbours unexplored    unexplored = []     unexplored.append( start )    # If length < 1: there are no more successors    while len( unexplored ) >= 1:        v = unexplored[0]        unexplored.remove( v )        for neighbour in G[v][1]:            """                Avoid acyclic directed graphs:                ~inf, has already been explored            """            if distances[neighbour] == float('inf'):                distances[neighbour] = distances[v] + 1                unexplored.append( neighbour )    return distances"""    Output the distances,    "how much steps to reach this node""""nodes, distances = "",""for node, distance in enumerate( BFS( graph, 0 ) ):    nodes += "{0}\t".format( graph[node][0] )    distances += "{0}\t".format( distance )print( nodes )print( distances )