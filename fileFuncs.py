def fetchFileContent( file ):


    f = open( file, "r" )
    try:
        list = []

        #All lines till line shall be contained in list
        for line in f.readlines():
            list.append( line.strip() )

        return list

    except FileNotFoundError:
        print( " fetchFileContent: file not found." )

