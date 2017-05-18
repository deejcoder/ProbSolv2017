

def maxIncreSeq( set, subset = [] ):
    for i in range( 0, len( set ) ):
        tmp = []
        tmp.append( set[i] )
        m = 0
        for k in range( i, len( set ) ):
            if( tmp[m] < set[k] ):
                tmp.append( set[k] )
                m += 1
        if( len( tmp ) > len( subset ) ):
            subset = tmp
    return subset

print( maxIncreSeq( [13, 2, 5, 11, 1, 7, 9, 3] ) )
