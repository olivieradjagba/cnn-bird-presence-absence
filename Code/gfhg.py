def count_victories(board):
    n = len(board)
    count1 = 0
    count2 = 0
    for i in range(n):
        row = len(set(board[i]))
        col = len(set(board[j][i] for j in range(n)))
        if row < 3:
            if row == 1:
                count1 += 1
            else:
                count2 += 1
            if col == 1:
                count1 += 1
            else:
                count2 += 1
        diag1 = len(set(board[j][j] for j in range(n)))
        diag2 = len(set(board[j][n-j-1] for j in range(n)))
    if diag1 == 1:
        count1 += 1
    elif diag1 == 1:
        count2 += 1
    if diag2 == 1:
        count1 += 1
    elif diag2 == 1:
        count2 += 1
        
    return count1, count2

# Input
board = [input() for _ in range(3)]
individuals, pairs = count_victories(board)

# Output
print(individuals)
print(pairs)