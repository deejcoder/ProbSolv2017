"""

    Dijkstra's Algorithim Implementation
    - Used for positive weights only
    - one-to-all
    - priority queue to find min(distance)
    - suitable for shortest path
    - O( VlogV + E )
    - If priority queue wasn't implemented, it'll only work for simple walks


"""
# Needs priority queue implementation

graph = [
    [(1,2), (2,1)], # A
    [(3,2)], # B
    [(4,1)], # C
    [(5,1)], # D
    [(3,1), (6,2)], # E
    [(3,2), (4,2)], # F
    []
];def Dijkstra( G : list, start = 0 ):    Q = []    dist = []    prev = []    for i in range( len( G ) ):        dist.append( float('inf') )        prev.append( None )        Q.append( i )    dist[start] = 0    while len( Q ) >= 1:        v = min( Q )        Q.remove( v )        for s in range( len( G[v] ) ):            s_vert = G[v][s][0]            alt = dist[v] + G[v][s][1]            if alt < dist[s_vert]:                dist[s_vert] = alt                prev[s_vert] = v    return dist, prevprint( Dijkstra( graph ) )
