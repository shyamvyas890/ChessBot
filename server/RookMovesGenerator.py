from ChessEnums import Player
from StraightLineMoveUtilties import generateStraightLinePieceMoves, generateStraightLinePieceMovesCount
        
rookInstanceVariableDictionary = {
    Player.COMPUTER: "_computerRooks",
    Player.HUMAN: "_humanRooks"
}
def generateRookMoves(thePlayer: Player, theBitBoardsObject):
    return generateStraightLinePieceMoves(thePlayer,theBitBoardsObject, rookInstanceVariableDictionary[thePlayer])

def generateRookMovesCount (thePlayer:Player, theBitboardsObject):
    return generateStraightLinePieceMovesCount(thePlayer, theBitboardsObject, rookInstanceVariableDictionary[thePlayer])