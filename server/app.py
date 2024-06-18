from flask import Flask
from ChessEnums import Player
from ArrayToBitboard import convert2DArrayToBitboards
from DebuggingTools import board_to_2D_array
from UtilityFunctions import splitPieceIntoIndividualBitboards
from KnightMovesGenerator import generateKnightMovesCount
from BishopMovesGenerator import generateBishopMoves
import multiprocessing
import time
app = Flask(__name__)

@app.route('/')
def hello():

    


    initial_chess_board = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],  
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],   
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
        [' ', ' ', ' ', ' ', 'p', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        ['p', 'p', 'p', 'p', ' ', 'p', 'p', 'p'],  
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']   
    ]

    bitboardsObject = convert2DArrayToBitboards(initial_chess_board)
    t0 = time.time()
    computerIsUnderCheck = isComputerUnderCheckRightNow(bitboardsObject)
    topLevelChildren = None
    if(not computerIsUnderCheck):
        topLevelChildren = bitboardsObject.children(Player.COMPUTER)
    else:
        unfilteredTopLevelChildren = bitboardsObject.children(Player.COMPUTER)
        topLevelChildren = []
        for child in unfilteredTopLevelChildren:
            if(not isComputerUnderCheckRightNow(child)):
                topLevelChildren.append(child)
        if(len(topLevelChildren) == 0):
            print("Human beat you")
            return "Human won"

    results= None
    with multiprocessing.Pool() as pool:
        results = pool.map(runAlphaBetaWithDepthFour, topLevelChildren)
    maxVal = float('-inf')
    maxNode = None
    for i in range(len(topLevelChildren)):
        if(results[i] > maxVal):
            maxNode = topLevelChildren[i]
            maxVal = results[i]
    t1 = time.time()
    board_to_2D_array(maxNode)
    print(t1-t0)

    
    return "Test"


def runAlphaBetaWithDepthFour(theBitboardsObject):
    return minimaxWithAlphaBeta(theBitboardsObject, float('-inf'), float('inf'), False, 4, 4)

def isComputerUnderCheckRightNow(theBitboardsObject):
    possibleHumanMoves = theBitboardsObject.children(Player.HUMAN)
    for move in possibleHumanMoves:
        if (move.numComputerKings == 0):
            return True
    return False

    

    


# alpha = best maximizer value discovered from this and any particular ancestor node (of this node) that happened to be discovered so far
# beta = best minimizer value discovered from this and any particular ancestor node (of this node) that happened to be discovered so far
def minimaxWithAlphaBeta(node, alpha: int, beta: int, isMaximizer: bool, depth, originalDepth):
    if(depth == 0 or node.numComputerKings == 0 or node.numHumanKings == 0):
        return node.evaluate()
    if(isMaximizer):
        bestValDiscoveredSoFarForThisNode = float('-inf')
        nodeRepresentingBestVal = None
        currentAlpha = alpha
        children = node.children(Player.COMPUTER)
        if(depth == originalDepth):
            nodeRepresentingBestVal = children[0]
        for childNode in children:
            if(currentAlpha >= beta):
                break
            evaluation = minimaxWithAlphaBeta(childNode, currentAlpha, beta, False, depth - 1, originalDepth)
            currentAlpha = max(currentAlpha, evaluation)
            if(evaluation > bestValDiscoveredSoFarForThisNode):
                if(depth == originalDepth):
                    nodeRepresentingBestVal = childNode
                bestValDiscoveredSoFarForThisNode = evaluation
        if(depth == originalDepth):
            return nodeRepresentingBestVal
        return bestValDiscoveredSoFarForThisNode
    else:
        bestValDiscoveredSoFarForThisNode = float('inf')
        currentBeta = beta
        children = node.children(Player.HUMAN)
        for childNode in children:
            if(alpha >= currentBeta):
                break
            evaluation = minimaxWithAlphaBeta(childNode, alpha, currentBeta, True, depth-1, originalDepth)
            currentBeta = min(currentBeta, evaluation)
            bestValDiscoveredSoFarForThisNode = min(bestValDiscoveredSoFarForThisNode, evaluation)
        return bestValDiscoveredSoFarForThisNode



    
    

    


            
if __name__ == '__main__':
    app.run(debug=True, port=5001)
