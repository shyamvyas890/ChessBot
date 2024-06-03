from Player import Player
from DebuggingTools import pretty_print_board
from BoardState import BoardState



def isUpDownRookMoveValid (newIndividualRookBitboard, leftScreenBound, friendlyMask, opponentMask):
    if((newIndividualRookBitboard > leftScreenBound) or (newIndividualRookBitboard == 0)):
        return 1 #invalid move because off the board, so move will be discarded, and further search in this direction will be stopped
    if((newIndividualRookBitboard & friendlyMask) != 0):
        return 2 # invalid move because you hit a friendly piece searching in this direction, so move will be discarded, and further search in this direction will be stopped
    if((newIndividualRookBitboard & opponentMask) != 0):
        return 3 #valid move and this move takes an opponents piece, so that will be noted and further search in this direction will stop
    return 4 # valid move and this move didn't get any of your opponents pieces either
def isLeftRightRookMoveValid(newIndividualRookBitboard, friendlyMask, opponentMask, directionIsLeft): #directionIsLeft: true means left and false means right
    rightBound = 0x01_01_01_01_01_01_01_01
    leftBound = 0x80_80_80_80_80_80_80_80
    if(newIndividualRookBitboard & friendlyMask) != 0:
            return 1 #invalid move, so discard and stop searching further = 1
    if(newIndividualRookBitboard & opponentMask) != 0:
        return 2 #valid move, but it takes an opponent piece, so stop searching further = 2
    if directionIsLeft and (leftBound & newIndividualRookBitboard) != 0:
        return 3 #valid move, and it doesn't take an opponent piece, but it hits a boundary so stop searching further
    if (not directionIsLeft) and (rightBound & newIndividualRookBitboard) != 0:
        return 3 #valid move, and it doesn't take an opponent piece, but it hits a boundary so stop searching further
    return 4 #valid move, and it doesn't take an opponent piece or hit a boundary

        
    
    

