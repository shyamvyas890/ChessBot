from ChessEnums import Player
from DiagonalLineMoveUtilities import generateDiagonalPieceMoves

bishopInstanceVariableDictionary = {
    Player.COMPUTER: "_computerBishops",
    Player.HUMAN: "_humanBishops"
}
def generateBishopMoves(thePlayer: Player, theBitBoardsObject):
    return generateDiagonalPieceMoves(thePlayer, theBitBoardsObject, bishopInstanceVariableDictionary[thePlayer])
