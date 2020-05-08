
def check_valid_move(game_piece, current_pos, pos_to_move, chess_board):

    #rules = {"Rook": }

    print(game_piece)

    if game_piece == "Black Rook" or game_piece == "White Rook":

        if pos_to_move[0] == current_pos[0] or pos_to_move[1] == current_pos[1]:

            # If Y cord on pos_to_move equals Y cord on current_pos, we are moving horizontal
            if pos_to_move[1] == current_pos[1]:

                # Checks if we are moving to the right or left
                if pos_to_move[0] > current_pos[0]:

                    # Checks every square in x direction and checks if there is a piece blocking it.
                    # This only checks going right to left, not left to right
                    for x in range(current_pos[0] + 1, pos_to_move[0] + 1):

                        print("Checking position ({},{})".format(x, current_pos[1]))

                        if (x, current_pos[1]) not in chess_board or chess_board[(x, pos_to_move[1])] is None:

                            print("Path at ({},{}) is empty".format(x, pos_to_move[1]))

                        else:

                            print("Invalid move, game piece {} is in the way".format(chess_board[(x, pos_to_move[1])].get_name()))
                            #print(chess_board[(x, pos_to_move[1])].get_name())
                            return False

                    print("Valid move")
                    print("Moving horizontal to the right")

                    return True

                else:

                    temp_current_pos = current_pos[0] - 1

                    while pos_to_move[0] <= temp_current_pos:

                        print("Checking position ({},{})".format(temp_current_pos, current_pos[1]))

                        if (temp_current_pos, current_pos[1]) not in chess_board or chess_board[(temp_current_pos, pos_to_move[1])] is None:

                            print("Path at ({},{}) is empty".format(temp_current_pos, pos_to_move[1]))

                        else:

                            print("Invalid move, game piece {} is in the way".format( chess_board[ (temp_current_pos, pos_to_move[1]) ].get_name() ))
                            return False

                        temp_current_pos -= 1

                    return True

            else:

                # Checks if Rook is moving up or down
                if pos_to_move[1] > current_pos[1]:

                    # Checks every square in Y direction and sees if a game piece is blocking it
                    for y in range(current_pos[1] + 1, pos_to_move[1] + 1):

                        print("Checking position ({},{})".format(current_pos[0], y))

                        if (current_pos[0], y) not in chess_board or chess_board[(current_pos[0], y)] is None:

                            print("Path at ({},{}) is empty".format(current_pos[0], y))

                        else:

                            print("Invalid move, game piece {} is in the way".format(chess_board[(current_pos[0], y)]))
                            return False

                    print("Valid move")
                    print("Moving vertical")

                    return True

                else:

                    temp_current_pos = current_pos[1] - 1

                    while pos_to_move[1] <= temp_current_pos:

                        print("Checking position ({},{})".format(current_pos[0], temp_current_pos))

                        # This if statement was broken and backwards causing rooks not being able to move
                        # if (temp_current_pos, current_pos[1]) not in chess_board or chess_board[
                        #     (temp_current_pos, pos_to_move[1])] is None:
                        if (current_pos[0], temp_current_pos) not in chess_board or chess_board[
                            (current_pos[0], temp_current_pos)] is None:

                            print("Path at ({},{}) is empty".format(temp_current_pos, pos_to_move[1]))

                        else:

                            print("Invalid move, game piece {} is in the way".format(
                                chess_board[(temp_current_pos, pos_to_move[1])]))
                            return False

                        temp_current_pos -= 1

                    return True

        else:

            return False

    elif game_piece == "Black Knight" or game_piece == "White Knight":

        moves, captures = knight_calculate_all_possible_moves(current_pos, chess_board)

        print(f"Can capture {captures}")

        if pos_to_move in moves:

            return True

        elif pos_to_move in captures:

            print("Capturing")

            return True

        else:

            return False

    elif game_piece == "Black Bishop" or game_piece == "White Bishop":

        if pos_to_move in bishop_calculate_all_possible_moves(current_pos, chess_board):

            return True

        else:

            return False

        #print(bishop_calculate_all_possible_moves(current_pos, chess_board))

    elif game_piece == "Black Queen" or game_piece == "White Queen":

        if pos_to_move in queen_calculate_all_possible_moves(current_pos, chess_board):

            return True

        else:

            return False

    elif game_piece == "Black King" or game_piece == "White King":

        if pos_to_move in king_calculate_all_possible_moves(current_pos, chess_board):

            return True

        else:

            return False

    elif game_piece == "Black Pawn" or game_piece == "White Pawn":

        if pos_to_move in pawn_calculate_all_possible_moves(current_pos, chess_board):

            chess_board[current_pos].set_first_move_false()

            return True

        else:

            return False

    # Temporary else for testing and moving all other game pieces
    else:

        return True


