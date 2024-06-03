from flask import Flask
from Player import Player
from BoardState import BoardState
from DebuggingTools import pretty_print_board
from ArrayToBitboard import convert2DArrayToBitboards
from KnightMovesGenerator import generateKnightMoves
from RookMovesGenerator import generateRookMoves
from BishopMovesGenerator import generateBishopMoves
app = Flask(__name__)

@app.route('/')
def hello():
    initial_chess_board = [
        ['R', 'N', 'B', 'Q', 'K', ' ', 'N', 'R'],  
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
        [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']   
    ]

    bitboardsObject = convert2DArrayToBitboards(initial_chess_board)
    generateBishopMoves(Player.COMPUTER, bitboardsObject)

    return "Test"






            
if __name__ == '__main__':
    app.run(debug=True, port=5001)
