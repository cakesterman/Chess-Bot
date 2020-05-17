import chess
import chess_rules
import random


class computer(object):

    def __init__(self, name):

        self.name = name


    def get_name(self):

        return self.name

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