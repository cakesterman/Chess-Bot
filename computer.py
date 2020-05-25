import chess
import chess_rules
import random


class computer(object):

    def __init__(self, name):

        self.name = name
        self.game_pieces = {}



    def get_name(self):

        return self.name

    def set_game_pieces(self, game_pieces_list):

        for x in game_pieces_list:

            self.game_pieces[x] = [x.get_pos(), x.get_id()]

    def get_game_pieces(self):

        return self.game_pieces

    def find_game_piece(self, game_piece):

        return self.get_game_pieces().get(game_piece)

    def update_game_piece(self, game_obj, new_pos):

        self.game_pieces[game_obj] = new_pos

    def remove_game_piece(self, game_obj):

        self.game_pieces.pop(game_obj)

def make_move(computer):

    if computer.get_name() == "White":

        game_piece_list = []

        all_possible_moves_white = []
        all_possible_captures_white = []

        for game_piece in chess.chess.get_chess_board():

            if chess.chess.get_chess_board().get(game_piece) is not None and \
                    chess.chess.get_chess_board().get(game_piece).get_player_side() == 1:

                game_piece_list.append(game_piece)

        valid_choice = False

        while not valid_choice:

            random_game_piece = game_piece_list[random.randrange(len(game_piece_list))]

            # print(random_game_piece)

            _, moves, captures = chess_rules.check_valid_move(
                chess.chess.get_chess_board().get(random_game_piece).get_name(), random_game_piece, "",
                chess.chess.get_chess_board())

            if len(moves) > 0 or len(captures) > 0:

                valid_choice = True

        # print(f"DEBUG: {len(moves)}")

        if len(moves) > 0:
            random_move = moves[random.randrange(len(moves))]
        else:
            random_move = captures[random.randrange(len(captures))]


        #all_possible_moves_white.extend(moves)
        #all_possible_captures_white.extend(captures)


        # if len(all_possible_captures_white) > 0:
        #
        #     choice2 = random.randrange(len(captures))
        #
        #     if random.randrange(1) == 0:
        #
        #         return moves[choice1]
        #
        #     else:
        #
        #         return captures[choice2]

        # print("Returning")
        return random_game_piece, random_move

    else:

        game_piece_list = []

        # all_possible_moves_black = []
        # all_possible_captures_black = []

        for game_piece in chess.chess.get_chess_board():

            if chess.chess.get_chess_board().get(game_piece) is not None and \
                    chess.chess.get_chess_board().get(game_piece).get_player_side() == 2:
                # print(chess.chess.get_chess_board().get(game_piece).get_name())

                game_piece_list.append(game_piece)

        valid_choice = False

        while not valid_choice:

            random_game_piece = game_piece_list[random.randrange(len(game_piece_list))]

            # print(random_game_piece)

            _, moves, captures = chess_rules.check_valid_move(
                chess.chess.get_chess_board().get(random_game_piece).get_name(), random_game_piece, "",
                chess.chess.get_chess_board())

            if len(moves) > 0 or len(captures) > 0:
                valid_choice = True

        if len(moves) > 0:
            random_move = moves[random.randrange(len(moves))]
        else:
            random_move = captures[random.randrange(len(captures))]

        # all_possible_moves_white.extend(moves)
        # all_possible_captures_white.extend(captures)

        # choice1 = random.randrange(len(moves))
        #
        # if len(captures) > 0:
        #
        #     choice2 = random.randrange(len(captures))
        #
        #     if random.randrange(1) == 0:
        #
        #         return moves[choice1]
        #
        #     else:
        #
        #         return captures[choice2]

        # print("Returning")
        return random_game_piece, random_move


