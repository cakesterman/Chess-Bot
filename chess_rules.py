
def check_valid_move(game_piece, current_pos, pos_to_move, chess_board):

    #rules = {"Rook": }

    # print(game_piece)

    if game_piece == "Black Rook" or game_piece == "White Rook":

        moves, captures = rook_calculate_all_possible_moves(current_pos, chess_board)

        if pos_to_move in moves:

            return True, moves, captures

        elif pos_to_move in captures:

            # print("Capturing")

            return True, moves, captures

        return False, moves, captures

    elif game_piece == "Black Knight" or game_piece == "White Knight":

        moves, captures = knight_calculate_all_possible_moves(current_pos, chess_board)

        #print(f"Can capture {captures}")

        if pos_to_move in moves:

            return True, moves, captures

        elif pos_to_move in captures:

            # print("Capturing")

            return True, moves, captures

        else:

            return False, moves, captures

    elif game_piece == "Black Bishop" or game_piece == "White Bishop":

        moves, captures = bishop_calculate_all_possible_moves(current_pos, chess_board)

        if pos_to_move in moves:

            return True, moves, captures

        elif pos_to_move in captures:

            # print("Capturing")

            return True, moves, captures

        else:

            return False, moves, captures

        #print(bishop_calculate_all_possible_moves(current_pos, chess_board))

    elif game_piece == "Black Queen" or game_piece == "White Queen":

        moves, captures = queen_calculate_all_possible_moves(current_pos, chess_board)

        if pos_to_move in moves:

            return True, moves, captures

        elif pos_to_move in captures:

            return True, moves, captures

        else:

            return False, moves, captures

    elif game_piece == "Black King" or game_piece == "White King":

        moves, captures = king_calculate_all_possible_moves(current_pos, chess_board)

        if pos_to_move in moves:

            return True, moves, captures

        elif pos_to_move in captures:

            return True, moves, captures

        else:

            return False, moves, captures

    elif game_piece == "Black Pawn" or game_piece == "White Pawn":

        moves, captures = pawn_calculate_all_possible_moves(current_pos, chess_board)

        if pos_to_move in moves:

            chess_board[current_pos].set_first_move_false()

            return True, moves, captures

        elif pos_to_move in captures:

            chess_board[current_pos].set_first_move_false()

            return True, moves, captures

        else:

            return False, moves, captures

    # Temporary else for testing and moving all other game pieces
    else:

        return True


def rook_calculate_all_possible_moves(current_pos, chess_board):

    player = chess_board.get(current_pos).get_player_side()

    all_possible_moves = []
    all_possible_captures = []

    x = current_pos[0]
    y = current_pos[1]

    # New code for Rook, probably broke some shit, ill find out later

    # Checking x axis going left and right
    if 0 <= x <= 7:

        # x is between 0 and 7

        # Check x axis going left
        for index in range(x - 1, 0, -1):

            # If the position is empty, add to all_possible_moves
            if chess_board.get((index, y)) is None:

                all_possible_moves.append( (index, y) )

            # If the position is not empty and is an enemy piece, add to all_possible_captures
            elif chess_board.get((index, y)).get_player_side() != player:

                all_possible_captures.append( (index, y) )

                break

            else:

                break

        # Checking x axis going right
        for index in range(x + 1, 7):

            # If the position is empty, add to all_possible_moves
            if chess_board.get((index, y)) is None:

                all_possible_moves.append((index, y))

            # If the position is not empty and is an enemy piece, add to all_possible_captures
            elif chess_board.get((index, y)).get_player_side() != player:

                all_possible_captures.append((index, y))

                break

            else:

                break

    # Checking y axis
    if 0 <= y <= 7:

        # Check y axis going up
        for index in range(y - 1, 0, -1):

            if chess_board.get((x, index)) is None:

                all_possible_moves.append( (x, index) )

            elif chess_board.get((x, index)).get_player_side() != player:

                all_possible_captures.append((x, index))

            else:

                break

        # Check y axis going down
        for index in range(y + 1, 7):

            if chess_board.get((x, index)) is None:

                all_possible_moves.append((x, index))

            elif chess_board.get((x, index)).get_player_side() != player:

                all_possible_captures.append((x, index))

            else:

                break

    return all_possible_moves, all_possible_captures


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

    # print(all_possible_captures)

    return all_possible_moves, all_possible_captures


