from ChessEnums import Player
from DiagonalLineMoveUtilities import generateDiagonalPieceMoves, generateDiagonalPieceMovesCount

bishopInstanceVariableDictionary = {
    Player.COMPUTER: "_computerBishops",
    Player.HUMAN: "_humanBishops"
}
def generateBishopMoves(thePlayer: Player, theBitBoardsObject):
    return generateDiagonalPieceMoves(thePlayer, theBitBoardsObject, bishopInstanceVariableDictionary[thePlayer])
def generateBishopMovesCount(thePlayer: Player, theBitBoardsObject):
    return generateDiagonalPieceMovesCount(thePlayer, theBitBoardsObject, bishopInstanceVariableDictionary[thePlayer])

