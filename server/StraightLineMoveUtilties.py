from ChessEnums import Player
from UtilityFunctions import splitPieceIntoIndividualBitboards, generateOpponentMask, generateFriendlyMasks, modifyBitboardToTakePiece
IS_THE_PIECE_OFF_LEFT_SCREEN = 0x80_00_00_00_00_00_00_00
IS_THE_PIECE_OFF_RIGHT_SCREEN = 0
RIGHT_BOUND = 0x01_01_01_01_01_01_01_01
LEFT_BOUND = 0x80_80_80_80_80_80_80_80
def isUpDownPieceMoveValid (newIndividualPieceBitboard, friendlyMask, opponentMask):
    if((newIndividualPieceBitboard > IS_THE_PIECE_OFF_LEFT_SCREEN) or (newIndividualPieceBitboard == 0)):
        return 1 #invalid move because off the board, so move will be discarded, and further search in this direction will be stopped
    if((newIndividualPieceBitboard & friendlyMask) != 0):
        return 2 # invalid move because you hit a friendly piece searching in this direction, so move will be discarded, and further search in this direction will be stopped
    if((newIndividualPieceBitboard & opponentMask) != 0):
        return 3 #valid move and this move takes an opponents piece, so that will be noted and further search in this direction will stop
    return 4 # valid move and this move didn't get any of your opponents pieces either
def isLeftRightPieceMoveValid(newIndividualPieceBitboard, friendlyMask, opponentMask, directionIsLeft): #directionIsLeft: true means left and false means right
    if(newIndividualPieceBitboard & friendlyMask) != 0:
            return 1 #invalid move, so discard and stop searching further = 1
    if(newIndividualPieceBitboard & opponentMask) != 0:
        return 2 #valid move, but it takes an opponent piece, so stop searching further = 2
    if directionIsLeft and (LEFT_BOUND & newIndividualPieceBitboard) != 0:
        return 3 #valid move, and it doesn't take an opponent piece, but it hits a boundary so stop searching further
    if (not directionIsLeft) and (RIGHT_BOUND & newIndividualPieceBitboard) != 0:
        return 3 #valid move, and it doesn't take an opponent piece, but it hits a boundary so stop searching further
    return 4 #valid move, and it doesn't take an opponent piece or hit a boundary
queenInstanceVariableDictionary = {
    Player.COMPUTER: "_computerQueens",
    Player.HUMAN: "_humanQueens"
}
def generateStraightLinePieceMoves(thePlayer: Player, theBitBoardsObject, pieceInstanceVariable):
    individualPieceBitboards = splitPieceIntoIndividualBitboards(pieceInstanceVariable, theBitBoardsObject)
    finalLegalPieceMoves = []
    allOpponentPlayerPieces = generateOpponentMask(thePlayer,theBitBoardsObject)
    for individualPiece in individualPieceBitboards:
        #other friendly pieces mask
        allOtherCurrentPlayerPieces, allOtherCurrentPlayerPiecesOfSameType = generateFriendlyMasks(thePlayer, pieceInstanceVariable, theBitBoardsObject, individualPiece)
        #up and down
        for index in range(2):
            potentialUpDownPieceMove = None
            if (index == 0):
                potentialUpDownPieceMove = individualPiece << 8
            elif (index == 1):
                potentialUpDownPieceMove = individualPiece >> 8
            while True:
                score = isUpDownPieceMoveValid(potentialUpDownPieceMove,allOtherCurrentPlayerPieces, allOpponentPlayerPieces)
                if(score == 1 or score == 2):
                    break
                newPieceBitboard = allOtherCurrentPlayerPiecesOfSameType | potentialUpDownPieceMove
                theBitBoardsObjectCopy = theBitBoardsObject.boardClone()
                if(score == 3):
                    modifyBitboardToTakePiece(theBitBoardsObjectCopy,thePlayer, pieceInstanceVariable, newPieceBitboard, potentialUpDownPieceMove)
                    finalLegalPieceMoves = [theBitBoardsObjectCopy] + finalLegalPieceMoves
                    break
                if(score == 4):
                    setattr(theBitBoardsObjectCopy, pieceInstanceVariable, newPieceBitboard)
                    finalLegalPieceMoves.append(theBitBoardsObjectCopy)
                    if(index == 0):
                        potentialUpDownPieceMove <<= 8
                    elif(index == 1):
                        potentialUpDownPieceMove >>= 8
        for index in range(2):
            if(index == 0 and ((individualPiece & LEFT_BOUND) != 0)): # check if they are already on the boundary and if so, there's no possible moves
                continue
            if(index == 1 and ((individualPiece & RIGHT_BOUND) != 0)):
                continue
            potentialLeftRightPieceMove = None
            if(index == 0):
                potentialLeftRightPieceMove = individualPiece << 1
            elif (index == 1):
                potentialLeftRightPieceMove = individualPiece >> 1
            while True:
                score = None
                if(index == 0):
                    score = isLeftRightPieceMoveValid(potentialLeftRightPieceMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, True)
                elif (index ==1):
                    score = isLeftRightPieceMoveValid(potentialLeftRightPieceMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, False)
                if(score == 1):
                    break
                newPieceBitboard = allOtherCurrentPlayerPiecesOfSameType | potentialLeftRightPieceMove
                theBitBoardsObjectCopy = theBitBoardsObject.boardClone()
                if(score == 2):
                    modifyBitboardToTakePiece(theBitBoardsObjectCopy, thePlayer, pieceInstanceVariable, newPieceBitboard, potentialLeftRightPieceMove)
                    finalLegalPieceMoves = [theBitBoardsObjectCopy] + finalLegalPieceMoves
                    break
                if(score == 3):
                    setattr(theBitBoardsObjectCopy, pieceInstanceVariable, newPieceBitboard)
                    finalLegalPieceMoves.append(theBitBoardsObjectCopy)
                    break
                if(score == 4):
                    setattr(theBitBoardsObjectCopy, pieceInstanceVariable, newPieceBitboard)
                    finalLegalPieceMoves.append(theBitBoardsObjectCopy)
                    if(index == 0):
                        potentialLeftRightPieceMove <<= 1
                    elif(index == 1):
                        potentialLeftRightPieceMove >>= 1
    return finalLegalPieceMoves

