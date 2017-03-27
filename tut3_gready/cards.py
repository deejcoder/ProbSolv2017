#   Dylan Tonks
#   Student ID 16058989
#   Computational Thinking for Problem Solving 159.271
#   Tutorial 3

import random

defence = []
attack = []
pairs = []
n = 0
worthSum = 0


n = input( "Enter the amount of cards that should be dealt (for each Attack and Defence collection): " )
n = int( n )


for i in range( 0, n ):
    defence.append( [random.randrange(1, n), random.randrange( 1,n )] )
    # Where the second index of the 2D array is weather or not the card has been used
    attack.append( [random.randrange( 1,n ), False] )
#sort by worth high to low
defence.sort( reverse = True )

#sort by attack ability high to low
attack.sort( reverse = True );


for d in range( n ):
    defWorth = defence[d][0]
    defAb = defence[d][1]

    attkAb = attack[0][0]

    a = 1
    highAttk = 0

    #find the highest attack card such that this defence card can beat it
    #ignore: cards that are already used
    #range: till n
    while( ( defAb < attkAb or attack[a][1] is True ) and a < n - 1 ):
        a += 1
        attkAb = attack[a][0]

        #if not used keep track of the highest attack
        if( not attack[a][1] ):
            if( attack[a][0] > highAttk ):
                highAttk = a


    #Suppose all unused attack cards cannot be beaten by this card
    if( defAb < attkAb or attack[a][1] ):

        #Pair the defence card with the highest attack card
        pairs.append( ( defence[d][1], attack[highAttk][0] ) )

        #The attack card has now been used
        attack[highAttk][1] = True

    else:

        #The defence cards beats an attack card (the highest it can beat), so pair them
        pairs.append( ( defence[d][1], attack[a][0] ) )

        #The defence card remains alive so add to the overall worth
        worthSum += defWorth


        attack[a][1] = True


print( "Defence cards: ", defence );
print( "Attack cards: " ,attack ,"\n" );

for i in range( n ):
    print( pairs[i], defence[i][1], attack[pairs[i][1]][0] );
print( "Total Worth: %d" % worthSum );