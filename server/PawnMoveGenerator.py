from ChessEnums import Player
from BoardState import BoardState
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
'''
pawn rules:

If pawn is on default line, it can move up two or one
If the Pawn has an opponent piece diagonally from it, it can capture and if not it cant


If on any of the above pawn moves, it lands on opposite end of the board, you can replace with either a queen or knight

'''

def generatePawnMoves(thePlayer: Player, theBitboardsObject: BoardState):
    individualPawnBitboards = splitPieceIntoIndividualBitboards(PAWN_INSTANCE_VARIABLE_DICTIONARY[thePlayer], theBitboardsObject)
    finalLegalPawnMoves = []
    allOpponentPlayerPieces = generateOpponentMask(thePlayer, theBitboardsObject)
    for individualPawn in individualPawnBitboards:
        allOtherCurrentPlayerPieces, allOtherCurrentPlayerPiecesOfSameType = generateFriendlyMasks(thePlayer,PAWN_INSTANCE_VARIABLE_DICTIONARY[thePlayer], theBitboardsObject, individualPawn)
        allPiecesOtherThanThisPawn = allOtherCurrentPlayerPieces | allOpponentPlayerPieces
        if(thePlayer == Player.COMPUTER):
            potentialOffsetsForThisPiece = []
            if((individualPawn >> 8) & allPiecesOtherThanThisPawn) == 0:
                potentialOffsetsForThisPiece.append(8)
            if(((individualPawn & PAWN_DEFAULT_DICTIONARY[thePlayer]) != 0) and ((individualPawn >> 16) & allPiecesOtherThanThisPawn) == 0):
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
                    theBitboardsObjectCopy2 = theBitboardsObjectCopy.boardClone()
                    theBitboardsObjectCopy.computerQueens |= potentialMove
                    theBitboardsObjectCopy2.computerKnights |= potentialMove
                    finalLegalPawnMoves.append(theBitboardsObjectCopy2)
                finalLegalPawnMoves.append(theBitboardsObjectCopy)     
        else:    
            potentialOffsetsForThisPiece = []
            if((individualPawn << 8) & allPiecesOtherThanThisPawn) == 0:
                potentialOffsetsForThisPiece.append(8)
            if(((individualPawn & PAWN_DEFAULT_DICTIONARY[thePlayer]) != 0) and ((individualPawn << 16) & allPiecesOtherThanThisPawn) == 0):
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
                    theBitboardsObjectCopy2 = theBitboardsObjectCopy.boardClone()
                    theBitboardsObjectCopy.humanQueens |= potentialMove
                    theBitboardsObjectCopy2.humanKnights |= potentialMove
                    finalLegalPawnMoves.append(theBitboardsObjectCopy2)
                finalLegalPawnMoves.append(theBitboardsObjectCopy)
    return finalLegalPawnMoves


