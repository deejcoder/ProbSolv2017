def msum(a):

    bounds = (0,0)
    max = 0
    sum = 0
    j = 0

    for i in range( len( a ) ):
        sum += a[i]

        if( sum > max ):
            max = sum
            bounds = (j, i+1)

        if( sum < 0 ):
            """
                Reset the temporary sum, but
                the max sum so far is still
                saved as 'max'
                
                Move onto the next possible subset
                by setting lower bound, j
            """
            sum = 0
            j = i + 1

        else:
            """
                Do nothing, instead keep summing!
            """
            pass

    return (max, bounds)

"""
    Negative indices: the number after this may
    contribute to make the sum larger.
    The maximum sum is still stored as 'max' for this reason
"""
print( msum( [1,3,-2,5,3,9] ) )