def knight_calculate_all_possible_moves(current_pos, chess_board):

    player = chess_board.get(current_pos).get_player_side()

    all_possible_moves = []
    all_possible_captures = []

    def check_bounds_and_chess_board(x, y):

        if 0 <= x < 8 and 0 <= y < 8:

            if chess_board.get((x, y)) is None:

                all_possible_moves.append((x, y))

            elif chess_board.get((x, y)).get_player_side() != player:

                all_possible_captures.append((x, y))

    for x in range(8):

        for y in range(8):

            if x == (current_pos[0] - 1) and y == (current_pos[1] + 2):

                check_bounds_and_chess_board(x, y)

            elif x == (current_pos[0] + 1) and y == (current_pos[1] + 2):

                check_bounds_and_chess_board(x, y)

            elif x == (current_pos[0] - 1) and y == (current_pos[1] - 2):

                check_bounds_and_chess_board(x, y)

            elif x == (current_pos[0] + 1) and y == (current_pos[1] - 2):

                check_bounds_and_chess_board(x, y)

            elif x == (current_pos[0] - 2) and y == (current_pos[1] + 1):

                check_bounds_and_chess_board(x, y)

            elif x == (current_pos[0] - 2) and y == (current_pos[1] - 1):

                check_bounds_and_chess_board(x, y)

            elif x == (current_pos[0] + 2) and y == (current_pos[1] + 1):

                check_bounds_and_chess_board(x, y)

            elif x == (current_pos[0] + 2) and y == (current_pos[1] - 1):

                check_bounds_and_chess_board(x, y)

    print(all_possible_captures)

    return all_possible_moves, all_possible_captures


def bishop_calculate_all_possible_moves(current_pos, chess_board):

    all_possible_moves = []

    def search_left_down_diagonally():

        x = current_pos[0]
        y = current_pos[1]

        possible = True
        while possible:

            x -= 1
            y += 1

            if chess_board.get((x, y)) is None:

                if x == 0 or y == 7:
                    possible = False

                #print("At location ({}, {})".format(x, y))

                all_possible_moves.append((x, y))

            else:

                possible = False

    def search_right_down_diagonally():

        x = current_pos[0]
        y = current_pos[1]

        possible = True
        while possible:

            x += 1
            y += 1

            if chess_board.get((x, y)) is None:

                if x == 7 or y == 7:
                    possible = False

                #print("At location ({}, {})".format(x, y))

                all_possible_moves.append((x, y))

            else:

                possible = False

    def search_left_up_diagonally():

        x = current_pos[0]
        y = current_pos[1]

        possible = True
        while possible:

            x -= 1
            y -= 1

            if chess_board.get((x, y)) is None:

                if x == 0 or y == 0:
                    possible = False

                #print("At location ({}, {})".format(x, y))

                all_possible_moves.append((x, y))

            else:

                possible = False

    def search_right_up_diagonally():

        x = current_pos[0]
        y = current_pos[1]

        possible = True
        while possible:

            x += 1
            y -= 1

            if chess_board.get((x, y)) is None:

                if x == 7 or y == 0:
                    possible = False

                #print("At location ({}, {})".format(x, y))

                all_possible_moves.append((x, y))

            else:

                possible = False

    if current_pos[1] == 0:

        if current_pos[0] > 0:

            # Search left down diagonally
            search_left_down_diagonally()

        if current_pos[0] < 7:

            # Search right down diagonally
            search_right_down_diagonally()

    else:

        if current_pos[1] == 7 and 0 < current_pos[0] < 7:

            search_left_up_diagonally()
            search_right_up_diagonally()

        else:

            if current_pos[0] > 0:

                search_left_down_diagonally()
                search_right_down_diagonally()
                search_left_up_diagonally()
                search_right_up_diagonally()

        if current_pos[0] == 0 and current_pos[1] < 7:

            search_right_up_diagonally()
            search_right_down_diagonally()

        if current_pos[0] == 7 and current_pos[1] < 7:

            search_left_up_diagonally()
            search_left_down_diagonally()

    return all_possible_moves


