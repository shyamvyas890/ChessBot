from ChessEnums import Player, Piece
from DebuggingTools import pretty_print_board
from BoardState import BoardState
from UtilityFunctions import splitPieceIntoIndividualBitboards, generateOpponentMask, generateFriendlyMasks, modifyBitboardToTakePiece

RIGHT_BOUND = 0x01_01_01_01_01_01_01_01
LEFT_BOUND = 0x80_80_80_80_80_80_80_80
UPPER_BOUND = 0xFF_00_00_00_00_00_00_00
LOWER_BOUND = 0x00_00_00_00_00_00_00_FF

kingInstanceVariableDictionary = {
    Player.COMPUTER: "_computerKings",
    Player.HUMAN: "_humanKings"
}

diagonalOffsets = (7,9,-9,-7) # southwest, southeast, northwest, northeast
straightOffsets = (8,-8,1,-1) # south, north, right, left
def generateKingMoves (thePlayer: Player, theBitBoardsObject: BoardState):
    finalLegalKingMoves = []
    allOpponentPlayerPieces = generateOpponentMask(thePlayer,theBitBoardsObject)
    allOtherCurrentPlayerPieces = generateFriendlyMasks(thePlayer, kingInstanceVariableDictionary[thePlayer], theBitBoardsObject, getattr(theBitBoardsObject, kingInstanceVariableDictionary[thePlayer]))[0]
    currentKing = getattr(theBitBoardsObject, kingInstanceVariableDictionary[thePlayer])
    legalOffsets = []

    if ( ((currentKing & LEFT_BOUND) == 0) and ((currentKing & LOWER_BOUND) == 0) and (((currentKing >> 7) & allOtherCurrentPlayerPieces) == 0)):
        legalOffsets.append(7)
    if ( ((currentKing & RIGHT_BOUND) == 0) and ((currentKing & LOWER_BOUND) == 0) and (((currentKing >> 9) & allOtherCurrentPlayerPieces) == 0)):
        legalOffsets.append(9)
    if ( ((currentKing & LEFT_BOUND) == 0) and ((currentKing & UPPER_BOUND) == 0) and (((currentKing << 9) & allOtherCurrentPlayerPieces) == 0)):
        legalOffsets.append(-9)
    if ( ((currentKing & RIGHT_BOUND) == 0) and ((currentKing & UPPER_BOUND) == 0) and (((currentKing << 7) & allOtherCurrentPlayerPieces) == 0)):
        legalOffsets.append(-7)
    if(((currentKing & LEFT_BOUND) == 0) and (((currentKing << 1) & allOtherCurrentPlayerPieces) == 0)):
        legalOffsets.append(-1)
    if(((currentKing & RIGHT_BOUND) == 0) and (((currentKing >> 1) & allOtherCurrentPlayerPieces) == 0)):
        legalOffsets.append(1)
    if(((currentKing & UPPER_BOUND) == 0) and (((currentKing <<8) & allOtherCurrentPlayerPieces) == 0)):
        legalOffsets.append(-8)
    if(((currentKing & LOWER_BOUND) == 0) and (((currentKing >>8) & allOtherCurrentPlayerPieces) == 0)):
        legalOffsets.append(8)
    
    for offset in legalOffsets:
        theBitBoardsObjectCopy = theBitBoardsObject.boardClone()
        newKingPosition = None
        if(offset > 0):
            newKingPosition = currentKing >> offset
        else:
            newKingPosition = currentKing << abs(offset)
        if(newKingPosition & allOpponentPlayerPieces) != 0:
            modifyBitboardToTakePiece(theBitBoardsObjectCopy, thePlayer,kingInstanceVariableDictionary[thePlayer], newKingPosition, newKingPosition)
        else:
            setattr(theBitBoardsObjectCopy, kingInstanceVariableDictionary[thePlayer], newKingPosition)
        finalLegalKingMoves.append(theBitBoardsObjectCopy)
    

    print(len(finalLegalKingMoves))
    for potentialMove in finalLegalKingMoves:
        pretty_print_board(getattr(potentialMove, kingInstanceVariableDictionary[thePlayer]))
        pretty_print_board(potentialMove.humanPawns)
    

    
    

    




