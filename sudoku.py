# Create the Sodoku grid
grid = [[3,2,0,1,6,0,8,0,9],
        [0,7,8,9,0,3,1,2,6],
        [6,0,0,8,0,0,4,5,3],
        [7,1,0,4,0,0,0,6,2],
        [5,4,0,0,0,0,0,0,7],
        [0,0,0,2,0,5,3,1,0],
        [0,5,9,7,4,0,2,0,8],
        [2,0,7,5,0,9,0,0,0],
        [8,6,4,0,0,0,0,9,5],]

# Create possibilities
possible = {}
for y in range(9):
    for x in range(9):
        possible[(y,x)] = [1,2,3,4,5,6,7,8,9]

# A function that returns the row it is in.
def check_row(y,x):
    return grid[y]

# A function that returns the column it is in.
def check_column(y,x):
    column = []
    for hops in range(9):
        column.append(grid[hops][x])
    return column

# A function that returns the square it is in.
#  ------------- 
# 1| 0 | 1 | 2 |
#  -------------
# 2| 3 | 4 | 5 |
#  -------------
# 3| 6 | 7 | 8 |
#  -------------
#    1   2   3
def check_square(they,thex):

    square0 = []
    square1 = []
    square2 = []
    square3 = []
    square4 = []
    square5 = []
    square6 = []
    square7 = []
    square8 = []

    for y in range(3):
        for x in range(3):
             square0.append([y,x])

    for y in range(3):
        for x in range(3,6):
            square1.append([y,x])

    for y in range(3):
        for x in range(6,9):
            square2.append([y,x])

    for y in range(3,6):
        for x in range(3):
            square3.append([y,x])

    for y in range(3,6):
        for x in range(3,6):
            square4.append([y,x])

    for y in range(3,6):
        for x in range(6,9):
            square5.append([y,x])

    for y in range(6,9):
        for x in range(3):
            square6.append([y,x])

    for y in range(6,9):
        for x in range(3,6):
            square7.append([y,x])

    for y in range(6,9):
        for x in range(6,9):
            square8.append([y,x])

    tests = [square0,
             square1,
             square2,
             square3,
             square4,
             square5,
             square6,
             square7,
             square8]

    square_list = []

    def list_of_grid(result):
        for cood in result:
            [they,thex] = cood
            square_list.append(grid[they][thex])
            

    # Check which square it of and print the list of grid
    for test in tests:
        if [they,thex] in test:
            list_of_grid(test)

    return square_list


# Function that eliminates row possibilities
def elim_row():

    get_rid = []
    # For the ys
    for y in range(9):
        # For the xs
        for x in range(9):
            
            # Iterates through the current row
            for digit in check_row(y,x):
                # If that digit is not blank...
                if digit != 0:
                    try:
                        # Add it to a list called remove_this
                        get_rid.append(digit)
                    except ValueError:
                        pass

    
        for element in get_rid:
            for x in range(9):
                try:
                    if grid[y][x] == 0:
                        possible[(y,x)].remove(element)
                    else:
                        possible[(y,x)] = []
                except ValueError:
                    pass

# Funciton that eliminates column possibilites
def elim_column():
    get_rid = []
    for x in range(9):
        for y in range(9):
            
            for digit in check_column(y,x):
                if digit != 0:
                    try:
                        get_rid.append(digit)
                    except ValueError:
                        pass

        for element in get_rid:
            for y in range(9):
                try:
                    if grid[y][x] == 0:
                        possible[(y,x)].remove(element)
                    else:
                        possible[(y,x)] = []
                except ValueError:
                    pass

# Function that eliminates square possibilites
def elim_square():
    pass

# Check if done:
def done():
    empty = 0
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                empty += 1
    if empty == 0:
        return True
    else:
        return False


# print grid
if __name__ == "__main__uaua":
    # Go through each row, column and square and delete possibilites
    while not done():
        
        raw_input("")
        
        for cood in possible.keys():
            (y, x) = cood

            elim_row(y,x)
            elim_column(y,x)

            # Check if len of possible == 1
            if len(possible[cood]) == 1:
                grid[y][x] = possible[cood][0]

        print possible[(0,2)]
        for rows in grid:
            print rows

    
elim_row()
elim_column()

for y in range(9):
    for x in range(9):
        if len(possible[(y,x)]) == 1:
            grid[y][x] = possible[(y,x)][0]

for rows in grid:
    print rows
