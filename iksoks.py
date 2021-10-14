"""
igraci unose naizmjenicno oznake X i O
pobjednik je igrac koji spoji 4 ista znaka u nizu
program analizira nakon svakog unosa da li postoji pobjednik
"""

gameboard = [
["","","",""],
["","","",""],
["","","",""],
["","","",""]
]

def gameboard_print(gameboard):
    print(gameboard[0])
    print(gameboard[1])
    print(gameboard[2])
    print(gameboard[3])

def check_winner(gameboard):
    if gameboard[0][0] == gameboard[0][1] == gameboard[0][2] == gameboard[0][3] != "" or \
            gameboard[1][0] == gameboard[1][1] == gameboard[1][2] == gameboard[1][3]  != "" or \
                gameboard[2][0] == gameboard[2][1] == gameboard[2][2] == gameboard[2][3]  != "" or \
                    gameboard[3][0] == gameboard[3][1] == gameboard[3][2] == gameboard[3][3]  != "" or \
                        gameboard[0][0] == gameboard[1][0] == gameboard[2][0] == gameboard[3][0]  != "" or \
                            gameboard[0][1] == gameboard[1][1] == gameboard[2][1] == gameboard[3][1]  != "" or \
                                gameboard[0][2] == gameboard[1][2] == gameboard[2][2] == gameboard[3][2]  != "" or \
                                    gameboard[0][3] == gameboard[1][3] == gameboard[2][3] == gameboard[3][3]  != "" or \
                                        gameboard[0][0] == gameboard[1][1] == gameboard[2][2] == gameboard[3][3]  != "" or \
                                            gameboard[0][3] == gameboard[1][2] == gameboard[2][1] == gameboard[3][0] != "" :
        return True
    else:
        return False

turn = "X"
i = 0
j = 0
game_end = False

while not game_end: 
    print("Unesite koordinate na koje upisujete znak", turn)
    i = int(input())
    j = int(input())
    while i<0 or i>3 or j<0 or j>3 or gameboard[i][j] != "":
        print("Zauzeto polje ili pogresan unos - koordinate moraju biti brojevi izmedju 0 i 3. Pokusajte ponovo")
        i = int(input())
        j = int(input())
    gameboard[i][j] = turn
    gameboard_print(gameboard)
    if check_winner(gameboard) == True:
        print("GAME OVER pobjednik je", turn)
        gameboard = [
        ["","","",""],
        ["","","",""],
        ["","","",""],
        ["","","",""]    
        ]
        gameboard_print(gameboard)
    else:
        if turn == "X":
            turn = "Y"
        else:
            turn = "X"




