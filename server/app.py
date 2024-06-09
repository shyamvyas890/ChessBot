from flask import Flask
from ChessEnums import Player
from ArrayToBitboard import convert2DArrayToBitboards
from DebuggingTools import board_to_2D_array
from UtilityFunctions import splitPieceIntoIndividualBitboards
from KnightMovesGenerator import generateKnightMovesCount
import time
app = Flask(__name__)

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

    t0 = time.time()
    score = minimaxWithAlphaBeta(bitboardsObject, float('-inf'), float('inf'), True, 4, 4)
    t1 = time.time()
    board_to_2D_array(score)
    print(t1-t0)

    
    return "Test"
    


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
