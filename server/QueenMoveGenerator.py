from ChessEnums import Player
from StraightLineMoveUtilties import generateStraightLinePieceMoves, generateStraightLinePieceMovesCount
from DiagonalLineMoveUtilities import generateDiagonalPieceMoves, generateDiagonalPieceMovesCount
queenInstanceVariableDictionary = {
    Player.COMPUTER: "_computerQueens",
    Player.HUMAN: "_humanQueens"
}
def generateQueenMoves(thePlayer: Player, theBitBoardsObject):
    return (*generateStraightLinePieceMoves(thePlayer,theBitBoardsObject, queenInstanceVariableDictionary[thePlayer]) , *generateDiagonalPieceMoves(thePlayer, theBitBoardsObject, queenInstanceVariableDictionary[thePlayer]))
def generateQueenMovesCount(thePlayer: Player, theBitBoardsObject):
    return generateStraightLinePieceMovesCount(thePlayer, theBitBoardsObject, queenInstanceVariableDictionary[thePlayer]) + generateDiagonalPieceMovesCount(thePlayer, theBitBoardsObject, queenInstanceVariableDictionary[thePlayer])
