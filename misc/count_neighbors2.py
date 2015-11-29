def checkio(grid, row, col):
    count = 0
    min_row = 0
    min_col = 0
    max_row = 4
    max_col = 4
    if row == min_row:
        for i in range(min_row, row + 2):
            if col > min_col and col < max_col:
                for j in range(col - 1, col + 2):
                    count += grid[i][j]
            if col == min_col:
                for j in range(min_col, col + 2):
                    count += grid[i][j]
            if col == max_col:
                for j in range(col - 1, max_col + 1):
                    count += grid[i][j]
    if row == max_row:
        for i in range(row - 1, max_row + 1):
            if col > min_col and col < max_col:
                for j in range(col - 1, col + 2):
                    count += grid[i][j]
            if col == min_col:
                for j in range(min_col, col + 2):
                    count += grid[i][j]
            if col == max_col:
                for j in range(col - 1, max_col + 1):
                    count += grid[i][j]
    if row > min_row and row < max_row:
        for i in range(row - 1, row + 2):
            if col > min_col and col < max_col:
                for j in range(col - 1, col + 2):
                    count += grid[i][j]
            if col == min_col:
                for j in range(min_col, col + 2):
                    count += grid[i][j]
            if col == max_col:
                for j in range(col - 1, max_col + 1):
                    count += grid[i][j]