def bishop_calculate_all_possible_moves(current_pos, chess_board):

    player = chess_board.get(current_pos).get_player_side()

    all_possible_moves = []
    all_possible_captures = []

    def search_left_down_diagonally():

        x = current_pos[0]
        y = current_pos[1]

        possible = True
        while possible:

            x -= 1
            y += 1

            if chess_board.get((x, y)) is None:

                if x < 0 or y > 7:
                    possible = False
                    break

                #print("At location ({}, {})".format(x, y))

                all_possible_moves.append((x, y))

            elif chess_board.get((x, y)).get_player_side() != player:

                if x < 0 or y > 7:
                    possible = False
                    break

                all_possible_captures.append((x, y))
                possible = False

            else:

                possible = False

    def search_right_down_diagonally():

        x = current_pos[0]
        y = current_pos[1]

        print(y)

        possible = True
        while possible:

            x += 1
            y += 1

            # if x == 7 or y == 7:
            #     possible = False

            if chess_board.get((x, y)) is None:

                if x > 7 or y > 7:
                    possible = False
                    break

                #print("At location ({}, {})".format(x, y))

                all_possible_moves.append((x, y))

            elif chess_board.get((x, y)).get_player_side() != player:

                if x > 7 or y > 7:
                    possible = False
                    break

                all_possible_captures.append((x, y))
                possible = False

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

                if x < 0 or y < 0:
                    possible = False
                    break

                #print("At location ({}, {})".format(x, y))

                all_possible_moves.append((x, y))

            elif chess_board.get((x, y)).get_player_side() != player:

                if x < 0 or y < 0:
                    possible = False
                    break

                all_possible_captures.append((x, y))
                possible = False

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

                if x > 7 or y < 0:
                    possible = False
                    break

                #print("At location ({}, {})".format(x, y))

                all_possible_moves.append((x, y))

            elif chess_board.get((x, y)).get_player_side() != player:

                if x > 7 or y < 0:
                    possible = False
                    break

                all_possible_captures.append((x, y))
                possible = False

            else:

                possible = False

    if current_pos[1] == 0:

        if current_pos[0] > 0:

            print("Here1")

            # Search left down diagonally
            search_left_down_diagonally()

        if current_pos[0] < 7:
            print("Here2")

            # Search right down diagonally
            search_right_down_diagonally()

    else:

        if current_pos[1] == 7 and 0 < current_pos[0] < 7:

            print("Here3")
            search_left_up_diagonally()
            search_right_up_diagonally()

        else:

            if current_pos[0] > 0:
                print("Here4")

                search_left_down_diagonally()
                search_right_down_diagonally()
                search_left_up_diagonally()
                search_right_up_diagonally()

        if current_pos[0] == 0 and current_pos[1] < 7:
            print("Here5")
            search_right_up_diagonally()
            search_right_down_diagonally()

        if current_pos[0] == 7 and current_pos[1] < 7:
            print("Here6")
            search_left_up_diagonally()
            search_left_down_diagonally()

    return all_possible_moves, all_possible_captures


def queen_calculate_all_possible_moves(current_pos, chess_board):

    player = chess_board.get(current_pos).get_player_side()

    all_possible_moves = []
    all_possible_captures = []

    moves, captures = bishop_calculate_all_possible_moves(current_pos, chess_board)

    all_possible_moves.extend(moves)
    all_possible_captures.extend(captures)

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

            elif chess_board.get((x, y)).get_player_side() != player:

                if y == 7:

                    possible = False

                all_possible_captures.append((x, y))
                possible = False

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

            elif chess_board.get((x, y)).get_player_side() != player:

                if y == 0:

                    possible = False

                all_possible_captures.append((x, y))
                possible = False

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

            elif chess_board.get((x, y)).get_player_side() != player:

                if x == 0:

                    possible = False

                all_possible_captures.append((x, y))
                possible = False

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

            elif chess_board.get((x, y)).get_player_side() != player:

                if x == 7:

                    possible = False

                all_possible_captures.append((x, y))
                possible = False

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

    #print(all_possible_moves)
    return all_possible_moves, all_possible_captures


