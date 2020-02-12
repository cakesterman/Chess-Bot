
def check_valid_move(game_piece, current_pos, pos_to_move):

    #rules = {"Rook": }

    if game_piece == "Rook":

        if pos_to_move[0] == current_pos[0] or pos_to_move[1] == current_pos[1]:

            if pos_to_move[0] > current_pos[0]:

                print("Moving horizontal")

            else:

                print("Moving vertical")

            print("Valid move")

            return True

        else:

            return False