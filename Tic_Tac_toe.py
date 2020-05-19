def draw_board(ls):
    print("Tic-Tac-Toe")
    print("~~~~~~~~~~~~~~")
    print("||{}||{}||{}||".format(ls[0],ls[1],ls[2]))
    print("~~~~~~~~~~~~~~")
    print("||{}||{}||{}||".format(ls[3],ls[4],ls[5]))
    print("~~~~~~~~~~~~~~")
    print("||{}||{}||{}||".format(ls[6],ls[7],ls[8]))
    print("~~~~~~~~~~~~~~")
def  get_player_input(player_char,c_list):
    while True:
        move = int(input(player_char+": Where would you like to place your piece (1 - 9): "))
        if move>0 and move<10:
            if c_list[move-1] == '_':
                return move
            else:
                print("That spot has already been chosen. Try again.")
        else:
            print("This is not a spot on the board. Try again.")

def  place_char_on_board(player_char,move,c_list):
    c_list[move-1] = player_char

def is_winner(player_char,c_list):
    return ((c_list[0]==player_char and c_list[4] == player_char and c_list[8] == player_char)or
            (c_list[2] == player_char and c_list[4] == player_char and c_list[6] == player_char)or
            (c_list[0] == player_char and c_list[1] == player_char and c_list[2] == player_char)or
            (c_list[3] == player_char and c_list[4] == player_char and c_list[5] == player_char)or
            (c_list[6] == player_char and c_list[7] == player_char and c_list[8] == player_char)or
            (c_list[0] == player_char and c_list[3] == player_char and c_list[6] == player_char)or
            (c_list[1] == player_char and c_list[4] == player_char and c_list[7] == player_char)or
            (c_list[2] == player_char and c_list[5] == player_char and c_list[8] == player_char)
            )

player1 = "X"
player2 = "O"
c_list = ['_']*9
n_list = ["1","2","3","4","5","6","7","8","9"]
draw_board(n_list)
print()
draw_board(c_list)
while True:
    player_move = get_player_input(player1,c_list)
    place_char_on_board(player1,player_move,c_list)
    draw_board(n_list)
    draw_board(c_list)
    if is_winner(player1,c_list):
        print("Congratulations! Player 1 wins!")
        break
    elif "_" not in c_list:
        print("There is a tie")
        break
    player_move = get_player_input(player2, c_list)
    place_char_on_board(player2, player_move, c_list)
    draw_board(n_list)
    draw_board(c_list)
    if is_winner(player2, c_list):
        print("Congratulations! Player 2 wins!")
        break
