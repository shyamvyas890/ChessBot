from ChessEnums import Player, Piece
from BoardState import BoardState
def splitPieceIntoIndividualBitboards (instanceVariableString:str, theBitBoardsObject: BoardState):
    originalPieceBitboard = getattr(theBitBoardsObject, instanceVariableString)
    individualPieceBitboards = []
    individualBoard = originalPieceBitboard & (~originalPieceBitboard + 1)
    individualPieceBitboards.append(individualBoard)
    originalPieceBitboard ^= individualBoard
    while (originalPieceBitboard != 0):
        individualBoard = originalPieceBitboard & (~originalPieceBitboard + 1)
        individualPieceBitboards.append(individualBoard)
        originalPieceBitboard ^= individualBoard
    return individualPieceBitboards
def generateOpponentMask (thePlayer: Player, theBitBoardsObject: BoardState):
    if(thePlayer == Player.COMPUTER):
        return (theBitBoardsObject.humanKings | theBitBoardsObject.humanRooks | theBitBoardsObject.humanBishops | theBitBoardsObject.humanQueens | theBitBoardsObject.humanKnights | theBitBoardsObject.humanPawns)
    elif(thePlayer == Player.HUMAN):
        return (theBitBoardsObject.computerKings | theBitBoardsObject.computerRooks | theBitBoardsObject.computerBishops | theBitBoardsObject.computerQueens | theBitBoardsObject.computerKnights | theBitBoardsObject.computerPawns) 
def generateFriendlyMasks (thePlayer: Player,thePlayerAndPieceTypeInstanceVariable: str, theBitBoardsObject:BoardState, individualPieceBitboard):
    allOtherCurrentPlayerPieces= None
    if(thePlayer == Player.COMPUTER):
        allOtherCurrentPlayerPieces = theBitBoardsObject.computerKings | theBitBoardsObject.computerRooks | theBitBoardsObject.computerBishops | theBitBoardsObject.computerQueens | theBitBoardsObject.computerKnights | theBitBoardsObject.computerPawns
    elif (thePlayer == Player.HUMAN):
        allOtherCurrentPlayerPieces = theBitBoardsObject.humanKings | theBitBoardsObject.humanRooks | theBitBoardsObject.humanBishops | theBitBoardsObject.humanQueens | theBitBoardsObject.humanKnights | theBitBoardsObject.humanPawns
    allOtherCurrentPlayerPieces ^= individualPieceBitboard
    allOtherCurrentPlayerPieceTypePieces = ((getattr(theBitBoardsObject, thePlayerAndPieceTypeInstanceVariable)) ^ individualPieceBitboard)
    return (allOtherCurrentPlayerPieces, allOtherCurrentPlayerPieceTypePieces)
def modifyBitboardToTakePiece (theBitBoardsObjectCopy: BoardState, thePlayer: Player, instanceVariableString: str, newPieceBitboard: int, isolatedPieceBitboard: int):
    setattr(theBitBoardsObjectCopy, instanceVariableString, newPieceBitboard)
    if(thePlayer == Player.COMPUTER):
        if((theBitBoardsObjectCopy.humanKings & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.humanKings ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numHumanKings -= 1
        elif((theBitBoardsObjectCopy.humanRooks & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.humanRooks ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numHumanRooks -= 1
        elif((theBitBoardsObjectCopy.humanBishops & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.humanBishops ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numHumanBishops -= 1
        elif((theBitBoardsObjectCopy.humanQueens & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.humanQueens ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numHumanQueens -= 1
        elif((theBitBoardsObjectCopy.humanKnights & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.humanKnights ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numHumanKnights -= 1
        elif((theBitBoardsObjectCopy.humanPawns & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.humanPawns ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numHumanPawns -= 1
    elif(thePlayer == Player.HUMAN):
        if((theBitBoardsObjectCopy.computerKings & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.computerKings ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numComputerKings -= 1
        elif((theBitBoardsObjectCopy.computerRooks & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.computerRooks ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numComputerRooks -= 1
        elif((theBitBoardsObjectCopy.computerBishops & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.computerBishops ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numComputerBishops -= 1
        elif((theBitBoardsObjectCopy.computerQueens & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.computerQueens ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numComputerQueens -= 1
        elif((theBitBoardsObjectCopy.computerKnights & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.computerKnights ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numComputerKnights -= 1
        elif((theBitBoardsObjectCopy.computerPawns & isolatedPieceBitboard) != 0):
            theBitBoardsObjectCopy.computerPawns ^= isolatedPieceBitboard
            theBitBoardsObjectCopy.numComputerPawns -= 1


