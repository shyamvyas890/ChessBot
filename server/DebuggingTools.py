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
