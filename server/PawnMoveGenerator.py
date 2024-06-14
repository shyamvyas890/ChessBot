from ChessEnums import Player
from UtilityFunctions import splitPieceIntoIndividualBitboards, generateOpponentMask, generateFriendlyMasks, modifyBitboardToTakePiece

PAWN_INSTANCE_VARIABLE_DICTIONARY = {
    Player.COMPUTER: "_computerPawns",
    Player.HUMAN: "_humanPawns"
}
PAWN_FINAL_ROW_DICTIONARY = {
    Player.COMPUTER: 0x00_00_00_00_00_00_00_FF,
    Player.HUMAN: 0xFF_00_00_00_00_00_00_00
}
PAWN_DEFAULT_DICTIONARY = {
    Player.COMPUTER: 0x00_FF_00_00_00_00_00_00,
    Player.HUMAN: 0x00_00_00_00_00_00_FF_00
}
RIGHT_BOUND = 0x01_01_01_01_01_01_01_01
LEFT_BOUND = 0x80_80_80_80_80_80_80_80

def generatePawnMoves(thePlayer: Player, theBitboardsObject):
    individualPawnBitboards = splitPieceIntoIndividualBitboards(PAWN_INSTANCE_VARIABLE_DICTIONARY[thePlayer], theBitboardsObject)
    legalPawnMovesPromotion = [] # may be capture or not capture
    legalPawnMovesWITHCapture = [] # definitely not promotion
    legalPawnMovesNOCapture = [] # definitely not promotion
    allOpponentPlayerPieces = generateOpponentMask(thePlayer, theBitboardsObject)
    for individualPawn in individualPawnBitboards:
        allOtherCurrentPlayerPieces, allOtherCurrentPlayerPiecesOfSameType = generateFriendlyMasks(thePlayer,PAWN_INSTANCE_VARIABLE_DICTIONARY[thePlayer], theBitboardsObject, individualPawn)
        allPiecesOtherThanThisPawn = allOtherCurrentPlayerPieces | allOpponentPlayerPieces
        if(thePlayer == Player.COMPUTER):
            potentialOffsetsForThisPiece = []
            if((individualPawn >> 8) & allPiecesOtherThanThisPawn) == 0:
                potentialOffsetsForThisPiece.append(8)
            if(((individualPawn & PAWN_DEFAULT_DICTIONARY[thePlayer]) != 0) and (((individualPawn >> 16) | (individualPawn >> 8)) & allPiecesOtherThanThisPawn) == 0):
                potentialOffsetsForThisPiece.append(16)
            if((individualPawn & LEFT_BOUND) == 0) and  (((individualPawn >> 7) & allOpponentPlayerPieces) != 0):
                potentialOffsetsForThisPiece.append(7)
            if((individualPawn & RIGHT_BOUND) == 0) and  (((individualPawn >> 9) & allOpponentPlayerPieces) != 0):
                potentialOffsetsForThisPiece.append(9)
            for offset in potentialOffsetsForThisPiece:
                potentialMove = individualPawn >> offset
                newPawnBitboard = allOtherCurrentPlayerPiecesOfSameType | potentialMove
                theBitboardsObjectCopy = theBitboardsObject.boardClone()
                if(offset == 7 or offset == 9):
                    modifyBitboardToTakePiece(theBitboardsObjectCopy, thePlayer, PAWN_INSTANCE_VARIABLE_DICTIONARY[thePlayer], newPawnBitboard,potentialMove)
                else:
                    theBitboardsObjectCopy.computerPawns = newPawnBitboard
                if((potentialMove & PAWN_FINAL_ROW_DICTIONARY[thePlayer]) != 0):
                    theBitboardsObjectCopy.computerPawns ^= potentialMove
                    theBitboardsObjectCopy.numComputerPawns -= 1
                    theBitboardsObjectCopy2 = theBitboardsObjectCopy.boardClone()
                    theBitboardsObjectCopy.computerQueens |= potentialMove
                    theBitboardsObjectCopy.numComputerQueens += 1
                    theBitboardsObjectCopy2.computerKnights |= potentialMove
                    theBitboardsObjectCopy2.numComputerKnights += 1
                    legalPawnMovesPromotion.append(theBitboardsObjectCopy)
                    legalPawnMovesPromotion.append(theBitboardsObjectCopy2)
                else:
                    if(offset == 7 or offset == 9):
                        legalPawnMovesWITHCapture.append(theBitboardsObjectCopy)
                    else:
                        legalPawnMovesNOCapture.append(theBitboardsObjectCopy)     
        else:    
            potentialOffsetsForThisPiece = []
            if((individualPawn << 8) & allPiecesOtherThanThisPawn) == 0:
                potentialOffsetsForThisPiece.append(8)
            if(((individualPawn & PAWN_DEFAULT_DICTIONARY[thePlayer]) != 0) and (((individualPawn << 16) | (individualPawn << 8)) & allPiecesOtherThanThisPawn) == 0):
                potentialOffsetsForThisPiece.append(16)
            if((individualPawn & LEFT_BOUND) == 0) and  (((individualPawn << 9) & allOpponentPlayerPieces) != 0):
                potentialOffsetsForThisPiece.append(9)
            if((individualPawn & RIGHT_BOUND) == 0) and  (((individualPawn << 7) & allOpponentPlayerPieces) != 0):
                potentialOffsetsForThisPiece.append(7)
            for offset in potentialOffsetsForThisPiece:
                potentialMove = individualPawn << offset
                newPawnBitboard = allOtherCurrentPlayerPiecesOfSameType | potentialMove
                theBitboardsObjectCopy = theBitboardsObject.boardClone()
                if(offset == 7 or offset == 9):
                    modifyBitboardToTakePiece(theBitboardsObjectCopy, thePlayer, PAWN_INSTANCE_VARIABLE_DICTIONARY[thePlayer], newPawnBitboard,potentialMove)
                else:
                    theBitboardsObjectCopy.humanPawns = newPawnBitboard
                if((potentialMove & PAWN_FINAL_ROW_DICTIONARY[thePlayer]) != 0):
                    theBitboardsObjectCopy.humanPawns ^= potentialMove
                    theBitboardsObjectCopy.numHumanPawns -= 1
                    theBitboardsObjectCopy2 = theBitboardsObjectCopy.boardClone()
                    theBitboardsObjectCopy.humanQueens |= potentialMove
                    theBitboardsObjectCopy.numHumanQueens += 1
                    theBitboardsObjectCopy2.humanKnights |= potentialMove
                    theBitboardsObjectCopy2.numHumanKnights += 1
                    legalPawnMovesPromotion.append(theBitboardsObjectCopy)
                    legalPawnMovesPromotion.append(theBitboardsObjectCopy2)
                else:
                    if(offset == 7 or offset == 9):
                        legalPawnMovesWITHCapture.append(theBitboardsObjectCopy)
                    else:
                        legalPawnMovesNOCapture.append(theBitboardsObjectCopy)

    return (legalPawnMovesPromotion, legalPawnMovesWITHCapture, legalPawnMovesNOCapture)
