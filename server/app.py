from flask import Flask
from enum import Enum
app = Flask(__name__)
def pretty_print_board(bitboard):
    board = [bit for bit in format(bitboard, '064b')]
    print("---------------------------------")
    count = 0
    while(count<64):
        row = "| "
        for i in range(8):
            row += f"{board[count]} | "
            count=count+1
        print(row)
        print("---------------------------------")
class Player(Enum):
    COMPUTER = 1
    HUMAN = 2




class BoardState:
    def __init__(self, computerKings, computerRooks, computerBishops, computerQueens, computerKnights, computerPawns, humanKings, humanRooks, humanBishops, humanQueens, humanKnights, humanPawns):
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
            self._humanPawns
        )

@app.route('/')
def hello():
    initial_chess_board = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],  
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']   
    ]

    bitboardsObject = convert2DArrayToBitboards(initial_chess_board)
    generateKnightMoves(Player.HUMAN, bitboardsObject)





    return "Test"


        
'''
Capital letters are computer pieces and lowercase letters are human pieces 
K: king
R: rook
B: bishop
Q: queen
N: knight
P: pawn
'''

def convert2DArrayToBitboards(the2dArray):
    (computerKings, computerRooks, computerBishops, computerQueens, computerKnights, computerPawns, humanKings, humanRooks, humanBishops, humanQueens, humanKnights, humanPawns) = (0b0,) * 12
    for i in range(len(the2dArray)):
        for j in range(len(the2dArray[i])):
            theIndexInBitboard = (i*8) + j
            indexForBitwiseOperations = 63- theIndexInBitboard
            if(the2dArray[i][j]== "K"):
                computerKings |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "R"):
                computerRooks |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "B"):
                computerBishops |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "Q"):
                computerQueens |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "N"):
                computerKnights |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "P"):
                computerPawns |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "k"):
                humanKings |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "r"):
                humanRooks |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "b"):
                humanBishops |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "q"):
                humanQueens |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "n"):
                humanKnights |= (1 << indexForBitwiseOperations)
            elif(the2dArray[i][j]== "p"):
                humanPawns |= (1 << indexForBitwiseOperations)
    return BoardState(computerKings, computerRooks, computerBishops, computerQueens, computerKnights, computerPawns, humanKings, humanRooks, humanBishops, humanQueens, humanKnights, humanPawns)