def move_king(computer):

    print("Move King")

    if computer.get_name() == "White":

        # Probably would be best to have a method that always know where the kings position is

        king_pos = (-1, -1)

        king_moves = []
        king_captures = []

        all_possible_black_moves = []
        all_possible_black_captures = []

        # Finds the position of the king and gets its moves and captures
        for game_piece in chess.chess.get_chess_board():

            if chess.chess.get_chess_board().get(game_piece) is not None and \
                    chess.chess.get_chess_board().get(game_piece).get_player_side() == 1:

                if chess.chess.get_chess_board().get(game_piece).get_name() == "White King":

                    _, moves, captures = chess_rules.check_valid_move(
                        chess.chess.get_chess_board().get(game_piece).get_name(), game_piece, "",
                        chess.chess.get_chess_board())

                    king_moves.extend(moves)
                    king_captures.extend(captures)

                    king_pos = game_piece

                    break

        # This gets all enemy moves and captures
        for game_piece in chess.chess.get_chess_board():

            if chess.chess.get_chess_board().get(game_piece) is not None and \
                    chess.chess.get_chess_board().get(game_piece).get_player_side() == 2:

                _, moves, captures = chess_rules.check_valid_move(
                    chess.chess.get_chess_board().get(game_piece).get_name(), game_piece, "",
                    chess.chess.get_chess_board())

                all_possible_black_moves.extend(moves)
                all_possible_black_captures.extend(captures)

        best_possible_moves = []

        # This chooses the best move to go to
        for x in king_captures:

            if x not in all_possible_black_captures and all_possible_black_moves and \
                    chess.chess.get_chess_board().get(x).get_name() != "Black King":

                best_possible_moves.append(x)

        for x in king_moves:

            if x not in all_possible_black_captures and all_possible_black_moves:

                best_possible_moves.append(x)

        random_move = best_possible_moves[random.randrange(len(best_possible_moves))]

        return king_pos, random_move

    elif computer.get_name() == "Black":

        king_pos = (-1, -1)

        king_moves = []
        king_captures = []

        all_possible_white_moves = []
        all_possible_white_captures = []

        # Finds the position of the king and gets its moves and captures
        for game_piece in chess.chess.get_chess_board():

            if chess.chess.get_chess_board().get(game_piece) is not None and \
                    chess.chess.get_chess_board().get(game_piece).get_player_side() == 2:

                if chess.chess.get_chess_board().get(game_piece).get_name() == "Black King":
                    _, moves, captures = chess_rules.check_valid_move(
                        chess.chess.get_chess_board().get(game_piece).get_name(), game_piece, "",
                        chess.chess.get_chess_board())

                    king_moves.extend(moves)
                    king_captures.extend(captures)

                    king_pos = game_piece

                    break

        # This gets all enemy moves and captures
        for game_piece in chess.chess.get_chess_board():

            if chess.chess.get_chess_board().get(game_piece) is not None and \
                    chess.chess.get_chess_board().get(game_piece).get_player_side() == 1:
                _, moves, captures = chess_rules.check_valid_move(
                    chess.chess.get_chess_board().get(game_piece).get_name(), game_piece, "",
                    chess.chess.get_chess_board())

                all_possible_white_moves.extend(moves)
                all_possible_white_captures.extend(captures)

        best_possible_moves = []

        # This chooses the best move to go to
        for x in king_captures:

            if x not in all_possible_white_captures and all_possible_white_moves and \
                    chess.chess.get_chess_board().get(x).get_name() != "White King":

                best_possible_moves.append(x)

        for x in king_moves:

            if x not in all_possible_white_captures and all_possible_white_moves:
                best_possible_moves.append(x)

        random_move = best_possible_moves[random.randrange(len(best_possible_moves))]

        return king_pos, random_move


def move_pawn(computer):

    # Check all pawns and see all possible pawn positions
    # Needs to return the pawn to move(pawn position) and the location that it is moving to

    pawn_list = []

    all_possible_pawn_positions = {}
    # {pawn object : [{moves: pawn object}]}
    all_possible_pawn_captures = {}
    # {pawn object : [{captures: pawn object}]}

    # This puts all of the pawns in a list for later use
    for key, value in computer.get_game_pieces().items():

        # Checks if the id is a pawn value
        if 9 <= value[1] <= 16:

            pawn_list.append(key)

    for pawn in pawn_list:

        _, moves, captures = chess_rules.check_valid_move(
            pawn.get_name(), computer.get_game_pieces().get(pawn)[0], "",
            chess.chess.get_chess_board())

        # This stupid shit always makes a generator object and I dont know how to work with that
        #all_possible_pawn_positions[pawn] = [{(x for x in moves): pawn}]

        for move in moves:

            all_possible_pawn_positions[pawn] = [{move: pawn}]

        for capture in captures:

            all_possible_pawn_positions[pawn] = [capture]

        print(f"{pawn.get_name()} at pos {computer.get_game_pieces().get(pawn)[0]} moves are: {moves}")

    print(all_possible_pawn_positions)
    print(all_possible_pawn_captures)

    if len(all_possible_pawn_captures) != 0:

        highest_value = 0
        highest_enemy_piece_value = {}
        # highest_enemy_piece_value = {pos: [value, pawn object]}

        for key, value in all_possible_pawn_captures.items():

            # Get value of enemy game piece, decide if it is worth capturing their piece

            if len(value) > 1:

                for x in value:

                    enemy_piece_value = chess.chess.get_chess_board().get(x).get_value()
                    if enemy_piece_value > highest_value:
                        highest_value = enemy_piece_value
                        highest_enemy_piece_value.clear()
                        highest_enemy_piece_value[x] = [enemy_piece_value, key]

                    if enemy_piece_value == highest_value:
                        highest_enemy_piece_value[x] = [enemy_piece_value, key]

            else:

                enemy_piece_value = chess.chess.get_chess_board().get(value[0]).get_value()
                if enemy_piece_value > highest_value:

                    highest_value = enemy_piece_value
                    highest_enemy_piece_value.clear()
                    highest_enemy_piece_value[value[0]] = [enemy_piece_value, key]

                if enemy_piece_value == highest_value:

                    highest_enemy_piece_value[value[0]] = [enemy_piece_value, key]

        # Since pawns have the lowest value, usually it is worth it to capture enemy piece.  If enemy piece is a pawn
        # making sure that you are not trading pieces could be important

        if len(highest_enemy_piece_value) > 1:

            print("Multiple options for capturing, add stuff here later")

        else:

            return computer.get_game_pieces().get(x for x in highest_enemy_piece_value.keys())

