from ChessEnums import Player
from BoardState import BoardState
from StraightLineMoveUtilties import generateStraightLinePieceMoves
        
rookInstanceVariableDictionary = {
    Player.COMPUTER: "_computerRooks",
    Player.HUMAN: "_humanRooks"
}
def generateRookMoves(thePlayer: Player, theBitBoardsObject: BoardState):
    return generateStraightLinePieceMoves(thePlayer,theBitBoardsObject, rookInstanceVariableDictionary[thePlayer])