def generateKnightMoves(thePlayer: Player, theBitboardsObject: dict):
    originalKnightBitboard = None
    if(thePlayer == Player.COMPUTER):
        originalKnightBitboard = theBitboardsObject.computerKnights
    elif(thePlayer == Player.HUMAN):
        originalKnightBitboard = theBitboardsObject.humanKnights
    individualKnightBitboards = []
    individualBoard = originalKnightBitboard & (~originalKnightBitboard + 1)
    individualKnightBitboards.append(individualBoard)
    originalKnightBitboard ^= individualBoard
    while (originalKnightBitboard != 0):
        individualBoard = originalKnightBitboard & (~originalKnightBitboard + 1)
        individualKnightBitboards.append(individualBoard)
        originalKnightBitboard ^= individualBoard        
    add6 = 0xC0_C0_C0_C0_C0_C0_C0_FF
    add10 = 0x03_03_03_03_03_03_03_FF
    add15 = 0x80_80_80_80_80_80_FF_FF
    add17 = 0x01_01_01_01_01_01_FF_FF
    sub6 = 0xFF_03_03_03_03_03_03_03
    sub10 = 0xFF_C0_C0_C0_C0_C0_C0_C0
    sub15 = 0xFF_FF_01_01_01_01_01_01
    sub17 = 0xFF_FF_80_80_80_80_80_80
    finalLegalKnightMoves = []
    for individualKnight in individualKnightBitboards:
        unviolatedMasks = []
        if((add6 & individualKnight) == 0):
            unviolatedMasks.append(6)
        if((add10 & individualKnight) == 0):
            unviolatedMasks.append(10)
        if((add15 & individualKnight) == 0):
            unviolatedMasks.append(15)
        if((add17 & individualKnight) == 0):
            unviolatedMasks.append(17)
        
        if((sub6 & individualKnight) == 0):
            unviolatedMasks.append(-6)
        if((sub10 & individualKnight) == 0):
            unviolatedMasks.append(-10)
        if((sub15 & individualKnight) == 0):
            unviolatedMasks.append(-15)
        if((sub17 & individualKnight) == 0):
            unviolatedMasks.append(-17)
        
        
        allOtherSelectedPlayerPieces = None
        if(thePlayer == Player.COMPUTER):
            allOtherSelectedPlayerPieces = theBitboardsObject.computerKings | theBitboardsObject.computerRooks | theBitboardsObject.computerBishops | theBitboardsObject.computerQueens | theBitboardsObject.computerPawns
        elif(thePlayer == Player.HUMAN):
            allOtherSelectedPlayerPieces = theBitboardsObject.humanKings | theBitboardsObject.humanRooks | theBitboardsObject.humanBishops | theBitboardsObject.humanQueens | theBitboardsObject.humanPawns

        


        otherSelectedPlayerKnightsOnCurrentBoard = 0
        for potentialOtherKnight in individualKnightBitboards:
            if(potentialOtherKnight != individualKnight):
                allOtherSelectedPlayerPieces |= potentialOtherKnight
                otherSelectedPlayerKnightsOnCurrentBoard |= potentialOtherKnight
        
        translatedBitboards = []
        for mask in unviolatedMasks:
            if(mask>0):
                translated = individualKnight >> mask
                translatedBitboards.append(translated)
            else:
                translated = individualKnight << abs(mask)
                translatedBitboards.append(translated)
        translatedBitboardsP2 = []

        for i in range(len(translatedBitboards)):
            if((translatedBitboards[i] & allOtherSelectedPlayerPieces) == 0):
                translatedBitboardsP2.append(translatedBitboards[i])
        if(thePlayer == Player.COMPUTER):
            for translatedBitboard in translatedBitboardsP2:
                newKnightBitboard = translatedBitboard | otherSelectedPlayerKnightsOnCurrentBoard
                theBitboardsObjectCopy = theBitboardsObject.boardClone()
                theBitboardsObjectCopy.computerKnights = newKnightBitboard
                if((theBitboardsObjectCopy.humanKings & translatedBitboard) != 0):
                    theBitboardsObjectCopy.humanKings ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                elif((theBitboardsObjectCopy.humanRooks & translatedBitboard) != 0):
                    theBitboardsObjectCopy.humanRooks ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                elif((theBitboardsObjectCopy.humanBishops & translatedBitboard) != 0):
                    theBitboardsObjectCopy.humanBishops ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                elif((theBitboardsObjectCopy.humanQueens & translatedBitboard) != 0):
                    theBitboardsObjectCopy.humanQueens ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                elif((theBitboardsObjectCopy.humanKnights & translatedBitboard) != 0):
                    theBitboardsObjectCopy.humanKnights ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                elif((theBitboardsObjectCopy.humanPawns & translatedBitboard) != 0):
                    theBitboardsObjectCopy.humanPawns ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                else:
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
        elif (thePlayer == Player.HUMAN):
            for translatedBitboard in translatedBitboardsP2:
                newKnightBitboard = translatedBitboard | otherSelectedPlayerKnightsOnCurrentBoard
                theBitboardsObjectCopy = theBitboardsObject.boardClone()
                theBitboardsObjectCopy.humanKnights = newKnightBitboard
                if((theBitboardsObjectCopy.computerKings & translatedBitboard) != 0):
                    theBitboardsObjectCopy.computerKings ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                elif((theBitboardsObjectCopy.computerRooks & translatedBitboard) != 0):
                    theBitboardsObjectCopy.computerRooks ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                elif((theBitboardsObjectCopy.computerBishops & translatedBitboard) != 0):
                    theBitboardsObjectCopy.computerBishops ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                elif((theBitboardsObjectCopy.computerQueens & translatedBitboard) != 0):
                    theBitboardsObjectCopy.computerQueens ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                elif((theBitboardsObjectCopy.computerKnights & translatedBitboard) != 0):
                    theBitboardsObjectCopy.computerKnights ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                elif((theBitboardsObjectCopy.computerPawns & translatedBitboard) != 0):
                    theBitboardsObjectCopy.computerPawns ^= translatedBitboard
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                    continue
                else:
                    finalLegalKnightMoves.append(theBitboardsObjectCopy)
                


    print(len(finalLegalKnightMoves))
    for finalMove in finalLegalKnightMoves:
        pretty_print_board(finalMove.humanKnights)





            
if __name__ == '__main__':
    app.run(debug=True, port=5001)
