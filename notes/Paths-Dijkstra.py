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
];