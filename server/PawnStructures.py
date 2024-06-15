from ChessEnums import Player
EVERYTHING_EXCEPT_RIGHT_BOUND = 0xFE_FE_FE_FE_FE_FE_FE_FE # FROM HUMAN PERSPECTIVE
EVERYTHING_EXCEPT_LEFT_BOUND = 0x7F_7F_7F_7F_7F_7F_7F_7F # FROM HUMAN PERSPECTIVE
FULL_CHESS_BOARD = 0xFF_FF_FF_FF_FF_FF_FF_FF

COLUMN_MASKS = [
        0x0101010101010101,
        0x0202020202020202,
        0x0404040404040404,
        0x0808080808080808,
        0x1010101010101010,
        0x2020202020202020,
        0x4040404040404040,
        0x8080808080808080
    ]
def count_ones (originalNum):
    count = 0
    while originalNum != 0:
        isolatedOne = originalNum & (~originalNum + 1)
        count += 1
        originalNum ^= isolatedOne
    return count

def getPassedPawnsCount(thePlayer: Player, friendlyPawns, enemyPawns):
    if(thePlayer == Player.COMPUTER):
        currentEnemyMask = enemyPawns | ((enemyPawns & EVERYTHING_EXCEPT_LEFT_BOUND) << 9) | ((enemyPawns & EVERYTHING_EXCEPT_RIGHT_BOUND) << 7)
        for _ in range(5):
            currentEnemyMask |= (currentEnemyMask << 8)
            currentEnemyMask &= FULL_CHESS_BOARD
        passedPawns = friendlyPawns & (FULL_CHESS_BOARD ^ currentEnemyMask)
        return count_ones(passedPawns)
    else:
        currentEnemyMask = enemyPawns | ((enemyPawns & EVERYTHING_EXCEPT_LEFT_BOUND) >> 7) | ((enemyPawns & EVERYTHING_EXCEPT_RIGHT_BOUND) >> 9)
        for _ in range(5):
            currentEnemyMask |= (currentEnemyMask >> 8)
        passedPawns = friendlyPawns & (FULL_CHESS_BOARD ^ currentEnemyMask)
        return count_ones(passedPawns)

def getDoubledPawnsCount(friendlyPawns):
    total = 0
    for column in COLUMN_MASKS:
        pawnsInColumn = friendlyPawns & column
        numberOfPawns = count_ones(pawnsInColumn)
        if(numberOfPawns != 1):
            total += numberOfPawns
    return total


def areTherePawnsInAdjancentFiles(index, friendlyPawns):
    if(index == 0):
        return (friendlyPawns & COLUMN_MASKS[1]) != 0
    if (index == 7):
        return (friendlyPawns & COLUMN_MASKS[6]) != 0
    else:
        return ((friendlyPawns & COLUMN_MASKS[index - 1]) | (friendlyPawns & COLUMN_MASKS[index + 1])) != 0

def getIsolatedPawnsCount(friendlyPawns):
    count = 0
    for i in range(len(COLUMN_MASKS)):
        pawnsInThisFile = COLUMN_MASKS[i] & friendlyPawns
        if((pawnsInThisFile != 0) and (not areTherePawnsInAdjancentFiles(i,friendlyPawns))):
            count += count_ones(pawnsInThisFile)
    return count


        
            