def generateRookMoves(thePlayer: Player, theBitBoardsObject: BoardState):
    originalRookBitboard = None
    if(thePlayer == Player.COMPUTER):
        originalRookBitboard = theBitBoardsObject.computerRooks
    elif (thePlayer == Player.HUMAN):
        originalRookBitboard = theBitBoardsObject.humanRooks
    individualRookBitboards = []
    individualBoard = originalRookBitboard & (~originalRookBitboard + 1)
    individualRookBitboards.append(individualBoard)
    originalRookBitboard ^= individualBoard
    while(originalRookBitboard != 0):
        individualBoard = originalRookBitboard & (~originalRookBitboard + 1)
        individualRookBitboards.append(individualBoard)
        originalRookBitboard ^= individualBoard

    isTheRookOffLeftScreen = 0x80_00_00_00_00_00_00_00
    isTheRookOffRightScreen = 0

    rightBound = 0x01_01_01_01_01_01_01_01
    leftBound = 0x80_80_80_80_80_80_80_80

    finalLegalRookMoves = []

    allOpponentPlayerPieces = None
    if(thePlayer == Player.COMPUTER):
        allOpponentPlayerPieces = theBitBoardsObject.humanKings | theBitBoardsObject.humanRooks | theBitBoardsObject.humanBishops | theBitBoardsObject.humanQueens | theBitBoardsObject.humanKnights | theBitBoardsObject.humanPawns
    elif(thePlayer == Player.HUMAN):
        allOpponentPlayerPieces = theBitBoardsObject.computerKings | theBitBoardsObject.computerRooks | theBitBoardsObject.computerBishops | theBitBoardsObject.computerQueens | theBitBoardsObject.computerKnights | theBitBoardsObject.computerPawns

    for individualRook in individualRookBitboards:
        #other friendly pieces mask
        allOtherCurrentPlayerPieces = None
        if(thePlayer == Player.COMPUTER):
            allOtherCurrentPlayerPieces = theBitBoardsObject.computerKings | theBitBoardsObject.computerBishops | theBitBoardsObject.computerQueens | theBitBoardsObject.computerKnights | theBitBoardsObject.computerPawns
        elif (thePlayer == Player.HUMAN):
            allOtherCurrentPlayerPieces = theBitBoardsObject.humanKings | theBitBoardsObject.humanBishops | theBitBoardsObject.humanQueens | theBitBoardsObject.humanKnights | theBitBoardsObject.humanPawns
        
        allOtherCurrentPlayerRooks = 0
        for potentialOtherRook in individualRookBitboards:
            if potentialOtherRook != individualRook:
                allOtherCurrentPlayerPieces |= potentialOtherRook
                allOtherCurrentPlayerRooks |= potentialOtherRook
        

        #up and down
        for index in range(2):
            potentialUpDownRookMove = None
            if (index == 0):
                
                potentialUpDownRookMove = individualRook << 8
                
            elif (index == 1):
                potentialUpDownRookMove = individualRook >> 8
            while True:
                score = isUpDownRookMoveValid(potentialUpDownRookMove,isTheRookOffLeftScreen,allOtherCurrentPlayerPieces, allOpponentPlayerPieces)
                if(score == 1 or score == 2):
                    break
                newRookBitboard = allOtherCurrentPlayerRooks | potentialUpDownRookMove
                
                theBitBoardsObjectCopy = theBitBoardsObject.boardClone()
                if(score == 3):
                    if(thePlayer == Player.COMPUTER):
                        theBitBoardsObjectCopy.computerRooks = newRookBitboard
                        if((theBitBoardsObjectCopy.humanKings & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.humanKings ^= potentialUpDownRookMove
                        elif((theBitBoardsObjectCopy.humanRooks & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.humanRooks ^= potentialUpDownRookMove
                        elif((theBitBoardsObjectCopy.humanBishops & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.humanBishops ^= potentialUpDownRookMove
                        elif((theBitBoardsObjectCopy.humanQueens & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.humanQueens ^= potentialUpDownRookMove
                        elif((theBitBoardsObjectCopy.humanKnights & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.humanKnights ^= potentialUpDownRookMove
                        elif((theBitBoardsObjectCopy.humanPawns & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.humanPawns ^= potentialUpDownRookMove
                        
                    elif(thePlayer == Player.HUMAN):
                        theBitBoardsObjectCopy.humanRooks = newRookBitboard
                        if((theBitBoardsObjectCopy.computerKings & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.computerKings ^= potentialUpDownRookMove
                        elif((theBitBoardsObjectCopy.computerRooks & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.computerRooks ^= potentialUpDownRookMove
                        elif((theBitBoardsObjectCopy.computerBishops & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.computerBishops ^= potentialUpDownRookMove
                        elif((theBitBoardsObjectCopy.computerQueens & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.computerQueens ^= potentialUpDownRookMove
                        elif((theBitBoardsObjectCopy.computerKnights & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.computerKnights ^= potentialUpDownRookMove
                        elif((theBitBoardsObjectCopy.computerPawns & potentialUpDownRookMove) != 0):
                            theBitBoardsObjectCopy.computerPawns ^= potentialUpDownRookMove
                    finalLegalRookMoves.append(theBitBoardsObjectCopy)

                    break
                if(score == 4):
                    if(thePlayer == Player.COMPUTER):
                        
                        theBitBoardsObjectCopy.computerRooks = newRookBitboard
                    elif(thePlayer == Player.HUMAN):
                        theBitBoardsObjectCopy.humanRooks = newRookBitboard
                    
                    finalLegalRookMoves.append(theBitBoardsObjectCopy)
                    if(index == 0):
                        potentialUpDownRookMove <<= 8
                    elif(index == 1):
                        potentialUpDownRookMove >>= 8
        for index in range(2):
            if(index == 0 and ((individualRook & leftBound) != 0)): # check if they are already on the boundary and if so, there's no possible moves
                continue
            if(index == 1 and ((individualRook & rightBound) != 0)):
                continue
            potentialLeftRightRookMove = None
            if(index == 0):
                potentialLeftRightRookMove = individualRook << 1
            elif (index == 1):
                potentialLeftRightRookMove = individualRook >> 1
            while True:
                score = None
                if(index == 0):
                    score = isLeftRightRookMoveValid(potentialLeftRightRookMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, True)
                elif (index ==1):
                    score = isLeftRightRookMoveValid(potentialLeftRightRookMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, False)
                if(score == 1):
                    break
                newRookBitboard = allOtherCurrentPlayerRooks | potentialLeftRightRookMove
                theBitBoardsObjectCopy = theBitBoardsObject.boardClone()
                if(score == 2):
                    if(thePlayer == Player.COMPUTER):
                        theBitBoardsObjectCopy.computerRooks = newRookBitboard
                        if((theBitBoardsObjectCopy.humanKings & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.humanKings ^= potentialLeftRightRookMove
                        elif((theBitBoardsObjectCopy.humanRooks & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.humanRooks ^= potentialLeftRightRookMove
                        elif((theBitBoardsObjectCopy.humanBishops & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.humanBishops ^= potentialLeftRightRookMove
                        elif((theBitBoardsObjectCopy.humanQueens & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.humanQueens ^= potentialLeftRightRookMove
                        elif((theBitBoardsObjectCopy.humanKnights & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.humanKnights ^= potentialLeftRightRookMove
                        elif((theBitBoardsObjectCopy.humanPawns & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.humanPawns ^= potentialLeftRightRookMove
                        
                        
                    elif(thePlayer == Player.HUMAN):
                        theBitBoardsObjectCopy.humanRooks = newRookBitboard
                        if((theBitBoardsObjectCopy.computerKings & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.computerKings ^= potentialLeftRightRookMove
                        elif((theBitBoardsObjectCopy.computerRooks & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.computerRooks ^= potentialLeftRightRookMove
                        elif((theBitBoardsObjectCopy.computerBishops & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.computerBishops ^= potentialLeftRightRookMove
                        elif((theBitBoardsObjectCopy.computerQueens & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.computerQueens ^= potentialLeftRightRookMove
                        elif((theBitBoardsObjectCopy.computerKnights & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.computerKnights ^= potentialLeftRightRookMove
                        elif((theBitBoardsObjectCopy.computerPawns & potentialLeftRightRookMove) != 0):
                            theBitBoardsObjectCopy.computerPawns ^= potentialLeftRightRookMove
                    finalLegalRookMoves.append(theBitBoardsObjectCopy)
                    break
                if(score == 3):
                    if(thePlayer == Player.COMPUTER):
                        theBitBoardsObjectCopy.computerRooks = newRookBitboard
                    elif(thePlayer == Player.HUMAN):
                        theBitBoardsObjectCopy.humanRooks = newRookBitboard
                    
                    finalLegalRookMoves.append(theBitBoardsObjectCopy)
                    break
                if(score == 4):
                    if(thePlayer == Player.COMPUTER):
                        theBitBoardsObjectCopy.computerRooks = newRookBitboard
                    elif(thePlayer == Player.HUMAN):
                        theBitBoardsObjectCopy.humanRooks = newRookBitboard
                    
                    finalLegalRookMoves.append(theBitBoardsObjectCopy)
                    if(index == 0):
                        potentialLeftRightRookMove <<= 1
                    elif(index == 1):
                        potentialLeftRightRookMove >>= 1

    print(len(finalLegalRookMoves))
    for potentialMove in finalLegalRookMoves:
        print("Computer rooks")
        pretty_print_board(potentialMove.computerRooks)
        print("Humans Pawns")
        pretty_print_board(potentialMove.humanPawns)
