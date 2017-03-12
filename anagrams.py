import fileFuncs
import time
#import linkedlists AS list

#import the dictionary of words
dictionary = fileFuncs.fetchFileContent( "words.txt" )

starttime = time.time()

output = {}
LIMIT = 5
#precondition: given a dictionary of words, plus a starting word

for word in dictionary:
    #loop invariant: all words so far till "word" has been appended to their "set" of matching anagrams, if none, then they're alone

    #property of anagram: length = length

    #compare the two words
    compareWord = ''.join( sorted( word ) )


    try:
        #python's dictionary method uses hashing, creating a fingerprint...

        output[compareWord].append( word )

    except:
        output[compareWord] = [word]

#post condition: printed all words that are anagrams

for anagrams in sorted( output.values(), reverse = True, key = lambda x:len(x) ):
    if( len( anagrams ) >= LIMIT ):
        print( anagrams );

endtime = time.time()
print("completed in: %g" % (endtime - starttime))