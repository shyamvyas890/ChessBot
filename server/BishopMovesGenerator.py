from ChessEnums import Player, Piece
from DebuggingTools import pretty_print_board
from BoardState import BoardState
from UtilityFunctions import splitPieceIntoIndividualBitboards, generateOpponentMask, generateFriendlyMasks, modifyBitboardToTakePiece
RIGHT_BOUND = 0x01_01_01_01_01_01_01_01
LEFT_BOUND = 0x80_80_80_80_80_80_80_80
UPPER_BOUND = 0xFF_00_00_00_00_00_00_00
LOWER_BOUND = 0x00_00_00_00_00_00_00_FF

boundaryBasedOnDirection = {
    1: (LEFT_BOUND, LOWER_BOUND),
    2: (RIGHT_BOUND, LOWER_BOUND),
    3: (LEFT_BOUND, UPPER_BOUND),
    4: (RIGHT_BOUND, UPPER_BOUND)
}

def validateMove(potentialLeftRightBishopMove, friendlyMask, opponentMask, direction: int):
    if(potentialLeftRightBishopMove & friendlyMask) != 0:
        return 1 #invalid move, so discard and stop searching further = 1
    if(potentialLeftRightBishopMove & opponentMask) != 0:
        return 2 #valid move, but it takes an opponent piece, so stop searching further = 2
    boundaries = boundaryBasedOnDirection[direction]
    if ((boundaries[0] & potentialLeftRightBishopMove) != 0) or ((boundaries[1] & potentialLeftRightBishopMove) != 0):
        return 3 #valid move, and it doesn't take an opponent piece, but it hits a boundary so stop searching further
    return 4 #valid move, and it doesn't take an opponent piece or hit a boundary

bishopInstanceVariableDictionary = {
    Player.COMPUTER: "_computerBishops",
    Player.HUMAN: "_humanBishops"
}

def generateBishopMoves(thePlayer: Player, theBitBoardsObject: BoardState):
    individualBishopBitboards = splitPieceIntoIndividualBitboards(bishopInstanceVariableDictionary[thePlayer], theBitBoardsObject)
    finalLegalBishopMoves = []
    allOpponentPlayerPieces = generateOpponentMask(thePlayer,theBitBoardsObject)
    for individualBishop in individualBishopBitboards:
        allOtherCurrentPlayerPieces, allOtherCurrentPlayerBishops = generateFriendlyMasks(thePlayer, bishopInstanceVariableDictionary[thePlayer], theBitBoardsObject, individualBishop)
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
                    score = validateMove(potentialLeftRightBishopMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, 1)
                elif (index == 1):
                    score = validateMove(potentialLeftRightBishopMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, 2)
                elif (index == 2):
                    score = validateMove(potentialLeftRightBishopMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, 3)
                elif (index == 3):
                    score = validateMove(potentialLeftRightBishopMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, 4)
                if(score == 1):
                    break
                newBishopBitboard = allOtherCurrentPlayerBishops | potentialLeftRightBishopMove
                theBitBoardsObjectCopy = theBitBoardsObject.boardClone()
                if (score == 2):
                    modifyBitboardToTakePiece(theBitBoardsObjectCopy,thePlayer, bishopInstanceVariableDictionary[thePlayer], newBishopBitboard, potentialLeftRightBishopMove)
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
