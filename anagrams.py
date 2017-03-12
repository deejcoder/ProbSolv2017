import fileFuncs
import time


#   properties of anagrams: same length, same letters used.
#       hence ordering each word into A-Z, each word that are anagrams of each other will be the same.

def getAnagrams( list ):
    #   % precondition %: list is a list of words.
    #   % post condition %: prints in descending order based on the amount of anagrams in each set, the sets of anagrams belonging to each other.

    starttime = time.time()

    # anagrams stores the sets of anagrams
    dictionary = {}



    for word in list:
        #   % loop invariant %: there are ith words in lists referenced by a dictionary, sorting each word into A-Z form for a "key"
        #       It should be noted in Python, dictionaries rely on hash tables such that "key" is a reference to the hash table.


        #the sorted() method returns a list of characters, so join these back into a string
        key = ''.join( sorted( word ) )


        try:
            # if there already exists an entry with the same signature, add the word
            dictionary[key].append( word )

        except:
            # else create a new entry
            dictionary[key] = [word]


    # sorted() method uses the timsort algorithim
    for anagrams in sorted( dictionary.values(), reverse = True, key = lambda x: len(x) ):
        #   % Loop invariant %: all sets that have been printed have more anagrams than the ith set.
        #           set: a collection of words that are anagrams of each other

        # those of length 1 have no anagrams
        if( len( anagrams ) >= 2 ):

            #record print time
            printstart = time.time()

            print( anagrams )

            # subtract print time from timing
            starttime -= ( printstart - time.time() )

    endtime = time.time()
    print("completed in: %g" % (endtime - starttime))



# import the dictionary of words and store it as a list
wordlist = fileFuncs.fetchFileContent( "words.txt" )
getAnagrams( wordlist )




# Below is the old method of printing all the anagrams, that I was using
#   the above was proven more efficient though through timing

# counts = {}
# highestCount = 0
# for key in output:
#     try:
#         length = len( output[key] )
#         counts[length].append( output[key] )
#
#         if( length > highestCount ):
#             highestCount = length
#     except:
#         counts[len(output[key])] = [output[key]]
#
# for i in range( highestCount, 1, -1 ):
#     try:
#         if( len( counts[i] ) > 1 ):
#             for item in counts[i]:
#                 print( item )
#         else:
#             print( item )
#     except:
#         continue





