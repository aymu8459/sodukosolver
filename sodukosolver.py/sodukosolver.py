board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(b):
    find = find_empty(b)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if rule_out(b, i, (row, col)):
            b[row][col] = i

            if solve(b):
                return True
            
            b[row][col] = 0
    
    return False

def rule_out(b, num, pos):
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i: 
            # if the number inputted is equal to an i'th indexed number in the row but the column index is not equal to i,
            # then that means that there is another entry in that row that is the same as the inputted number, 
            # it doesn't pass the soduko test
            return False

    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

     # determining quadrant(x,y) of the soduko table
    quadrant_x = pos[1] // 3
    quadrant_y = pos[0] // 3
            # by using integer division, able to use in for loop to determine range of quadrant where the pos is in
    for i in range(quadrant_y * 3, quadrant_y *3 + 3):
        for j in range(quadrant_x * 3, quadrant_x * 3 + 3):
            if b[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")

def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i,j)

    return None


print_board(board)
solve(board)
print('\n')
print_board(board)