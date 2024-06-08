def pretty_print_board(bitboard):
    board = [bit for bit in format(bitboard, '064b')]
    print("---------------------------------")
    if(len(board) == 64):
        count = 0    
        while(count<64):
            row = "| "
            for i in range(8):
                row += f"{board[count]} | "
                count=count+1
            print(row)
            print("---------------------------------")
    elif (len(board) > 64):
        count = len(board)-64
        while(count<64):
            row = "| "
            for i in range(8):
                row += f"{board[count]} | "
                count=count+1
            print(row)
            print("---------------------------------")
def board_to_2D_array(board):
    instanceVariableDictionary = {
        "_computerKings": "K",
        "_computerRooks": "R",
        "_computerBishops": "B",
        "_computerQueens": "Q",
        "_computerKnights": "N",
        "_computerPawns": "P",
        "_humanKings": "k",
        "_humanRooks": "r",
        "_humanBishops": "b",
        "_humanQueens": "q",
        "_humanKnights": "n",
        "_humanPawns": "p"
    }
    readableBoard = [[' ' for _ in range(8)] for _ in range(8)]

    for key in instanceVariableDictionary:
        bitboard = getattr(board,key)
        individualBitsInBitboard = [bit for bit in format(bitboard, '064b')]
        if(len(individualBitsInBitboard) == 64):
            for i in range(64):
                row = i // 8
                column = i % 8
                if(individualBitsInBitboard[i] == "1"):
                    readableBoard[row][column] = instanceVariableDictionary[key]
        else:
            offset = len(individualBitsInBitboard) - 64
            for i in range(64):
                row = i // 8
                column = i % 8
                if(individualBitsInBitboard[i + offset] == "1"):
                    readableBoard[row][column] = instanceVariableDictionary[key]
    print("---------------------------------")
    for i in range(8):
        row = "| "
        for j in range(8):
            row += f"{readableBoard[i][j]} | "
        print(row)
        print("---------------------------------")
    




    
    
    

            







