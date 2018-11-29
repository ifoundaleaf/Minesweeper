# minesweeper
# Alif Islam
# Wednesday, November 28, 2018

import random
import math

GRIDSIZE = 10
MINECHANCE = 10

# function    :  initMines
# input       :  none
# output      :  grid
# description :  create a grid of mines, where each grid has a 1 in MINECHANCE
#                probability of being a mine, where a mine = x
def initMines():
    grid = []
    mine = random.randint(0, MINECHANCE)

    for row in range(GRIDSIZE):
        grid.append([])
        for col in range(GRIDSIZE):
            grid[row].append(' ')
            if mine == 0:
                grid[row][col] = 'x'
            mine = random.randint(0, MINECHANCE)

    return grid

# function    :  initBoard
# input       :  none
# output      :  grid
# description :  create a grid of #
def initBoard():
    grid = []

    for row in range(GRIDSIZE):
        grid.append([])
        for col in range(GRIDSIZE):
            grid[row].append('#')

    return grid

# function    :  displayBoard
# input       :  grid
# output      :  none
# description :  display a given grid
def displayBoard(grid):
    print('  |', end = "")

    # to print the column labels
    for i in range(GRIDSIZE):
        print(i, end = "")

    print('\n', '-' * (GRIDSIZE + 2))

    for row in range(GRIDSIZE):
        # to print the row labels
        print(row, '|', end = "")
        for col in range(GRIDSIZE):
            # to print the grid
            print(grid[row][col], end = "")
        print('\n')

# function    :  countHiddenCells
# input       :  grid
# output      :  numCells
# description :  count the number of hidden cells in a grid
def countHiddenCells(grid):
    # calculate number of cells that are still hidden
    numCells = GRIDSIZE * GRIDSIZE

    for cell in grid:
        if cell == '#':
            numCells -= 1

    return numCells

# function    :  countMines
# input       :  grid
# output      :  numCells
# description :  count the number of mines cells in a grid
def countMines(grid):
    numCells = 0

    for cell in grid:
        if cell == 'x':
            numCells += 1

    return numCells

def isMineAt(grid, row, col):
    if (row < GRIDSIZE and col < GRIDSIZE):
        if grid[row][col] == 'x':
            return True
        else:
            return False
    else:
        print("invalid input, you grub")

def countMinesAround(grid, row, col):
    numMines = 0

    if (grid[row - 1][col - 1] == 'x'):
        numMines += 1

    if (grid[row - 1][col] == 'x'):
        numMines += 1

    if (grid[row - 1][col + 1] == 'x'):
        numMines += 1

    if (grid[row][col - 1] == 'x'):
        numMines += 1

    if (grid[row][col + 1] == 'x'):
        numMines += 1

    if (grid[row + 1][col - 1] == 'x'):
        numMines += 1

    if (grid[row + 1][col] == 'x'):
        numMines += 1

    if (grid[row + 1][col + 1] == 'x'):
        numMines += 1

    return numMines

def validateInput(input):
    if input[0] < 0 or input[0] > (GRIDSIZE - 1):
        return False
    elif input[1] != ',':
        return False
    elif input[2] < 0 or input[2] > (GRIDSIZE - 1):
        return False
    else:
        return True

def play():
    print('Please enter a location x,y: ')
    move = input('> ')

    while (validateInput(move) != True):
        print('Invalid input.')
        print('Please enter a location x,y: ')
        move = input('> ')

def main():
    win = False
    mine = initMines()
    board = initBoard()

    displayBoard(mine)
    displayBoard(board)

    while(win != True):
        play()

main()
