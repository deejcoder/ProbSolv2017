class Node:
    def __init__( self, data ):
        self.data = data
        self.next = None

class List:
    def __init__( self ):
        self.head = None
        self.last = None
        self.count = 0

    def append( self, data ):
        node = Node( data )

        if( self.head is None ):
            self.head = node
            self.last = node

        else:
            node.next = self.last
            self.last = node

        self.count += 1

    def fetch( self, i ):
        if( i == 0 ):
            return self.head.data

        if( i == self.count ):
            return self.last.data

        current = self.head
        atindex = 0

        while( current != None ):
            if( atindex == i ):
                return current.data

            current = current.next


