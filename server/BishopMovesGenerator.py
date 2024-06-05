from ChessEnums import Player
from BoardState import BoardState
from DiagonalLineMoveUtilities import generateDiagonalPieceMoves

bishopInstanceVariableDictionary = {
    Player.COMPUTER: "_computerBishops",
    Player.HUMAN: "_humanBishops"
}
def generateBishopMoves(thePlayer: Player, theBitBoardsObject: BoardState):
    return generateDiagonalPieceMoves(thePlayer, theBitBoardsObject, bishopInstanceVariableDictionary[thePlayer])
