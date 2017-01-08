# Program for playing the game of Life
from ADT.life import LifeGrid

# Define the initial configuration of live cells
INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]

# Set the size of the grid
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Indicate the number of the generation
NUM_GENS = 8

def main():
    # Construct the game and configure it
    grid = LifeGrid(GRID_HEIGHT, GRID_WIDTH)
    grid.configure(INIT_CONFIG)

    #Play the Game:
    print "prime generation"
    grid.draw()
    for i in range(NUM_GENS):
        evolve(grid)
        print "%d generation" % (i + 1)
        grid.draw()

# Generates the next generation of organisms
def evolve(grid):
    # List for storing the live cells of next generation
    liveCell = list()

    # Iterate over the elements of the grid
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            # Determine the number of the ive neighbors for this cell
            neighbors = grid.numLiveNeighbors(i, j)
            if (neighbors == 2 and grid.isLiveCell(i, j) or (neighbors == 3)):
                liveCell.append((i, j))
    grid.configure(liveCell)

main()