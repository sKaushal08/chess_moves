from flask import Flask, request, jsonify
from valid_moves import *
app = Flask(__name__)


    
@app.route('/chess/<slug>', methods=['POST'])
def get_valid_moves(slug):
    data = request.get_json()
    positions = data.get('positions', {})
    knight_moves = get_valid_moves_knight(positions.get('Knight', ''))
    bishop_moves = get_valid_moves_bishop(positions.get('Bishop', ''))  
    rook_moves = get_valid_moves_rook(positions.get('Rook', ''))
    queen_moves = get_valid_moves_queen(positions.get('Queen', ''))
    
    if slug == 'knight':
        invalid_moves = set(queen_moves).union(set(bishop_moves)).union(set(rook_moves))
        valid_moves = [move for move in knight_moves if move not in invalid_moves]
    elif slug == 'bishop':
        invalid_moves = set(queen_moves).union(set(knight_moves)).union(set(rook_moves))
        valid_moves = [move for move in bishop_moves if move not in invalid_moves]
    elif slug == 'rook':
        invalid_moves = set(queen_moves).union(set(bishop_moves)).union(set(knight_moves))
        valid_moves = [move for move in rook_moves if move not in invalid_moves]
    elif slug == 'queen':
        invalid_moves = set(knight_moves).union(set(bishop_moves)).union(set(rook_moves))
        valid_moves = [move for move in queen_moves if move not in invalid_moves]
    else:
        return jsonify({'error': 'Invalid slug'}), 400

    return jsonify({'valid_moves': valid_moves})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
