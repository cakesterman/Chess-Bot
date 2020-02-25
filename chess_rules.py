
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

                            print("Invalid move, game piece {} is in the way".format(chess_board[(x, pos_to_move[1])]))
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

                            print("Invalid move, game piece {} is in the way".format(chess_board[(temp_current_pos, pos_to_move[1])]))
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

                        if (temp_current_pos, current_pos[1]) not in chess_board or chess_board[
                            (temp_current_pos, pos_to_move[1])] is None:

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

        if pos_to_move in knight_calculate_all_possible_moves(current_pos, chess_board):

            return True

        else:

            return False

    elif game_piece == "Black Bishop" or game_piece == "White Bishop":

        if pos_to_move in bishop_calculate_all_possible_moves(current_pos, chess_board):

            return True

        else:

            return False

        #print(bishop_calculate_all_possible_moves(current_pos, chess_board))

    # Temporary else for testing and moving all other game pieces
    else:

        return True


def knight_calculate_all_possible_moves(current_pos, chess_board):

    all_possible_moves = []

    def check_bounds_and_chess_board(x, y):

        if 0 <= x < 8 and 0 <= y < 8:

            if chess_board.get((x, y)) is None:

                all_possible_moves.append((x, y))

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

    return all_possible_moves


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


# test = 1
# knight_calculate_all_possible_moves((0,0), test)

