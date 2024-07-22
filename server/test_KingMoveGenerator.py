import pytest
from KingMoveGenerator import generateKingMoves, generateKingMovesCount
from ChessEnums import Player
from BoardState import BoardState

def test_generateKingMoves():
    board = BoardState(
        computerKings=0x1000000000000000, # King on top left corner and then move right 3 spaces
        computerRooks=0,
        computerBishops=0,
        computerQueens=0,
        computerKnights=0,
        computerPawns=0,
        humanKings=0x0000000000000001,
        humanRooks=0,
        humanBishops=0,
        humanQueens=0,
        humanKnights=0,
        humanPawns=0,
        numComputerKings=1,
        numComputerRooks=0,
        numComputerBishops=0,
        numComputerQueens=0,
        numComputerKnights=0,
        numComputerPawns=0,
        numHumanKings=1,
        numHumanRooks=0,
        numHumanBishops=0,
        numHumanQueens=0,
        numHumanKnights=0,
        numHumanPawns=0
    )

    moves_with_capture, moves_no_capture = generateKingMoves(Player.COMPUTER, board)
    assert len(moves_with_capture) == 0
    assert len(moves_no_capture) == 5

    moves_with_capture, moves_no_capture = generateKingMoves(Player.HUMAN, board)
    assert len(moves_with_capture) == 0
    assert len(moves_no_capture) == 3


def test_generateKingMovesCount():
    board = BoardState(
        computerKings=0x1000000000000000, # King on top left corner and then move right 3 spaces
        computerRooks=0,
        computerBishops=0,
        computerQueens=0,
        computerKnights=0,
        computerPawns=0,
        humanKings=0x0000000000000001,
        humanRooks=0,
        humanBishops=0,
        humanQueens=0,
        humanKnights=0,
        humanPawns=0,
        numComputerKings=1,
        numComputerRooks=0,
        numComputerBishops=0,
        numComputerQueens=0,
        numComputerKnights=0,
        numComputerPawns=0,
        numHumanKings=1,
        numHumanRooks=0,
        numHumanBishops=0,
        numHumanQueens=0,
        numHumanKnights=0,
        numHumanPawns=0
    )

    count = generateKingMovesCount(Player.COMPUTER, board)
    assert count == 5
    count = generateKingMovesCount(Player.HUMAN, board)
    assert count == 3


