from enum import Enum
class Player(Enum):
    COMPUTER = 1
    HUMAN = 2

class Piece(Enum):
    KING = 1
    ROOK = 2
    BISHOP = 3
    QUEEN = 4
    KNIGHT = 5
    PAWN = 6