def generatePawnMoveCount (thePlayer: Player, theBitboardsObject):
    individualPawnBitboards = splitPieceIntoIndividualBitboards(PAWN_INSTANCE_VARIABLE_DICTIONARY[thePlayer], theBitboardsObject)
    allOpponentPlayerPieces = generateOpponentMask(thePlayer, theBitboardsObject)
    totalPawnMoves = 0
    for individualPawn in individualPawnBitboards:
        allOtherCurrentPlayerPieces = generateFriendlyMasks(thePlayer,PAWN_INSTANCE_VARIABLE_DICTIONARY[thePlayer], theBitboardsObject, individualPawn)[0]
        allPiecesOtherThanThisPawn = allOtherCurrentPlayerPieces | allOpponentPlayerPieces
        if(thePlayer == Player.COMPUTER):
            if((individualPawn >> 8) & allPiecesOtherThanThisPawn) == 0:
                totalPawnMoves += 1
            if(((individualPawn & PAWN_DEFAULT_DICTIONARY[thePlayer]) != 0) and (((individualPawn >> 16) | (individualPawn >> 8)) & allPiecesOtherThanThisPawn) == 0):
                totalPawnMoves += 1
            if((individualPawn & LEFT_BOUND) == 0) and  (((individualPawn >> 7) & allOpponentPlayerPieces) != 0):
                totalPawnMoves += 1
            if((individualPawn & RIGHT_BOUND) == 0) and  (((individualPawn >> 9) & allOpponentPlayerPieces) != 0):
                totalPawnMoves += 1     
        else:
            if((individualPawn << 8) & allPiecesOtherThanThisPawn) == 0:
                totalPawnMoves += 1
            if(((individualPawn & PAWN_DEFAULT_DICTIONARY[thePlayer]) != 0) and (((individualPawn << 16) | (individualPawn << 8)) & allPiecesOtherThanThisPawn) == 0):
                totalPawnMoves += 1
            if((individualPawn & LEFT_BOUND) == 0) and  (((individualPawn << 9) & allOpponentPlayerPieces) != 0):
                totalPawnMoves += 1
            if((individualPawn & RIGHT_BOUND) == 0) and  (((individualPawn << 7) & allOpponentPlayerPieces) != 0):
                totalPawnMoves += 1
    return totalPawnMoves




