from ChessEnums import Player
from StraightLineMoveUtilties import generateStraightLinePieceMoves
from DiagonalLineMoveUtilities import generateDiagonalPieceMoves
queenInstanceVariableDictionary = {
    Player.COMPUTER: "_computerQueens",
    Player.HUMAN: "_humanQueens"
}
def generateQueenMoves(thePlayer: Player, theBitBoardsObject):
    return (*generateStraightLinePieceMoves(thePlayer,theBitBoardsObject, queenInstanceVariableDictionary[thePlayer]) , *generateDiagonalPieceMoves(thePlayer, theBitBoardsObject, queenInstanceVariableDictionary[thePlayer]))