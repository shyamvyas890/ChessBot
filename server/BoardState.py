from KnightMovesGenerator import generateKnightMoves
from RookMovesGenerator import generateRookMoves
from BishopMovesGenerator import generateBishopMoves
from KingMoveGenerator import generateKingMoves
from QueenMoveGenerator import generateQueenMoves
from PawnMoveGenerator import generatePawnMoves
from ChessEnums import Player
from DebuggingTools import board_to_2D_array
class BoardState:
    def __init__(self, 
                 computerKings, computerRooks, computerBishops, computerQueens, 
                 computerKnights, computerPawns, humanKings, humanRooks, 
                 humanBishops, humanQueens, humanKnights, humanPawns, 
                 numComputerKings, numComputerRooks, numComputerBishops, numComputerQueens,
                 numComputerKnights, numComputerPawns, numHumanKings, numHumanRooks,
                 numHumanBishops, numHumanQueens, numHumanKnights, numHumanPawns):
        self._computerKings = computerKings
        self._computerRooks = computerRooks
        self._computerBishops = computerBishops
        self._computerQueens = computerQueens
        self._computerKnights = computerKnights
        self._computerPawns = computerPawns
        self._humanKings = humanKings
        self._humanRooks = humanRooks
        self._humanBishops = humanBishops
        self._humanQueens = humanQueens
        self._humanKnights = humanKnights
        self._humanPawns = humanPawns
        self._numComputerKings = numComputerKings
        self._numComputerRooks = numComputerRooks
        self._numComputerBishops = numComputerBishops
        self._numComputerQueens = numComputerQueens
        self._numComputerKnights = numComputerKnights
        self._numComputerPawns = numComputerPawns
        self._numHumanKings = numHumanKings
        self._numHumanRooks = numHumanRooks
        self._numHumanBishops = numHumanBishops
        self._numHumanQueens = numHumanQueens
        self._numHumanKnights = numHumanKnights
        self._numHumanPawns = numHumanPawns

    @property
    def numComputerKings(self):
        return self._numComputerKings

    @numComputerKings.setter
    def numComputerKings(self, value):
        self._numComputerKings = value

    @property
    def numComputerRooks(self):
        return self._numComputerRooks

    @numComputerRooks.setter
    def numComputerRooks(self, value):
        self._numComputerRooks = value

    @property
    def numComputerBishops(self):
        return self._numComputerBishops

    @numComputerBishops.setter
    def numComputerBishops(self, value):
        self._numComputerBishops = value

    @property
    def numComputerQueens(self):
        return self._numComputerQueens

    @numComputerQueens.setter
    def numComputerQueens(self, value):
        self._numComputerQueens = value

    @property
    def numComputerKnights(self):
        return self._numComputerKnights

    @numComputerKnights.setter
    def numComputerKnights(self, value):
        self._numComputerKnights = value

    @property
    def numComputerPawns(self):
        return self._numComputerPawns

    @numComputerPawns.setter
    def numComputerPawns(self, value):
        self._numComputerPawns = value

    @property
    def numHumanKings(self):
        return self._numHumanKings

    @numHumanKings.setter
    def numHumanKings(self, value):
        self._numHumanKings = value

    @property
    def numHumanRooks(self):
        return self._numHumanRooks

    @numHumanRooks.setter
    def numHumanRooks(self, value):
        self._numHumanRooks = value

    @property
    def numHumanBishops(self):
        return self._numHumanBishops

    @numHumanBishops.setter
    def numHumanBishops(self, value):
        self._numHumanBishops = value

    @property
    def numHumanQueens(self):
        return self._numHumanQueens

    @numHumanQueens.setter
    def numHumanQueens(self, value):
        self._numHumanQueens = value

    @property
    def numHumanKnights(self):
        return self._numHumanKnights

    @numHumanKnights.setter
    def numHumanKnights(self, value):
        self._numHumanKnights = value

    @property
    def numHumanPawns(self):
        return self._numHumanPawns

    @numHumanPawns.setter
    def numHumanPawns(self, value):
        self._numHumanPawns = value

    @property
    def computerKings(self):
        return self._computerKings

    @computerKings.setter
    def computerKings(self, value):
        self._computerKings = value

    @property
    def computerRooks(self):
        return self._computerRooks

    @computerRooks.setter
    def computerRooks(self, value):
        self._computerRooks = value

    @property
    def computerBishops(self):
        return self._computerBishops

    @computerBishops.setter
    def computerBishops(self, value):
        self._computerBishops = value

    @property
    def computerQueens(self):
        return self._computerQueens

    @computerQueens.setter
    def computerQueens(self, value):
        self._computerQueens = value

    @property
    def computerKnights(self):
        return self._computerKnights

    @computerKnights.setter
    def computerKnights(self, value):
        self._computerKnights = value

    @property
    def computerPawns(self):
        return self._computerPawns

    @computerPawns.setter
    def computerPawns(self, value):
        self._computerPawns = value

    @property
    def humanKings(self):
        return self._humanKings

    @humanKings.setter
    def humanKings(self, value):
        self._humanKings = value

    @property
    def humanRooks(self):
        return self._humanRooks

    @humanRooks.setter
    def humanRooks(self, value):
        self._humanRooks = value

    @property
    def humanBishops(self):
        return self._humanBishops

    @humanBishops.setter
    def humanBishops(self, value):
        self._humanBishops = value

    @property
    def humanQueens(self):
        return self._humanQueens

    @humanQueens.setter
    def humanQueens(self, value):
        self._humanQueens = value

    @property
    def humanKnights(self):
        return self._humanKnights

    @humanKnights.setter
    def humanKnights(self, value):
        self._humanKnights = value

    @property
    def humanPawns(self):
        return self._humanPawns

    @humanPawns.setter
    def humanPawns(self, value):
        self._humanPawns = value

    def boardClone(self):
        return BoardState(
            self._computerKings,
            self._computerRooks,
            self._computerBishops,
            self._computerQueens,
            self._computerKnights,
            self._computerPawns,
            self._humanKings,
            self._humanRooks,
            self._humanBishops,
            self._humanQueens,
            self._humanKnights,
            self._humanPawns,
            self._numComputerKings,
            self._numComputerRooks,
            self._numComputerBishops,
            self._numComputerQueens,
            self._numComputerKnights,
            self._numComputerPawns,
            self._numHumanKings,
            self._numHumanRooks,
            self._numHumanBishops,
            self._numHumanQueens,
            self._numHumanKnights,
            self._numHumanPawns
        )
    def evaluate(self):
        return (200*(self.numComputerKings - self.numHumanKings) + 9 * (self.numComputerQueens - self.numHumanQueens) + 5 * (self.numComputerRooks - self.numHumanRooks) + 3* (self.numComputerBishops - self.numHumanBishops + self.numComputerKnights - self.numHumanKnights) + (self.numComputerPawns - self.numHumanPawns) )
    def children(self, thePlayer: Player):
        # theKnights = generateKnightMoves(thePlayer, self)
        # thePawns = generatePawnMoves(thePlayer, self)
        # theBishops = generateBishopMoves(thePlayer, self)
        # theRooks = generateRookMoves(thePlayer, self)
        # theQueens = generateQueenMoves(thePlayer, self)
        # theKings = generateKingMoves(thePlayer, self)
        # print("KNIGHT MOVES")
        # for theKnight in theKnights:
        #     board_to_2D_array(theKnight)
        # print("PAWN MOVES")
        # for thePawn in thePawns:
        #     board_to_2D_array(thePawn)
        # print("BISHOP MOVES")
        # for theBishop in theBishops:
        #     board_to_2D_array(theBishop)
        # print("ROOK MOVES")
        # for theRook in theRooks:
        #     board_to_2D_array(theRook)
        # print("QUEEN MOVES")
        # for theQueen in theQueens:
        #     board_to_2D_array(theQueen)
        # print("KING MOVES")
        # for theKing in theKings:
        #     board_to_2D_array(theKing)
        return (*generateKnightMoves(thePlayer, self), *generatePawnMoves(thePlayer, self), *generateBishopMoves(thePlayer, self), *generateRookMoves(thePlayer, self), *generateQueenMoves(thePlayer, self), *generateKingMoves(thePlayer, self))