def queen_calculate_all_possible_moves(current_pos, chess_board):

    all_possible_moves = []

    all_possible_moves.extend(bishop_calculate_all_possible_moves(current_pos, chess_board))

    def search_down():

        x = current_pos[0]
        y = current_pos[1]

        possible = True
        while possible:

            y += 1

            if chess_board.get((x, y)) is None:

                if y == 7:

                    possible = False

                all_possible_moves.append((x, y))

            else:

                possible = False

    def search_up():

        x = current_pos[0]
        y = current_pos[1]

        possible = True
        while possible:

            y -= 1

            if chess_board.get((x, y)) is None:

                if y == 0:
                    possible = False

                all_possible_moves.append((x, y))

            else:

                possible = False

    def search_left():

        x = current_pos[0]
        y = current_pos[1]

        possible = True
        while possible:

            x -= 1

            if chess_board.get((x, y)) is None:

                if x == 0:
                    possible = False

                all_possible_moves.append((x, y))

            else:

                possible = False

    def search_right():

        x = current_pos[0]
        y = current_pos[1]

        possible = True
        while possible:

            x += 1

            if chess_board.get((x, y)) is None:

                if x == 7:
                    possible = False

                all_possible_moves.append((x, y))

            else:

                possible = False

    if current_pos[1] == 0 and 0 < current_pos[0] < 7:

        search_down()
        search_left()
        search_right()

    if current_pos[1] == 0 and current_pos[0] == 0:

        search_right()
        search_down()

    if current_pos[1] == 0 and current_pos[0] == 7:

        search_left()
        search_down()

    if current_pos[1] == 7 and 0 < current_pos[0] < 7:

        search_up()
        search_left()
        search_right()

    if current_pos[1] == 7 and current_pos[0] == 0:

        search_right()
        search_up()

    if current_pos[1] == 7 and current_pos[0] == 7:

        search_left()
        search_up()

    if 0 < current_pos[1] < 7 and 0 < current_pos[0] < 7:

        search_right()
        search_left()
        search_up()
        search_down()

    print(all_possible_moves)
    return all_possible_moves


def king_calculate_all_possible_moves(current_pos, chess_board):

    all_possible_moves = []

    def search_down():

        all_possible_moves.append((current_pos[0], (current_pos[1] + 1)))

    def search_up():

        all_possible_moves.append((current_pos[0], (current_pos[1] - 1)))

    def search_left():

        all_possible_moves.append((current_pos[0] - 1, current_pos[1]))

    def search_right():

        all_possible_moves.append((current_pos[0] + 1, current_pos[1]))

    def search_left_up_diagonally():

        all_possible_moves.append((current_pos[0] - 1, current_pos[1] - 1))

    def search_left_down_diagonally():

        all_possible_moves.append((current_pos[0] - 1, current_pos[1] + 1))

    def search_right_up_diagonally():

        all_possible_moves.append((current_pos[0] + 1, current_pos[1] - 1))

    def search_right_down_diagonally():

        all_possible_moves.append((current_pos[0] + 1, current_pos[1] + 1))

    # y == 0 and 0 < x < 7
    if current_pos[1] == 0 and 0 < current_pos[0] < 7:

        search_down()
        search_left()
        search_right()
        search_left_down_diagonally()
        search_right_down_diagonally()

    if current_pos[1] == 0 and current_pos[0] == 0:

        search_right()
        search_down()
        search_right_down_diagonally()

    if current_pos[1] == 0 and current_pos[0] == 7:

        search_left()
        search_down()
        search_left_down_diagonally()

    if current_pos[1] == 7 and 0 < current_pos[0] < 7:

        search_up()
        search_left()
        search_right()
        search_left_up_diagonally()
        search_right_up_diagonally()

    if current_pos[1] == 7 and current_pos[0] == 0:

        search_right()
        search_up()
        search_right_up_diagonally()

    if current_pos[1] == 7 and current_pos[0] == 7:

        search_left()
        search_up()
        search_left_up_diagonally()

    if 0 < current_pos[1] < 7 and 0 < current_pos[0] < 7:

        search_right()
        search_left()
        search_up()
        search_down()
        search_right_up_diagonally()
        search_left_up_diagonally()
        search_left_down_diagonally()
        search_right_down_diagonally()

    return all_possible_moves

def pawn_calculate_all_possible_moves(current_pos, chess_board):

    all_possible_moves = []

    x = current_pos[0]
    y = current_pos[1]

    # If this is pawns first move, it can move two spaces
    if chess_board[current_pos].get_is_first_move():

        if y == 1:

            all_possible_moves.append((x, y + 2))

        if y == 6:

            all_possible_moves.append((x, y - 2))

    if chess_board[current_pos].get_name()[0:5] == "Black":

        all_possible_moves.append((x, y + 1))

    # else pawn is a white piece
    else:

        all_possible_moves.append((x, y - 1))

    return all_possible_moves

# test = 1
# knight_calculate_all_possible_moves((0,0), test)

