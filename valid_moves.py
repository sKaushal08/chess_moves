#Fuctions to determine valid moves
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

def get_valid_moves_queen(position):
    moves = []
    moves.extend(get_valid_moves_bishop(position))
    moves.extend(get_valid_moves_rook(position))
    return moves