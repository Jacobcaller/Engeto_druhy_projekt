print("""Welcome to Tic Tac Toe
========================================
              GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
         Let's start the game
----------------------------------------""")
places = {"p1":" ", "p2":" ", "p3":" ", "p4":" ", "p5":" ", "p6":" ", "p7":" ", "p8":" ", "p9":" "}

playing_board = """                
            +---+---+---+
            | {0:2}| {1:2}| {2:2}|
            +---+---+---+
            | {3:2}| {4:2}| {5:2}|
            +---+---+---+
            | {6:2}| {7:2}| {8:2}|
            +---+---+---+

""".format(*places.values())
print(playing_board)
while True:
    x = input("Hrac X zvoli policko: ")
    places[f"p{x}"] = "X"
    playing_board = """                
                +---+---+---+
                | {0:2}| {1:2}| {2:2}|
                +---+---+---+
                | {3:2}| {4:2}| {5:2}|
                +---+---+---+
                | {6:2}| {7:2}| {8:2}|
                +---+---+---+

    """.format(*places.values())
    print(playing_board)

    o = input("Hrac O zvoli policko: ")
    places[f"p{o}"] = "O"
    playing_board = """                
                +---+---+---+
                | {0:2}| {1:2}| {2:2}|
                +---+---+---+
                | {3:2}| {4:2}| {5:2}|
                +---+---+---+
                | {6:2}| {7:2}| {8:2}|
                +---+---+---+

    """.format(*places.values())
    print(playing_board)

    


