#   Dylan Tonks
#   Student ID: 16058989
#   Tutorial 2
#   Computational Thinking for Problem Solving, 159.271

import pygame
import random


#GLOBAL DEFINITIONS
# Defi25ne some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)


#Grid prefixes

#This constant is fun to play with, I've set it to 10 so the cheese can be seen
GRID_SCALE = 5 #1 or some multiple of 5 { x | x is 1 or x is divisble by 5 }

GRID_SIZE = 1000
GRID_SCALED_SIZE = int( GRID_SIZE/GRID_SCALE )

#Object prefixes
COLOR_WALL = black
COLOR_FLOOR = white
COLOR_CHEESE = red

#Room & Door prefixes
DOOR_SIZE = 5
MIN_ROOM_SIZE = 25
CHEESE_SIZE = 2
 


# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size=[GRID_SIZE,GRID_SIZE]
screen=pygame.display.set_mode(size)
# Set the screen background
screen.fill(white)
      
# Set title of screen
pygame.display.set_caption("Random Maze")
 
# Create a 2 dimensional array. A two dimensional
# array in our implementation is simply a list of lists.
# Each cell corresponds to a 5 pixel x 5 pixel area of the screen surface.
mazegrid=[]
for row in range(GRID_SCALED_SIZE):
    # Add an empty array that will hold each cell in this row
    mazegrid.append([])
    for column in range(GRID_SCALED_SIZE):
        mazegrid[row].append(0) # Append a cell


def GenerateMaze():
    #Initial condition; create walls around maze's border, door at upper left corner
    for col in range( GRID_SCALED_SIZE):
        mazegrid[0][col] = COLOR_WALL
        mazegrid[len(mazegrid)-1][col] = COLOR_WALL;

    for row in range( GRID_SCALED_SIZE ):
        mazegrid[row][0] = COLOR_WALL
        mazegrid[row][len(mazegrid[row])-1] = COLOR_WALL

    for row in range( 0, DOOR_SIZE ):
        mazegrid[row][0] = COLOR_FLOOR
    for col in range( 0, DOOR_SIZE ):
        mazegrid[0][col] = COLOR_FLOOR

    #subtract the first room's walls by starting at (1,1), (199, 199) room size
    AddWalls( ( ( 1, 1 ), ( GRID_SCALED_SIZE - 1, GRID_SCALED_SIZE - 1 ) ), 0, 1 )

def addDoors( row, col, roomcoords ):
    #Precondition: given the row, col where the "new walls" were added,
    ##  and the coordinates of the current room

    (x1, y1), (x2, y2) = roomcoords
    #add the doors
    for c in range( -DOOR_SIZE, DOOR_SIZE+1 ):
        #Loop invariant: removes a "wall" and replaces with "floor" such that a door belongs there,
        #  for every i examined so far

        xpos = row - c
        ypos = col - c

        #only remove walls if it's inside the room
        if( xpos < x2 and xpos > x1 ):
            mazegrid[col][row-c] = COLOR_FLOOR
        if( ypos < y2 and ypos > y1 ):
            mazegrid[col-c][row] = COLOR_FLOOR

    #Post condition; updates the 2D array to contain the doors for the added rooms

def AddWalls(roomcoords, cheeseflag, first = 0):
    #PRECONDITION: given the current 'roomcoords', and weather or not this room should contain cheese,
    # and weather or not it's the first room added in the maze

    (x1,y1), (x2, y2) = roomcoords
    rwidth = abs( x2 - x1 )
    rheight = abs( y2 - y1 )

    #BASE CASES: the room must be large enough such that it can be subdivided, therefore width, height if it's <= 10,
    #   add the cheese (as it's the last room that is being created), then escape the sub instance
    if( rwidth <= 10 or rheight <= 10 ):
        if (cheeseflag):

            #generate random position inside the room for the cheese
            cheeseposX = random.randrange( x1+CHEESE_SIZE, x2-CHEESE_SIZE )
            cheeseposY = random.randrange( y1+CHEESE_SIZE, y2-CHEESE_SIZE )
            mazegrid[cheeseposX][cheeseposY] = COLOR_CHEESE
        return



    #Generate a random room at some random row, column such that each room should be big enough, and not touching
    #   existing walls
    midX = random.randrange( x1+5, x2-5 )
    midY = random.randrange( y1+5, y2-5 )

    #add the walls in the randomly generated row, col
    for row in range( y1, y2 ):
        mazegrid[row][midX] = COLOR_WALL

    for col in range( x1, x2 ):
        mazegrid[midY][col] = COLOR_WALL


    #create doors in the newly created walls
    addDoors( midX, midY, roomcoords )

    #set the cheeseflag, randomly choose an intial room
    room = cheeseflag
    if( first == 1 ):
        room = random.randint( 1, 3 )

    #FRIENDS: divide the room into four, let the friends handle those subdivisions
    AddWalls( ( ( x1, y1 ), (midX, midY ) ), 0 ) #1st - starting room
    AddWalls( ( (midX, midY), (x2, y2) ), 1 if room == 1 else 0 ) #4th
    AddWalls(((midX, y1), (x2, midY)), 1 if room == 2 else 0 ) #2nd
    AddWalls(((x1, midY ), (midX, y2)), 1 if room == 3 else 0 ) #3rd




def DisplayMaze():
    for row in range( 0, GRID_SCALED_SIZE):
        for col in range( 0, GRID_SCALED_SIZE):
            if( mazegrid[row][col] == COLOR_WALL ):
                pygame.draw.rect( screen, COLOR_WALL, [col*GRID_SCALE, row*GRID_SCALE, GRID_SCALE, GRID_SCALE] );
            if( mazegrid[row][col] == COLOR_CHEESE ):
                pygame.draw.rect(screen, COLOR_CHEESE, [col * GRID_SCALE, row * GRID_SCALE, GRID_SCALE*CHEESE_SIZE, GRID_SCALE*CHEESE_SIZE]);



# Loop until the user clicks the close button.
done=False


# Used to manage how fast the screen updates
clock=pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN: # If user wants to perform an action
                if event.key == pygame.K_m:
                    GenerateMaze()
                    DisplayMaze()
   
    
  

    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
# If you forget this line, the program will 'hang' on exit.
pygame.quit ()