def king_calculate_all_possible_moves(current_pos, chess_board):

    player = chess_board.get(current_pos).get_player_side()

    all_possible_moves = []
    all_possible_captures = []

    x = current_pos[0]
    y = current_pos[1]

    def search_down():

        if chess_board.get((x, y + 1)) is None:

            all_possible_moves.append((current_pos[0], (current_pos[1] + 1)))

        elif chess_board.get((x, y + 1)).get_player_side() != player:

            all_possible_captures.append((x, y + 1))

    def search_up():

        if chess_board.get((x, y - 1)) is None:

            all_possible_moves.append((current_pos[0], (current_pos[1] - 1)))

        elif chess_board.get((x, y - 1)).get_player_side() != player:

            all_possible_captures.append((x, y - 1))

    def search_left():

        if chess_board.get((x - 1, y)) is None:

            all_possible_moves.append((current_pos[0] - 1, current_pos[1]))

        elif chess_board.get((x - 1, y)).get_player_side() != player:

            all_possible_captures.append((x - 1, y))

    def search_right():

        if chess_board.get((x + 1, y)) is None:

            all_possible_moves.append((current_pos[0] + 1, current_pos[1]))

        elif chess_board.get((x + 1, y)).get_player_side() != player:

            all_possible_captures.append((x + 1, y))

    def search_left_up_diagonally():

        if chess_board.get((x - 1, y - 1)) is None:

            all_possible_moves.append((current_pos[0] - 1, current_pos[1] - 1))

        elif chess_board.get((x - 1, y - 1)).get_player_side() != player:

            all_possible_captures.append((x - 1, y - 1))

    def search_left_down_diagonally():

        if chess_board.get((x - 1, y + 1)) is None:

            all_possible_moves.append((current_pos[0] - 1, current_pos[1] + 1))

        elif chess_board.get((x - 1, y + 1)).get_player_side() != player:

            all_possible_captures.append((x - 1, y + 1))


    def search_right_up_diagonally():

        if chess_board.get((x + 1, y - 1)) is None:

            all_possible_moves.append((current_pos[0] + 1, current_pos[1] - 1))

        elif chess_board.get((x + 1, y - 1)).get_player_side() != player:

            all_possible_captures.append((x + 1, y - 1))

    def search_right_down_diagonally():

        if chess_board.get((x + 1, y + 1)) is None:

            all_possible_moves.append((current_pos[0] + 1, current_pos[1] + 1))

        elif chess_board.get((x + 1, y + 1)).get_player_side() != player:

            all_possible_captures.append((x + 1, y + 1))

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

    return all_possible_moves, all_possible_captures

def pawn_calculate_all_possible_moves(current_pos, chess_board):

    player = chess_board.get(current_pos).get_player_side()

    all_possible_moves = []
    all_possible_captures = []

    x = current_pos[0]
    y = current_pos[1]

    # If this is pawns first move, it can move two spaces
    if chess_board[current_pos].get_is_first_move():

        if y == 1:

            all_possible_moves.append((x, y + 2))

        if y == 6:

            all_possible_moves.append((x, y - 2))

    if chess_board[current_pos].get_name()[0:5] == "Black":

        if chess_board.get((x, y + 1)) is None:

            all_possible_moves.append((x, y + 1))

        if chess_board.get((x - 1, y + 1)) is not None and chess_board.get((x - 1, y + 1)).get_player_side() != player:

            all_possible_captures.append((x - 1, y + 1))

        if chess_board.get((x + 1, y + 1)) is not None and chess_board.get((x + 1, y + 1)).get_player_side() != player:

            all_possible_captures.append((x + 1, y + 1))

    # else pawn is a white piece
    else:

        if chess_board.get((x, y - 1)) is None:
            all_possible_moves.append((x, y - 1))

        if chess_board.get((x - 1, y - 1)) is not None and chess_board.get((x - 1, y - 1)).get_player_side() != player:
            all_possible_captures.append((x - 1, y - 1))

        if chess_board.get((x + 1, y - 1)) is not None and chess_board.get((x + 1, y - 1)).get_player_side() != player:
            all_possible_captures.append((x + 1, y - 1))

    return all_possible_moves, all_possible_captures