def generateStraightLinePieceMovesCount(thePlayer:Player, theBitBoardsObject, pieceInstanceVariable):
    individualPieceBitboards = splitPieceIntoIndividualBitboards(pieceInstanceVariable, theBitBoardsObject)
    finalLegalPieceMoveCount = 0
    allOpponentPlayerPieces = generateOpponentMask(thePlayer,theBitBoardsObject)
    for individualPiece in individualPieceBitboards:
        #other friendly pieces mask
        allOtherCurrentPlayerPieces = generateFriendlyMasks(thePlayer, pieceInstanceVariable, theBitBoardsObject, individualPiece)[0]
        #up and down
        for index in range(2):
            potentialUpDownPieceMove = None
            if (index == 0):
                potentialUpDownPieceMove = individualPiece << 8
            elif (index == 1):
                potentialUpDownPieceMove = individualPiece >> 8
            while True:
                score = isUpDownPieceMoveValid(potentialUpDownPieceMove,allOtherCurrentPlayerPieces, allOpponentPlayerPieces)
                if(score == 1 or score == 2):
                    break
                if(score == 3):
                    finalLegalPieceMoveCount += 1
                    break
                if(score == 4):
                    finalLegalPieceMoveCount += 1
                    if(index == 0):
                        potentialUpDownPieceMove <<= 8
                    elif(index == 1):
                        potentialUpDownPieceMove >>= 8
        for index in range(2):
            if(index == 0 and ((individualPiece & LEFT_BOUND) != 0)): # check if they are already on the boundary and if so, there's no possible moves
                continue
            if(index == 1 and ((individualPiece & RIGHT_BOUND) != 0)):
                continue
            potentialLeftRightPieceMove = None
            if(index == 0):
                potentialLeftRightPieceMove = individualPiece << 1
            elif (index == 1):
                potentialLeftRightPieceMove = individualPiece >> 1
            while True:
                score = None
                if(index == 0):
                    score = isLeftRightPieceMoveValid(potentialLeftRightPieceMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, True)
                elif (index ==1):
                    score = isLeftRightPieceMoveValid(potentialLeftRightPieceMove, allOtherCurrentPlayerPieces, allOpponentPlayerPieces, False)
                if(score == 1):
                    break
                if(score == 2 or score == 3):
                    finalLegalPieceMoveCount += 1
                    break
                if(score == 4):
                    finalLegalPieceMoveCount += 1
                    if(index == 0):
                        potentialLeftRightPieceMove <<= 1
                    elif(index == 1):
                        potentialLeftRightPieceMove >>= 1
    return finalLegalPieceMoveCount




