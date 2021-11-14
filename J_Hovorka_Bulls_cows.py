import random
#Úvodní proměnné
separator = 47 * "-"
welcome = """Hello there!
{}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{}""".format(separator, separator)
print(welcome)
num_of_games = 0
num_of_tries = 0

#Smyčka pro opakování hry.
while True:

    #Přičtení jedničky za každou započatou hru
    num_of_games += 1

    #Generování náhodného čísla, které se hráč bude snažit uhodnout.
    #Pomocí smyčky while, a for jsem se ujistil, aby náhodně vygenerované číslo nemělo duplikátní číslice.
    while True:
        x = 0
        the_num = random.randrange(1000,10000)
        for i in str(the_num):
                if str(the_num).count(i) > 1:
                    x += 1
        if x == 0:
            break

    #Jednotlivé číslice jsem vedl do listu pro snadné porovnávání s proměnnou user_guess, která bude taktéž v listu.
    the_num_list = []
    for i in str(the_num):
        the_num_list.append(i)

    #Počítadlo pokusů
    guesses = 0

    #Smyčka hádání čísla
    while True:

        #Uživatel hádá číslo
        #Pomocí try/except, a if podmínek jsem zajistil, aby se do programu dostala jen čísla, která odpovídají zadání.
        guesses += 1
        try:
            user_guess = input("Enter a number: ")
        except ValueError:
            print(f"That's not a number.")
            print(separator)
            continue

        #Pomocí smyčky loop jsem zkontroloval, zda-li číslo které zadal uživatel nemá duplikátní číslice.
        x = 0
        for i in user_guess:
            if user_guess.count(i) > 1:
                x += 1
                print("Number can't have duplicate digits.")
                print(separator)
            if x == 1:
                break
        if x != 0:
            continue

        #Číslo které zadá uživatel musí mít 4 číslice, a nesmí začínat nulou
        if user_guess[0] == "0":
            print("Number can't begin with 0")
            print(separator)
            continue                      
        if len(user_guess) != 4:
            print("Number has to be 4 only digits long.")
            print(separator)
            continue
        if int(user_guess) < 0:
            print("Number has to have positive value.")
            print(separator)
            continue

        #Vyhodnocení tipu uživatele
        #Vynulování proměnných pro vypisování cows/bulls po každé iteraci.
        print(separator)
        cows = 0
        bulls = 0

        #Převod jednotlivých číslic z proměnné user_guess do listu pro snadné porovnávánís listem the_num_list.
        user_guess_list = []
        for i in user_guess:
            user_guess_list.append(i)

        #Porovnání user inputu s vygenerovaným číslem, a přiřazení bulls/cows při shodě.
        for i, num in enumerate(user_guess_list):
            if num == the_num_list[i]:
                bulls += 1
                continue
            elif num in the_num_list:
                cows += 1

        #Zjišťování zda-li user již neuhodl správné číslo, případně výpis informací o hře.
        if bulls < 4:
            if bulls == 1 and cows == 1:
                print (f"{bulls} bull, {cows} cow")
            elif bulls == 1 and (cows > 1 or cows == 0):
                print (f"{bulls} bull, {cows} cows")
            elif cows == 1 and (bulls > 1 or bulls == 0):
                print (f"{bulls} bulls, {cows} cow")
            else:
                print (f"{bulls} bulls, {cows} cows")
        else:
            num_of_tries += guesses
            if guesses < 5:
                print(f"Correct, you've guessed the right number in {guesses} guesses!")
                print(separator)
                print("That's amazing !!")
                print(separator)
                break
            elif guesses >= 5:
                print(f"Correct, you've guessed the right number in {guesses} guesses!")
                print(separator)
                print("That's average.")
                print(separator)
                break
            else:
                print(f"Correct, you've guessed the right number in {guesses} guesses!")
                print(separator)
                print("That's not so good..")
                print(separator)
                break

    #Výpis průměrného počtu pokusů potřebných pro dokočnení této hry.
    average_guesses = round(num_of_tries / num_of_games,2)
    print(f"Average number of guesses you needed to finish this game is {average_guesses}.")
    print(separator)
    
    #Dotaz zda-li chce hráč hrát znovu.
    if input("Do you want to play again? (y for yes, n for no): ")  == "n":
        break