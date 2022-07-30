# Conway's Game of Life in python. Written with vim

import random, time, copy

WIDTH = 60
HEIGHT = 20

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')              # add a "living" cell
        else:
            column.append(' ')              # add a "dead" cell
    nextCells.append(column)                # nextCells is a list of column lists

while True:
    print('\n\n\n\n\n')                     # separates each step with new lines
    currentCells = copy.deepcopy(nextCells)
    
    # prints current cells onto screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')   # print the # or space
        print()                                 # print new line at end of each row

    # calculate next steps cells take based on current cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # gets neighboring coordinates
            # "% WIDTH" ensures leftCoord is always between 0 and WIDTH -1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # counts number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1                           # top-left is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1                           # top is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1                           # top-right is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1                           # left is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1                           # right is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1                           # below-left is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1                           # bottom is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1                           # bottom-right is alive

            # set cell based on Conways game of life rules
            if currentCells[x][y] == '#' and numNeighbors == 2 or numNeighbors == 3:
                # living cells with 2 or 3 neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # dead cells with 3 or more neighbors become alive
                nextCells[x][y] = '#'
            else:
                # everything else dies or stays dead
                nextCells[x][y] = ' '

time.sleep(1) # add a 1 second pause to reduce flickering
