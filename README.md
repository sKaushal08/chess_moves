# chess_moves
Infilect

Docker Instructions:

for pulling the image from docker repository:

docker pull kaushal0808/chess_moves_api:latest

running image and forming container:

docker run -p 8000:8000 kaushal0808/chess_moves_api:latest


File Description:

|- app.py contains POST api function to determine valid moves of slug provided based on given pieces position information 

|- valid_moves.py contains the fuctions for every possible moves of a slug: knight, rook, bishop, and queen 


Api Information:
positions need to be passed in Json body like: {"positions": {"Queen": "A5", "Bishop": "G8", "Rook": "H5", "Knight": "G4"}}

endpoint: /chess/<slug>

port: 8000


Sample cURL: 
curl --location 'http://localhost:8000/chess/queen' \
--header 'Content-Type: application/json' \
--data '{"positions": {"Queen": "A5", "Bishop": "G8", "Rook": "H5", "Knight": "G4"}}'

response of above curl:  {"valid_moves":["B4","C3","D2","E1","B6","C7","D8","A4","A3","A1","A6","A7","A8","H5"]}

Below are provided some examples for each case:

Example1:   {"positions": {"Queen": "E7", "Bishop": "B7", "Rook":"G5", "Knight": "C3"}

slug = knight

response1: {"valid_moves":["B1","D1","A4","A2"]}

Example2:   {"positions": {"Queen": "H1", "Bishop": "B7", "Rook":"H8", "Knight": "F2"}

slug = queen

response2: {"valid_moves":["B7","H8","G1","F1","E1","C1","B1","A1"]}

Example3:   {"positions": {"Queen": "A5", "Bishop": "G8", "Rook":"H5", "Knight": "G4"}

slug = rook

response3: {"valid_moves":["H4","H3","H1","H8","A5"]}

Example4:   {"positions": {"Queen": "H3", "Bishop": "B2", "Rook":"H8", "Knight": "F2"}

slug = bishop

response4: {"valid_moves":["A1","C1","D4","E5","F6","G7"]}

Example5:   {"positions": {"Queen": "H3", "Bishop": "B2", "Rook":"H8", "Knight": "F2"}

slug = abc

response5: {"error":"Invalid slug"}


