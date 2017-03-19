def fetchFileContent( file ):
    #   % precondition %: file is a string containing the file's path.
    #   % post condition %: returns a list containing all the data from the file.

    f = open( file, "r" )
    try:
        list = []

        #   % Loop invariant %: all lines till the ith line shall be contained in "list"
        for line in f.readlines():
            list.append( line.strip() )

        return list

    except FileNotFoundError:
        print( " fetchFileContent: file not found." )

