# chess_moves
Infilect

|- app.py contains POST api function to determine valid moves of slug provided based on given pieces position information 
|- valid_moves.py contains the fuctions for every possible moves of a slug: knight, rook, bishop, and queen 

positions need to be passed in Json body like: {"positions": {"Queen": "A5", "Bishop": "G8", "Rook": "H5", "Knight": "G4"}}
endpoint: /chess/<slug>
port: 8000

sample cURL: 
curl --location 'http://localhost:8000/chess/queen' \
--header 'Content-Type: application/json' \
--data '{"positions": {"Queen": "A5", "Bishop": "G8", "Rook": "H5", "Knight": "G4"}}'

response of above curl:
{"valid_moves":["B4","C3","D2","E1","B6","C7","D8","A4","A3","A1","A6","A7","A8","H5"]}