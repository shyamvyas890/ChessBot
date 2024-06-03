from Player import Player
from DebuggingTools import pretty_print_board
from BoardState import BoardState
RIGHT_BOUND = 0x01_01_01_01_01_01_01_01
LEFT_BOUND = 0x80_80_80_80_80_80_80_80
UPPER_BOUND = 0xFF_00_00_00_00_00_00_00
LOWER_BOUND = 0x00_00_00_00_00_00_00_FF

def validateSouthwestMove(potentialLeftRightBishopMove, friendlyMask, opponentMask):
    if(potentialLeftRightBishopMove & friendlyMask) != 0:
        return 1 #invalid move, so discard and stop searching further = 1
    if(potentialLeftRightBishopMove & opponentMask) != 0:
        return 2 #valid move, but it takes an opponent piece, so stop searching further = 2
    if ((LEFT_BOUND & potentialLeftRightBishopMove) != 0) or ((LOWER_BOUND & potentialLeftRightBishopMove) != 0):
        return 3 #valid move, and it doesn't take an opponent piece, but it hits a boundary so stop searching further
    return 4 #valid move, and it doesn't take an opponent piece or hit a boundary
def validateSoutheastMove(potentialLeftRightBishopMove, friendlyMask, opponentMask):
    if(potentialLeftRightBishopMove & friendlyMask) != 0:
        return 1 #invalid move, so discard and stop searching further = 1
    if(potentialLeftRightBishopMove & opponentMask) != 0:
        return 2 #valid move, but it takes an opponent piece, so stop searching further = 2
    if ((RIGHT_BOUND & potentialLeftRightBishopMove) != 0) or ((LOWER_BOUND & potentialLeftRightBishopMove) != 0):
        return 3 #valid move, and it doesn't take an opponent piece, but it hits a boundary so stop searching further
    return 4 #valid move, and it doesn't take an opponent piece or hit a boundary
def validateNorthwestMove(potentialLeftRightBishopMove, friendlyMask, opponentMask):
    if(potentialLeftRightBishopMove & friendlyMask) != 0:
        return 1 #invalid move, so discard and stop searching further = 1
    if(potentialLeftRightBishopMove & opponentMask) != 0:
        return 2 #valid move, but it takes an opponent piece, so stop searching further = 2
    if ((LEFT_BOUND & potentialLeftRightBishopMove) != 0) or ((UPPER_BOUND & potentialLeftRightBishopMove) != 0):
        return 3 #valid move, and it doesn't take an opponent piece, but it hits a boundary so stop searching further
    return 4 #valid move, and it doesn't take an opponent piece or hit a boundary
def validateNortheastMove(potentialLeftRightBishopMove, friendlyMask, opponentMask):
    if(potentialLeftRightBishopMove & friendlyMask) != 0:
        return 1 #invalid move, so discard and stop searching further = 1
    if(potentialLeftRightBishopMove & opponentMask) != 0:
        return 2 #valid move, but it takes an opponent piece, so stop searching further = 2
    if ((RIGHT_BOUND & potentialLeftRightBishopMove) != 0) or ((UPPER_BOUND & potentialLeftRightBishopMove) != 0):
        return 3 #valid move, and it doesn't take an opponent piece, but it hits a boundary so stop searching further
    return 4 #valid move, and it doesn't take an opponent piece or hit a boundary

