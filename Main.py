board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

game_over = False

def PrintBoard(pBoard):
    for row in pBoard:
        for col in row:
            print(str(col), end=' ')
        print()

def EnterMove(pBoard, pPlayer, pPosition):
    row = pPosition // 3
    col = pPosition % 3
    pBoard[row][col] = pPlayer
    PrintBoard(pBoard)

def CheckWin(pBoard):
    # Check vertical
    for row in pBoard:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    #Check horizontal
    for col in range(3):
        if pBoard[0][col] == pBoard[1][col] == pBoard[2][col] != " ":
            return pBoard[0][col]

    # Diagonalen prüfen
    if pBoard[0][0] == pBoard[1][1] == pBoard[2][2] != " ":
        return pBoard[0][0]
    if pBoard[0][2] == pBoard[1][1] == pBoard[2][0] != " ":
        return pBoard[0][2]

    return None  # kein Gewinner

def EnterPlayerMove():
    position = int(input("Enter your move: "))
    position -= 1
    EnterMove(board, "X", position)


def main():
    global game_over
    PrintBoard(board)
    while not game_over:
        EnterPlayerMove()
        if(CheckWin(board)!=None):
            game_over = True

main()
