from ChessEnums import Player
from StraightLineMoveUtilties import generateStraightLinePieceMoves, generateStraightLinePieceMovesCount
from DiagonalLineMoveUtilities import generateDiagonalPieceMoves, generateDiagonalPieceMovesCount
queenInstanceVariableDictionary = {
    Player.COMPUTER: "_computerQueens",
    Player.HUMAN: "_humanQueens"
}
def generateQueenMoves(thePlayer: Player, theBitBoardsObject):
    straightLineCaptures, straightLineRegular = generateStraightLinePieceMoves(thePlayer,theBitBoardsObject, queenInstanceVariableDictionary[thePlayer])
    diagonalLineCaptures, diagonalLineRegular = generateDiagonalPieceMoves(thePlayer, theBitBoardsObject, queenInstanceVariableDictionary[thePlayer])
    return ((*straightLineCaptures, *diagonalLineCaptures),(*straightLineRegular, *diagonalLineRegular))
def generateQueenMovesCount(thePlayer: Player, theBitBoardsObject):
    return generateStraightLinePieceMovesCount(thePlayer, theBitBoardsObject, queenInstanceVariableDictionary[thePlayer]) + generateDiagonalPieceMovesCount(thePlayer, theBitBoardsObject, queenInstanceVariableDictionary[thePlayer])
