import fileFuncs
import time
#import linkedlists AS list

#import the dictionary of words
dictionary = fileFuncs.fetchFileContent( "words.txt" )


starttime = time.time()


#sort a word, key: A-Z
#firstWordd = sorted( dictionary[19100] )

#firstWord = ""
#for char in firstWordd:
#    firstWord += char

output = {}
#precondition: given a dictionary of words, plus a starting word




counts = {}

for word in dictionary:
    #loop invariant: all words so far till "word" has been appended to their "set" of matching anagrams, if none, then they're alone

    #property of anagram: length = length
   # if( len( word ) != len( firstWord ) ):
    #    continue

    #compare the two words
    compareWordd = sorted( word )
    compareWord = ""
    for char in compareWordd:
        compareWord += char

    try:
        #python's dictionary method uses hashing, creating a fingerprint...
        if( output[compareWord] ):
            wordlist = []
            count = 0
            for words in output[compareWord][0]:
                wordlist.append( words )
                count += 1

            count += 1

            wordlist.append( word )
            output[compareWord] = [wordlist, count]
            try:
                counts[count] = [counts[count], output[compareWord]]
            except: counts[count] = [output[compareWord]]



            #print( output[compareWord] )
    except:
        output[compareWord] = [[word], 1]
        try:
            if( counts[1] ):
                counts[1] = [counts[1], output[compareWord]]
        except:
            counts[1] = [output[compareWord]]

#post condition: printed all words that are anagrams
#lasted
endtime = time.time()
print("completed in: %g" % (endtime - starttime))

maxkeycount = 0
maxkey = ""


for key in counts:
    if( key > 6 ):
        for l in counts[key][0][0]:
            print( l )
       # print( counts[key] )
#for key in output:



    #print(output[key])
   # if( output[key][1] > maxkeycount ):
    #    maxkey = key
   #     maxkeycount = output[key][1]
       # print( maxkeycount )

#print( output[maxkey] )



#print( output )
