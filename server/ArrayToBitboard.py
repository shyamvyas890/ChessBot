from BoardState import BoardState

'''
Capital letters are computer pieces and lowercase letters are human pieces 
K: king
R: rook
B: bishop
Q: queen
N: knight
P: pawn
'''
def convert2DArrayToBitboards(the2dArray):
    (computerKings, computerRooks, computerBishops, computerQueens, computerKnights, computerPawns, humanKings, humanRooks, humanBishops, humanQueens, humanKnights, humanPawns) = (0b0,) * 12
    for i in range(len(the2dArray)):
        for j in range(len(the2dArray[i])):
            theIndexInBitboard = (i*8) + j
            indexForBitwiseOperations = 63- theIndexInBitboard
            if(the2dArray[i][j]== "K"):
                computerKings |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "R"):
                computerRooks |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "B"):
                computerBishops |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "Q"):
                computerQueens |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "N"):
                computerKnights |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "P"):
                computerPawns |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "k"):
                humanKings |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "r"):
                humanRooks |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "b"):
                humanBishops |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "q"):
                humanQueens |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "n"):
                humanKnights |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "p"):
                humanPawns |= (1 << indexForBitwiseOperations)
    return BoardState(computerKings, computerRooks, computerBishops, computerQueens, computerKnights, computerPawns, humanKings, humanRooks, humanBishops, humanQueens, humanKnights, humanPawns)