import random


def createBoard(board):
    def createDiagonal(board):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(9):
            board[i][i] = nums[i]
        return board


    def checkRow(board, row, num):
        for i in range(9):
            if board[row][i] == num:
                return False
        return True

    def checkCol(board, col, num):
        for i in range(9):
            if board[i][col] == num:
                return False
        return True

    def checkBox(board, row, col, num):
        for i in range(3):
            for j in range(3):
                if board[i + row][j + col] == num:
                    return False
        return True


    def fillRemaining(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if checkRow(board, i, num) and checkCol(board, j, num) and checkBox(board, i - i % 3, j - j % 3, num):
                            board[i][j] = num
                            if fillRemaining(board):
                                return True
                            board[i][j] = 0
                    return False
        return True


    board = createDiagonal(board)
    if not fillRemaining(board):
        print("Failed to fill the board.")
    return board


if __name__ == "__main__":
    board = [[0 for _ in range(9)] for _ in range(9)]
    board = createBoard(board)
    for row in board:
        print(row)