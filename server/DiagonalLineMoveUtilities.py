from ChessEnums import Player
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

def validateMove(potentialLeftRightPieceMove, friendlyMask, opponentMask, direction: int):
    if(potentialLeftRightPieceMove & friendlyMask) != 0:
        return 1 #invalid move, so discard and stop searching further = 1
    if(potentialLeftRightPieceMove & opponentMask) != 0:
        return 2 #valid move, but it takes an opponent piece, so stop searching further = 2
    boundaries = boundaryBasedOnDirection[direction]
    if ((boundaries[0] & potentialLeftRightPieceMove) != 0) or ((boundaries[1] & potentialLeftRightPieceMove) != 0):
        return 3 #valid move, and it doesn't take an opponent piece, but it hits a boundary so stop searching further
    return 4 #valid move, and it doesn't take an opponent piece or hit a boundary

def generateDiagonalPieceMoves(thePlayer: Player, theBitBoardsObject: BoardState, pieceInstanceVariable):
    individualPieceBitboards = splitPieceIntoIndividualBitboards(pieceInstanceVariable, theBitBoardsObject)
    finalLegalPieceMoves = []
    allOpponentPlayerPieces = generateOpponentMask(thePlayer,theBitBoardsObject)
    for individualPiece in individualPieceBitboards:
        allOtherCurrentPlayerPieces, allOtherCurrentPlayerPiecesOfSameType = generateFriendlyMasks(thePlayer, pieceInstanceVariable, theBitBoardsObject, individualPiece)
        for index in range(4):
            if (index == 0 and ((individualPiece & LEFT_BOUND) != 0) or ((individualPiece & LOWER_BOUND) != 0)):
                continue
            if (index == 1 and ((individualPiece & RIGHT_BOUND) != 0) or ((individualPiece & LOWER_BOUND) != 0)):
                continue
            if (index == 2 and ((individualPiece & LEFT_BOUND) != 0) or ((individualPiece & UPPER_BOUND) != 0)):
                continue
            if (index == 3 and ((individualPiece & RIGHT_BOUND) != 0) or ((individualPiece & UPPER_BOUND) != 0)):
                continue
            
            potentialLeftRightPieceMove = None
            if (index == 0):
                potentialLeftRightPieceMove = individualPiece >> 7
            elif (index == 1):
                potentialLeftRightPieceMove = individualPiece >> 9
            elif (index == 2):
                potentialLeftRightPieceMove = individualPiece << 9
            elif (index == 3):
                potentialLeftRightPieceMove = individualPiece << 7
            while True:
                score = None
                if(index == 0):
                    score = validateMove(potentialLeftRightPieceMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, 1)
                elif (index == 1):
                    score = validateMove(potentialLeftRightPieceMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, 2)
                elif (index == 2):
                    score = validateMove(potentialLeftRightPieceMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, 3)
                elif (index == 3):
                    score = validateMove(potentialLeftRightPieceMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, 4)
                if(score == 1):
                    break
                newPieceBitboard = allOtherCurrentPlayerPiecesOfSameType | potentialLeftRightPieceMove
                theBitBoardsObjectCopy = theBitBoardsObject.boardClone()
                if (score == 2):
                    modifyBitboardToTakePiece(theBitBoardsObjectCopy,thePlayer, pieceInstanceVariable, newPieceBitboard, potentialLeftRightPieceMove)
                    finalLegalPieceMoves.append(theBitBoardsObjectCopy)
                    break
                if(score == 3):
                    setattr(theBitBoardsObjectCopy, pieceInstanceVariable, newPieceBitboard)
                    finalLegalPieceMoves.append(theBitBoardsObjectCopy)
                    break
                if (score == 4):
                    setattr(theBitBoardsObjectCopy, pieceInstanceVariable, newPieceBitboard)
                    finalLegalPieceMoves.append(theBitBoardsObjectCopy)
                    if(index == 0):
                        potentialLeftRightPieceMove >>= 7
                    elif (index == 1):
                        potentialLeftRightPieceMove >>= 9
                    if(index == 2):
                        potentialLeftRightPieceMove <<= 9
                    elif (index == 3):
                        potentialLeftRightPieceMove <<= 7
    return finalLegalPieceMoves