def generateBishopMoves(thePlayer: Player, theBitBoardsObject: BoardState):
    originalBishopBitboard = None
    if(thePlayer == Player.COMPUTER):
        originalBishopBitboard = theBitBoardsObject.computerBishops
    elif (thePlayer == Player.HUMAN):
        originalBishopBitboard = theBitBoardsObject.humanBishops
    individualBishopBitboards = []
    individualBoard = originalBishopBitboard & (~originalBishopBitboard + 1)
    individualBishopBitboards.append(individualBoard)
    originalBishopBitboard ^= individualBoard
    while (originalBishopBitboard != 0):
        individualBoard = originalBishopBitboard & (~originalBishopBitboard + 1)
        individualBishopBitboards.append(individualBoard)
        originalBishopBitboard ^= individualBoard

    finalLegalBishopMoves = []

    allOpponentPlayerPieces = None
    if(thePlayer == Player.COMPUTER):
        allOpponentPlayerPieces = theBitBoardsObject.humanKings | theBitBoardsObject.humanRooks | theBitBoardsObject.humanBishops | theBitBoardsObject.humanQueens | theBitBoardsObject.humanKnights | theBitBoardsObject.humanPawns
    elif(thePlayer == Player.HUMAN):
        allOpponentPlayerPieces = theBitBoardsObject.computerKings | theBitBoardsObject.computerRooks | theBitBoardsObject.computerBishops | theBitBoardsObject.computerQueens | theBitBoardsObject.computerKnights | theBitBoardsObject.computerPawns
    for individualBishop in individualBishopBitboards:
        allOtherCurrentPlayerPieces = None
        if(thePlayer == Player.COMPUTER):
            allOtherCurrentPlayerPieces = theBitBoardsObject.computerKings | theBitBoardsObject.computerRooks | theBitBoardsObject.computerQueens | theBitBoardsObject.computerKnights | theBitBoardsObject.computerPawns
        elif (thePlayer == Player.HUMAN):
            allOtherCurrentPlayerPieces = theBitBoardsObject.humanKings | theBitBoardsObject.humanRooks | theBitBoardsObject.humanQueens | theBitBoardsObject.humanKnights | theBitBoardsObject.humanPawns
        
        allOtherCurrentPlayerBishops = 0
        for potentialOtherBishop in individualBishopBitboards:
            if potentialOtherBishop != individualBishop:
                allOtherCurrentPlayerPieces |= potentialOtherBishop
                allOtherCurrentPlayerBishops |= potentialOtherBishop
        
        for index in range(4):
            if (index == 0 and ((individualBishop & LEFT_BOUND) != 0) or ((individualBishop & LOWER_BOUND) != 0)):
                continue
            if (index == 1 and ((individualBishop & RIGHT_BOUND) != 0) or ((individualBishop & LOWER_BOUND) != 0)):
                continue
            if (index == 2 and ((individualBishop & LEFT_BOUND) != 0) or ((individualBishop & UPPER_BOUND) != 0)):
                continue
            if (index == 3 and ((individualBishop & RIGHT_BOUND) != 0) or ((individualBishop & UPPER_BOUND) != 0)):
                continue
            
            potentialLeftRightBishopMove = None
            if (index == 0):
                potentialLeftRightBishopMove = individualBishop >> 7
            elif (index == 1):
                potentialLeftRightBishopMove = individualBishop >> 9
            elif (index == 2):
                potentialLeftRightBishopMove = individualBishop << 9
            elif (index == 3):
                potentialLeftRightBishopMove = individualBishop << 7
            while True:
                score = None
                if(index == 0):
                    score = validateSouthwestMove(potentialLeftRightBishopMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces)
                elif (index == 1):
                    score = validateSoutheastMove(potentialLeftRightBishopMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces)
                elif (index == 2):
                    score = validateNorthwestMove(potentialLeftRightBishopMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces)
                elif (index == 3):
                    score = validateNortheastMove(potentialLeftRightBishopMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces)
                if(score == 1):
                    break
                newBishopBitboard = allOtherCurrentPlayerBishops | potentialLeftRightBishopMove
                theBitBoardsObjectCopy = theBitBoardsObject.boardClone()
                if (score == 2):
                    if(thePlayer == Player.COMPUTER):
                        theBitBoardsObjectCopy.computerBishops = newBishopBitboard
                        if((theBitBoardsObjectCopy.humanKings & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.humanKings ^= potentialLeftRightBishopMove
                        elif((theBitBoardsObjectCopy.humanRooks & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.humanRooks ^= potentialLeftRightBishopMove
                        elif((theBitBoardsObjectCopy.humanBishops & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.humanBishops ^= potentialLeftRightBishopMove
                        elif((theBitBoardsObjectCopy.humanQueens & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.humanQueens ^= potentialLeftRightBishopMove
                        elif((theBitBoardsObjectCopy.humanKnights & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.humanKnights ^= potentialLeftRightBishopMove
                        elif((theBitBoardsObjectCopy.humanPawns & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.humanPawns ^= potentialLeftRightBishopMove
                    elif(thePlayer == Player.HUMAN):
                        theBitBoardsObjectCopy.humanBishops = newBishopBitboard
                        if((theBitBoardsObjectCopy.computerKings & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.computerKings ^= potentialLeftRightBishopMove
                        elif((theBitBoardsObjectCopy.computerRooks & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.computerRooks ^= potentialLeftRightBishopMove
                        elif((theBitBoardsObjectCopy.computerBishops & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.computerBishops ^= potentialLeftRightBishopMove
                        elif((theBitBoardsObjectCopy.computerQueens & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.computerQueens ^= potentialLeftRightBishopMove
                        elif((theBitBoardsObjectCopy.computerKnights & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.computerKnights ^= potentialLeftRightBishopMove
                        elif((theBitBoardsObjectCopy.computerPawns & potentialLeftRightBishopMove) != 0):
                            theBitBoardsObjectCopy.computerPawns ^= potentialLeftRightBishopMove
                    finalLegalBishopMoves.append(theBitBoardsObjectCopy)
                    break
                if(score == 3):
                    if(thePlayer == Player.COMPUTER):
                        theBitBoardsObjectCopy.computerBishops = newBishopBitboard
                    elif(thePlayer == Player.HUMAN):
                        theBitBoardsObjectCopy.humanBishops = newBishopBitboard
                    finalLegalBishopMoves.append(theBitBoardsObjectCopy)
                    break
                if (score == 4):
                    if(thePlayer == Player.COMPUTER):
                        theBitBoardsObjectCopy.computerBishops = newBishopBitboard
                    elif(thePlayer == Player.HUMAN):
                        theBitBoardsObjectCopy.humanBishops = newBishopBitboard
                    finalLegalBishopMoves.append(theBitBoardsObjectCopy)
                    if(index == 0):
                        potentialLeftRightBishopMove >>= 7
                    elif (index == 1):
                        potentialLeftRightBishopMove >>= 9
                    if(index == 2):
                        potentialLeftRightBishopMove <<= 9
                    elif (index == 3):
                        potentialLeftRightBishopMove <<= 7
    print(len(finalLegalBishopMoves))
    for potentialMove in finalLegalBishopMoves:
        print("Computer bishops")
        pretty_print_board(potentialMove.computerBishops)
        print("Humans Pawns")
        pretty_print_board(potentialMove.humanPawns)
                    


                            





    
