#Uvítání, pravidla.
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

#Tato funkce ověřuje zda-li někdo z hráčů nesplňuje požadavky pro výhru. Funkce se volá po každém tahu. Pokud hráč zvítězí, hra skončí, a program se zeptá, zda-li chceme ukončit/hrát znovu.
#Tato funkce funguje pomocí if projíždí všechny možné výherní kombinace.
def win_verificator(places, player):
        if places["p1"] == player and places["p2"] == player and places["p3"] == player:
            print(f"Congratulations, the player {player}  WON!")
            return False
        elif places["p4"] == player and places["p5"] == player and places["p6"] == player:
            print(f"Congratulations, the player {player}  WON!")
            return False
        elif places["p7"] == player and places["p8"] == player and places["p9"] == player:
            print(f"Congratulations, the player {player}  WON!")
            return False
        elif places["p1"] == player and places["p4"] == player and places["p7"] == player:
            print(f"Congratulations, the player {player}  WON!")
            return False
        elif places["p2"] == player and places["p5"] == player and places["p8"] == player:
            print(f"Congratulations, the player {player}  WON!")
            return False
        elif places["p3"] == player and places["p6"] == player and places["p9"] == player:
            print(f"Congratulations, the player {player}  WON!")
            return False
        elif places["p1"] == player and places["p5"] == player and places["p9"] == player:
            print(f"Congratulations, the player {player}  WON!")
            return False
        elif places["p3"] == player and places["p5"] == player and places["p7"] == player:
            print(f"Congratulations, the player {player}  WON!")
            return False
        elif possible_moves == []:
            print("There are no more moves left, so nobody won.")
            return False
        else:
            pass

#Hlavní smyčka, která zajišťuje možnost nabídnout hráči, možnost ukončit/hrát znovu.
while True:

    #Proměnná konec slouží pro ukončení druhé smyčky while pokud se hráč rozhodne, že chce hrát znovu.
    end = 0

    #Slovník places slouží k zapisování hodnot do všech 9 políček. Defaultně v sobě nese mezeru kvůli zarovnání hrací plochy.
    places = {"p1":" ", "p2":" ", "p3":" ", "p4":" ", "p5":" ", "p6":" ", "p7":" ", "p8":" ", "p9":" "}

    #Toto je hrací plocha, konkrétně zde hráči demonstruji, jaké číslo značí které políčko.
    playing_board = """  
    Write the number of the grid where you want to place your stone.              
                +---+---+---+
                | 1 | 2 | 3 |
                +---+---+---+
                | 4 | 5 | 6 |
                +---+---+---+
                | 7 | 8 | 9 |
                +---+---+---+

    """.format(*places.values())

    #Print hrací plochy při startu nové hry
    print(playing_board)

    #Toto je list, kde jsou uloženy všechny aktuálně volné pozice na hrací ploše. Po každém úspěšném tahu se číslo, které hráč zadal, z listu odstraní pomocí .remove.
    #Díky tomuto listu hráč nemůže zvolit pole, které je již obsazené, a zároveň nemůže ani zadat cokoliv jiného než čísla od 1-9 kvůli použití if (hráčův input in possible_moves) == True.
    possible_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    #Druhá smyčka while, tato smyčka po každém dohraném kole zahajuje další kolo, dokud jeden z hráčů nevyhraje.
    while True:

        #Smyčka pro tah hráče X. Používám ji k tomu, aby potom co hráč zadá špatný input, nepřeskočila řada na dalšího hráče.
        #Smyčka iteruje dokud hráč nezadá vhodný input.
        while True:
            x = input("Player X | Please enter your move number: ")
            #Pokud tah zadaný hráčem není v listu possible_moves, vyskočí chybová hláška.
            if x not in possible_moves:
                print("This place is already taken or you've entered something else than number.")
            else:
                #Pokud byl input hráče X platný, jeho písmeno se přiřadí k příslušnému políčku.
                places[f"p{x}"] = "X"
                #Hrací deska se aktualizuje.
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
                # A číslo tahu se vymaže z listu possible_moves.
                x = possible_moves.remove(x)
                break

        #Ověření, zda-li hráč již nezvítězil. Pokud ano, vypíše se gratulace, a program se zeptá, jestli chce hráč hrát znovu, nebo ukončit program.
        x = win_verificator(places,"X")
        if x == False:
            if input("Do you want to play again?(y/n): ") == "n":
                quit()
            else:
                end = 1
                break

        #Zde probíhá totožný proces jako u hráče X, akorát pro hráče O.
        while True:
            o = input("Player O | Please enter your move number: ")
            if o not in possible_moves:
                print("This place is already taken or you've entered something else than number.")
            else:
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
                o = possible_moves.remove(o)
                break

        o = win_verificator(places,"O")
        if o == False:
            if input("Do you want to play again?(y/n): ") == "n":
                quit()
            else:
                end = 1
                break
        if end == 1:
            break

    

    

    


