
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

    # Temporary else for testing and moving all other game pieces
    else:

        return True
