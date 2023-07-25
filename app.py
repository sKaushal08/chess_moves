from flask import Flask, request, jsonify

app = Flask(__name__)

rows = {
    1: 'A',
    2:'B'
}
#Fuctions to determine validls moves
def get_valid_moves_knight(position):
    moves = []
    if (ord(position[0])-1 >=65 and int(position[1])+2 <=8):
        moves.append(chr(ord(position[0])-1)+str(int(position[1])+2))
    if (ord(position[0])-1 >=65 and int(position[1])-2 > 0):
        moves.append(chr(ord(position[0])-1)+str(int(position[1])-2))
    if (ord(position[0])+1 <=72 and int(position[1])+2 <=8):
        moves.append(chr(ord(position[0])+1)+str(int(position[1])+2))
    if (ord(position[0])+1 <=72 and int(position[1])-2 > 0):
        moves.append(chr(ord(position[0])+1)+str(int(position[1])-2))
    if (ord(position[0])-2 >=65 and int(position[1])+1 <=8):
        moves.append(chr(ord(position[0])-2)+str(int(position[1])+1))
    if (ord(position[0])-2 >=65 and int(position[1])-1 > 0):
        moves.append(chr(ord(position[0])-2)+str(int(position[1])-1))
    if (ord(position[0])+2 <=72 and int(position[1])+1 <=8):
        moves.append(chr(ord(position[0])+2)+str(int(position[1])+1))
    if (ord(position[0])+2 <=72 and int(position[1])-1 > 0):
        moves.append(chr(ord(position[0])+2)+str(int(position[1])-1))
    print('knight', moves)
    return moves

def get_valid_moves_bishop(position):
    moves = []
    i=1
    while(ord(position[0])-i >=65 and int(position[1])-i > 0):
        moves.append(chr(ord(position[0])-i)+str(int(position[1])-i))
        i+=1
    i=1
    while(ord(position[0])-i >=65 and int(position[1])+i <=8):
        moves.append(chr(ord(position[0])-i)+str(int(position[1])+i))
        i+=1
    i=1
    while(ord(position[0])+i <= 72 and int(position[1])-i > 0):
        moves.append(chr(ord(position[0])+i)+str(int(position[1])-i))
        i+=1
    i=1
    while(ord(position[0])+i <= 72 and int(position[1])+i <=8):
        moves.append(chr(ord(position[0])+i)+str(int(position[1])+i))
        i+=1
    return moves

def get_valid_moves_rook(position):
    moves = []
    i=1
    while(int(position[1])-i > 0):
        moves.append(position[0]+str(int(position[1])-i))
        i+=1
    i=1
    while(int(position[1])+i <=8):
        moves.append(position[0]+str(int(position[1])+i))
        i+=1
    i=1
    while(ord(position[0])-i >=65):
        moves.append(chr(ord(position[0])-i)+ position[1])
        i+=1
    i=1
    while(ord(position[0])+i <=72):
        moves.append(chr(ord(position[0])+i)+ position[1])
        i+=1    
    return moves

def get_valid_moves_queen (position):
    moves = []
    moves.extend(get_valid_moves_bishop(position))
    moves.extend(get_valid_moves_rook(position))
    return moves


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
        valid_moves = list(set(knight_moves)-invalid_moves)
    elif slug == 'bishop':
        invalid_moves = set(queen_moves).union(set(knight_moves)).union(set(rook_moves))
        valid_moves = list(set(bishop_moves)-invalid_moves)
    elif slug == 'rook':
        invalid_moves = set(queen_moves).union(set(bishop_moves)).union(set(knight_moves))
        valid_moves = list(set(rook_moves)-invalid_moves)
    elif slug == 'queen':
        invalid_moves = set(knight_moves).union(set(bishop_moves)).union(set(rook_moves))
        valid_moves = list(set(queen_moves)-invalid_moves)
    else:
        return jsonify({'error': 'Invalid slug'}), 400

    return jsonify({'valid_moves': valid_moves})


if __name__ == 'main':
    app.run(host='0.0.0.0', port = 8000)