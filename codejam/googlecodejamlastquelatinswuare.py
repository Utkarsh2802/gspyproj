from itertools import combinations_with_replacement

###################################################################



# A Utility Function to print the Grid
def print_grid(arr,gridsize):
    for i in range(gridsize):
        for j in range(gridsize):
            print(arr[i][j],end=" ")
        print()

    # Function to Find the entry in the Grid that is still not used


# Searches the grid to find an entry that is still unassigned. If
# found, the reference parameters row, col will be set the location
# that is unassigned, and true is returned. If no unassigned entries
# remain, false is returned.
# 'l' is a list variable that has been passed from the solve_sudoku function
# to keep track of incrementation of Rows and Columns
def find_empty_location(arr, l,gridsize):
    for row in range(gridsize):
        for col in range(gridsize):
            if (arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


# Returns a boolean which indicates whether any assigned entry
# in the specified row matches the given number.
def used_in_row(arr, row, num,gridsize):
    for i in range(gridsize):
        if (arr[row][i] == num):
            return True
    return False


# Returns a boolean which indicates whether any assigned entry
# in the specified column matches the given number.
def used_in_col(arr, col, num,gridsize):
    for i in range(gridsize):
        if (arr[i][col] == num):
            return True
    return False


# Returns a boolean which indicates whether any assigned entry
# within the specified 3x3 box matches the given number


# Checks whether it will be legal to assign num to the given row,col
# Returns a boolean which indicates whether it will be legal to assign
# num to the given row,col location.
def check_location_is_safe(arr, row, col, num,gridsize):
    # Check if 'num' is not already placed in current row,
    # current column and current 3x3 box
    return not used_in_row(arr, row, num,gridsize) and not used_in_col(arr, col, num,gridsize)


# Takes a partially filled-in grid and attempts to assign values to
# all unassigned locations in such a way to meet the requirements
# for Sudoku solution (non-duplication across rows, columns, and boxes)
def solve_sudoku(arr,gridsize):
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function
    l = [0, 0]

    # If there is no unassigned location, we are done
    if (not find_empty_location(arr, l,gridsize)):
        return True

    # Assigning list values to row and col that we got from the above Function
    row = l[0]
    col = l[1]

    # consider digits 1 to 9
    for num in range(1, gridsize+1):

        # if looks promising
        if (check_location_is_safe(arr, row, col, num,gridsize)):

            # make tentative assignment
            arr[row][col] = num

            # return, if success, ya!
            if (solve_sudoku(arr,gridsize)):
                return True

            # failure, unmake & try again
            arr[row][col] = 0

    # this triggers backtracking
    return False
#STARTTTTTTTTTTTTTTTTTTT
t=int(input())
for ___ in range(t):
    gridsize,required_sum=list(map(int,input().split()))
    sizelist=[]
    for ____ in range(gridsize):
        sizelist.append(____+1)
    l = list(combinations_with_replacement(sizelist, gridsize))
    finaltrace = []
    for i in l:
        summ = 0
        for j in i:
            summ += j
        if summ == required_sum:
            finaltrace.append(i)
    # creating a 2D array for the grid
    answer=""
    answer+="Case #"
    answer+=str(___+1)
    answer+=":"
    grid=[]
    grid = [[0 for x in range(gridsize)] for y in range(gridsize)]
    cnt=0
    for i in range(len(finaltrace)):
        for j in range(len(finaltrace[i])):
            grid[j][j]=finaltrace[i][j]
        # if success print the grid
        if solve_sudoku(grid,gridsize):
            print(answer,"POSSIBLE")
            print_grid(grid,gridsize)
            break
        else:
            cnt+=1
    if cnt>=len(finaltrace):
        print(answer,"IMPOSSIBLE")