from ChessEnums import Player
from StraightLineMoveUtilties import generateStraightLinePieceMoves
        
rookInstanceVariableDictionary = {
    Player.COMPUTER: "_computerRooks",
    Player.HUMAN: "_humanRooks"
}
def generateRookMoves(thePlayer: Player, theBitBoardsObject):
    return generateStraightLinePieceMoves(thePlayer,theBitBoardsObject, rookInstanceVariableDictionary[thePlayer])
