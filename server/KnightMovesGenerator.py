from Player import Player
from DebuggingTools import pretty_print_board

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