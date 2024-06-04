from ChessEnums import Player, Piece
from DebuggingTools import pretty_print_board
from BoardState import BoardState
from UtilityFunctions import splitPieceIntoIndividualBitboards, generateOpponentMask, generateFriendlyMasks, modifyBitboardToTakePiece



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

        
rookInstanceVariableDictionary = {
    Player.COMPUTER: "_computerRooks",
    Player.HUMAN: "_humanRooks"
}
def generateRookMoves(thePlayer: Player, theBitBoardsObject: BoardState):
    individualRookBitboards = splitPieceIntoIndividualBitboards(rookInstanceVariableDictionary[thePlayer], theBitBoardsObject)
    isTheRookOffLeftScreen = 0x80_00_00_00_00_00_00_00
    isTheRookOffRightScreen = 0

    rightBound = 0x01_01_01_01_01_01_01_01
    leftBound = 0x80_80_80_80_80_80_80_80

    finalLegalRookMoves = []
    allOpponentPlayerPieces = generateOpponentMask(thePlayer,theBitBoardsObject)
    for individualRook in individualRookBitboards:
        #other friendly pieces mask
        allOtherCurrentPlayerPieces, allOtherCurrentPlayerRooks = generateFriendlyMasks(thePlayer, rookInstanceVariableDictionary[thePlayer], theBitBoardsObject, individualRook)
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
                    modifyBitboardToTakePiece(theBitBoardsObjectCopy,thePlayer, rookInstanceVariableDictionary[thePlayer], newRookBitboard, potentialUpDownRookMove)
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
                    modifyBitboardToTakePiece(theBitBoardsObjectCopy, thePlayer, rookInstanceVariableDictionary[thePlayer], newRookBitboard, potentialLeftRightRookMove)
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
