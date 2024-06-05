from ChessEnums import Player
from BoardState import BoardState
from StraightLineMoveUtilties import generateStraightLinePieceMoves
from DiagonalLineMoveUtilities import generateDiagonalPieceMoves
queenInstanceVariableDictionary = {
    Player.COMPUTER: "_computerQueens",
    Player.HUMAN: "_humanQueens"
}
def generateQueenMoves(thePlayer: Player, theBitBoardsObject: BoardState):
    return (*generateStraightLinePieceMoves(thePlayer,theBitBoardsObject, queenInstanceVariableDictionary[thePlayer]) , *generateDiagonalPieceMoves(thePlayer, theBitBoardsObject, queenInstanceVariableDictionary[thePlayer]))