import pygame, sys
import chess_rules
import computer
import time

class Chess(object):

    class Chess_Pieces(object):

        # self.image = ''

        def __init__(self, image, name, id, player, value, pos):

            self.image = image
            self.name = name
            self.id = id
            self.is_first_move = True
            self.player = player
            self.value = value
            self.pos = pos

        def get_image(self):

            return self.image

        def get_name(self):

            return self.name

        def get_id(self):

            return self.id

        def get_is_first_move(self):

            return self.is_first_move

        def set_first_move_false(self):

            self.is_first_move = False

        def get_player_side(self):

            return self.player

        def get_value(self):

            return self.value

        def get_pos(self):

            return self.pos

        def set_pos(self, pos):

            self.pos = pos

    run = True

    black_rook1 = Chess_Pieces(pygame.image.load('blackRook.png'), "Black Rook", 1, 2, 5, (0, 0))
    black_rook2 = Chess_Pieces(pygame.image.load('blackRook.png'), "Black Rook", 2, 2, 5, (7, 0))
    black_knight1 = Chess_Pieces(pygame.image.load('blackKnight.png'), "Black Knight", 3, 2, 3, (1, 0))
    black_knight2 = Chess_Pieces(pygame.image.load('blackKnight.png'), "Black Knight", 4, 2, 3, (6, 0))
    black_bishop1 = Chess_Pieces(pygame.image.load('blackBishop.png'), "Black Bishop", 5, 2, 3, (2, 0))
    black_bishop2 = Chess_Pieces(pygame.image.load('blackBishop.png'), "Black Bishop", 6, 2, 3, (5, 0))
    black_king1 = Chess_Pieces(pygame.image.load('blackKing.png'), "Black King", 7, 2, -1, (4, 0))
    black_queen1 = Chess_Pieces(pygame.image.load('blackQueen.png'), "Black Queen", 8, 2, 9, (3, 0))
    black_pawn1 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 9, 2, 1, (0, 1))
    black_pawn2 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 10, 2, 1, (1, 1))
    black_pawn3 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 11, 2, 1, (2, 1))
    black_pawn4 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 12, 2, 1, (3, 1))
    black_pawn5 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 13, 2, 1, (4, 1))
    black_pawn6 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 14, 2, 1, (5, 1))
    black_pawn7 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 15, 2, 1, (6, 1))
    black_pawn8 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 16, 2, 1, (7, 1))

    black_pieces_obj_list = [black_rook1, black_rook2, black_knight1, black_knight2, black_bishop1, black_bishop2,
                             black_king1, black_queen1, black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5,
                             black_pawn6, black_pawn7, black_pawn8]

    white_rook1 = Chess_Pieces(pygame.image.load('whiteRook.png'), "White Rook", 1, 1, 5, (0, 7))
    white_rook2 = Chess_Pieces(pygame.image.load('whiteRook.png'), "White Rook", 2, 1, 5, (7, 7))
    white_knight1 = Chess_Pieces(pygame.image.load('whiteKnight.png'), "White Knight", 3, 1, 3, (1, 7))
    white_knight2 = Chess_Pieces(pygame.image.load('whiteKnight.png'), "White Knight", 4, 1, 3, (6, 7))
    white_bishop1 = Chess_Pieces(pygame.image.load('whiteBishop.png'), "White Bishop", 5, 1, 3, (2, 7))
    white_bishop2 = Chess_Pieces(pygame.image.load('whiteBishop.png'), "White Bishop", 6, 1, 3, (5, 7))
    white_king1 = Chess_Pieces(pygame.image.load('whiteKing.png'), "White King", 7, 1, -1, (4, 7))
    white_queen1 = Chess_Pieces(pygame.image.load('whiteQueen.png'), "White Queen", 8, 1, 9, (3, 7))
    white_pawn1 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 9, 1, 1, (0, 6))
    white_pawn2 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 10, 1, 1, (1, 6))
    white_pawn3 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 11, 1, 1, (2, 6))
    white_pawn4 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 12, 1, 1, (3, 6))
    white_pawn5 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 13, 1, 1, (4, 6))
    white_pawn6 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 14, 1, 1, (5, 6))
    white_pawn7 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 15, 1, 1, (6, 6))
    white_pawn8 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 16, 1, 1, (7, 6))

    white_pieces_obj_list = [white_rook1, white_rook2, white_knight1, white_knight2, white_bishop1, white_bishop2,
                             white_king1, white_queen1, white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5,
                             white_pawn6, white_pawn7, white_pawn8]

    highlighted_box = (-1, -1)

    # global black_rook
    # global black_knight
    # global black_bishop
    # global black_king
    # global black_queen
    # global black_pawn

    black_rook = [pygame.image.load('blackRook.png'), "Black Rook"]
    black_knight = [pygame.image.load('blackKnight.png'), "Black Knight"]
    black_bishop = [pygame.image.load('blackBishop.png'), "Black Bishop"]
    black_king = [pygame.image.load('blackKing.png'), "Black King"]
    black_queen = [pygame.image.load('blackQueen.png'), "Black Queen"]
    black_pawn = [pygame.image.load('blackPawn.png'), "Black Pawn"]

    white_rook = [pygame.image.load('whiteRook.png'), "White Rook"]
    white_knight = [pygame.image.load('whiteKnight.png'), "White Knight"]
    white_bishop = [pygame.image.load('whiteBishop.png'), "White Bishop"]
    white_queen = [pygame.image.load("whiteQueen.png"), "White Queen"]
    white_king = [pygame.image.load("whiteKing.png"), "White King"]
    white_pawn = [pygame.image.load("whitePawn.png"), "White Pawn"]

    #black_pieces = [black_rook, black_knight, black_bishop, black_queen, black_king, black_pawn]
    black_pieces = [black_rook, black_knight, black_bishop, black_queen, black_king, black_pawn]
    white_pieces = [white_rook, white_knight, white_bishop, white_queen, white_king, white_pawn]

    chess_board = {(0, 0): black_rook1, (1, 0): black_knight1, (2, 0): black_bishop1, (3, 0): black_queen1,
                   (4, 0): black_king1, (5, 0): black_bishop2, (6, 0): black_knight2, (7, 0): black_rook2,
                   (0, 1): black_pawn1, (1, 1): black_pawn2, (2, 1): black_pawn3, (3, 1): black_pawn4, (4, 1): black_pawn5,
                   (5, 1): black_pawn6, (6, 1): black_pawn7, (7, 1): black_pawn8,

                   (0, 6): white_pawn1, (1, 6): white_pawn2, (2, 6): white_pawn3, (3, 6): white_pawn4, (4, 6): white_pawn5,
                   (5, 6): white_pawn6, (6, 6): white_pawn7, (7, 6): white_pawn8, (0, 7): white_rook1, (1, 7): white_knight1,
                   (2, 7): white_bishop1, (3, 7): white_queen1, (4, 7): white_king1, (5, 7): white_bishop2,
                   (6, 7): white_knight2, (7, 7): white_rook2}

    # 1 = White, 2 = Black
    turn = 1

    def is_running(self):

        return self.run

    def end_game(self):

        self.run = False

    def get_turn(self):

        return self.turn

    def set_turn(self, player_turn):

        self.turn = player_turn

    def get_highlighted_box(self):

        return self.highlighted_box

    def set_highlighted_box(self, cords):

        self.highlighted_box = cords

    def get_chessboard_color2(self):

        return (157, 87, 27)

    def get_chessboard_color1(self):

        return (230, 204, 171)

    def get_chess_board(self):

        return self.chess_board

    def get_black_pieces_obj(self):

        return self.black_pieces_obj_list

    def remove_black_piece(self, chess_piece_object):

        self.black_pieces_obj_list.remove(chess_piece_object)

    def get_white_pieces_obj(self):

        return self.white_pieces_obj_list

    def remove_white_piece(self, chess_piece_object):

        self.white_pieces_obj_list.remove(chess_piece_object)

    def get_black_game_pieces(self):

        return self.black_pieces

    def get_white_game_pieces(self):

        return self.white_pieces

    def update_game_piece(self, cords, game_piece):

        # print(type(game_piece))

        print(f"Updating game piece")

        self.chess_board[cords] = game_piece

    def draw_black_rook(self, pos):

        screen.blit(self.black_rook, (pos[0] + 25, pos[1] + 25))


def init_game(player1, player2):

    global chess

    chess = Chess()

    pygame.init()

    # Set up everything necessary for the computer class
    player1.set_game_pieces(chess.get_white_pieces_obj())
    player2.set_game_pieces(chess.get_black_pieces_obj())

    # print(player1.get_game_pieces())
    print(computer.move_pawn(player1))

    size = width, height = 1000, 800

    global screen

    screen = pygame.display.set_mode(size)

    def init_game_pieces():

        print("Running init_game_pieces")

        black_pieces_list = chess.get_black_game_pieces()

        screen.blit(black_pieces_list[0][0], (25, 25))
        screen.blit(black_pieces_list[1][0], (125, 25))
        screen.blit(black_pieces_list[2][0], (225, 25))
        screen.blit(black_pieces_list[3][0], (325, 25))
        screen.blit(black_pieces_list[4][0], (425, 25))
        screen.blit(black_pieces_list[2][0], (525, 25))
        screen.blit(black_pieces_list[1][0], (625, 25))
        screen.blit(black_pieces_list[0][0], (725, 25))

        black_pawn_x_pos = 25
        for x in range(8):

            screen.blit(black_pieces_list[5][0], (black_pawn_x_pos, 125))
            black_pawn_x_pos += 100

        white_pieces_list = chess.get_white_game_pieces()

        screen.blit(white_pieces_list[0][0], (25, 725))
        screen.blit(white_pieces_list[1][0], (125, 725))
        screen.blit(white_pieces_list[2][0], (225, 725))
        screen.blit(white_pieces_list[3][0], (325, 725))
        screen.blit(white_pieces_list[4][0], (425, 725))
        screen.blit(white_pieces_list[2][0], (525, 725))
        screen.blit(white_pieces_list[1][0], (625, 725))
        screen.blit(white_pieces_list[0][0], (725, 725))

        white_pawn_x_pos = 25
        for x in range(8):
            screen.blit(white_pieces_list[5][0], (white_pawn_x_pos, 625))
            white_pawn_x_pos += 100


    #draw_lines()
    draw_boxes()
    init_game_pieces()

    counter = 0

    # Game loop
    while chess.is_running():

        # Turns

        # White goes first, then once white makes a move, black makes a move

        if chess.get_turn() == 1:

            update_turn(screen, "White's Turn")

            # # returns True if king in check
            # if check_for_check():
            #
            #     king_pos, random_move = computer.move_king(player1)
            #     highlight_box(king_pos)
            #     update_board(screen)
            #     highlight_box(random_move)
            #     update_board(screen)
            #     #pygame.time.wait(500)
            #
            # else:
            #
            #     random_game_piece, random_move = computer.make_move(player1)
            #     highlight_box(random_game_piece)
            #     update_board(screen)
            #     highlight_box(random_move)
            #     update_board(screen)
                #pygame.time.wait(500)
            #pygame.time.wait(1000)

        elif chess.get_turn() == 2:

            update_turn(screen, "Black's Turn")

            # returns True if king in check
            if check_for_check():

                king_pos, random_move = computer.move_king(player2)
                highlight_box(king_pos, player1, player2)
                update_board(screen)
                highlight_box(random_move, player1, player2)
                update_board(screen)

            else:

                random_game_piece, random_move = computer.make_move(player2)
                highlight_box(random_game_piece, player1, player2)
                update_board(screen)
                highlight_box(random_move, player1, player2)
                update_board(screen)

            #pygame.time.wait(1000)

        # This is if there is human interaction (Left or right mouse click)
        for event in pygame.event.get():

            if event.type == pygame.QUIT: sys.exit()

            if (1, 0, 0) == pygame.mouse.get_pressed():

                #print(pygame.mouse.get_pressed())

                mouse_pos = pygame.mouse.get_pos()

                board_pos = check_bounds(mouse_pos, screen)

                highlight_box(board_pos, player1, player2)
                update_board(screen)

                counter = 0

            # This highlights all possible moves for selected game piece
            if (0, 0, 1) == pygame.mouse.get_pressed():

                mouse_pos = pygame.mouse.get_pos()

                board_pos = check_bounds(mouse_pos, screen)

                if chess.get_chess_board().get(board_pos) is not None:

                    _, moves, captures = chess_rules.check_valid_move(chess.get_chess_board().get(board_pos).get_name(),
                                                                      board_pos, "",
                                                                      chess.get_chess_board())

                    if counter % 2 == 0:
                        highlight_all_possible_moves(moves, captures, True)
                    else:
                        highlight_all_possible_moves(moves, captures, False)

                    counter += 1

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    pygame.time.wait(5000)

        pygame.display.flip()

    # This is for after the game ends and I want to analyze to see all the shit that broke and doesnt make sense
    # press ESC to quit the game
    x = True

    while x:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    x = False

            if (0, 0, 1) == pygame.mouse.get_pressed():

                print("RMB")

                mouse_pos = pygame.mouse.get_pos()

                board_pos = check_bounds(mouse_pos, screen)

                if chess.get_chess_board().get(board_pos) is not None:

                    _, moves, captures = chess_rules.check_valid_move(
                        chess.get_chess_board().get(board_pos).get_name(),
                        board_pos, "",
                        chess.get_chess_board())

                    if counter % 2 == 0:
                        highlight_all_possible_moves(moves, captures, True)
                    else:
                        highlight_all_possible_moves(moves, captures, False)

                    counter += 1

        pygame.display.flip()




    print("GAME ENDED")


def draw_boxes():

    x_box = 0
    y_box = 0

    for y in range(8):

        for x in range(8):

            #print("Drawing box in ({},{})".format(x, y))

            #print("x_box: {}, y_box: {}".format(x_box, y_box))

            if (y % 2) == 0:

                if (x % 2) == 0:

                    pygame.draw.rect(screen, chess.get_chessboard_color1(), pygame.Rect(x_box, y_box, 100, 100))

                else:

                    pygame.draw.rect(screen, chess.get_chessboard_color2(), pygame.Rect(x_box, y_box, 100, 100))

            else:

                if (x % 2) == 0:

                    pygame.draw.rect(screen, chess.get_chessboard_color2(), pygame.Rect(x_box, y_box, 100, 100))

                else:

                    pygame.draw.rect(screen, chess.get_chessboard_color1(), pygame.Rect(x_box, y_box, 100, 100))

            x_box += 100

        x_box = 0
        y_box += 100

    for y in range(7):

        pass


def update_board(screen):

    #draw_boxes()
    draw_game_pieces(screen)

def draw_game_pieces(screen):

    #print(chess.get_chess_board())

    for pieces in chess.get_chess_board():

        if chess.get_chess_board()[pieces] is not None:

            screen.blit(chess.get_chess_board()[pieces].get_image(), (pieces[0] * 100 + 25, pieces[1] * 100 + 25))


def update_turn(screen, player):

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render(player, True, WHITE)

    pygame.display.get_surface().fill(BLACK, rect=(801, 0, 199, 800))

    screen.blit(text, (800, 400))


# Deals with highlighting(single) boxes and moving/capturing game pieces, probably should separate those
def highlight_box(box_cords, player1, player2):

    # Need error conditioning

    # Will break if the user selects a pixel such as 100, 200, 300, 400...

    # False by default to keep a box highlighted when selecting empty boxes
    box_deselect = False

    x_pos = -1
    y_pos = -1

    try:

        x_pos = box_cords[0] * 100
        y_pos = box_cords[1] * 100

    except:

        # print("No pos found")

        # Breaks out of function
        return None

    # Checks if the last highlighted box is in the chess_board keys
    if chess.get_highlighted_box() in chess.get_chess_board().keys():

        # Checks if the last highlighted box value in chess_board is not None
        if chess.get_chess_board()[chess.get_highlighted_box()] is not None:

            # print("Not none")

            is_valid_move, _, _ = chess_rules.check_valid_move(
                chess.get_chess_board()[chess.get_highlighted_box()].get_name(),
                chess.get_highlighted_box(), box_cords, chess.get_chess_board())

            # Checks if that game piece can make that move and that it is the correct piece turn
            if is_valid_move and \
                    chess.get_chess_board()[chess.get_highlighted_box()].get_player_side() == chess.get_turn():

                # if "King" in chess.get_chess_board().get(chess.get_highlighted_box()).get_name():
                #
                #     print("Check")


                # temp is the game piece that is moving
                temp = chess.get_chess_board()[chess.get_highlighted_box()]

                print(f"{temp.get_name()} moving to {box_cords}")

                if temp.get_player_side() == 1:

                    player1.update_game_piece(temp, box_cords)

                else:

                    player2.update_game_piece(temp, box_cords)

                if chess.get_chess_board().get(box_cords) is not None:

                    print(f"Capturing piece {chess.get_chess_board().get(box_cords).get_name()} ({box_cords}")

                    if player1.get_game_pieces().get(chess.get_chess_board().get(box_cords)):

                        player1.remove_game_piece(chess.get_chess_board().get(box_cords))

                    else:

                        player2.remove_game_piece(chess.get_chess_board().get(box_cords))

                # Sets the previous box to None
                chess.update_game_piece(chess.get_highlighted_box(), None)
                # Sets the new box to whichever piece was moving(temp)
                chess.update_game_piece(box_cords, temp)

                # draw_boxes() call because if highlights are left over after viewing all possible moves
                draw_boxes()

                #check_for_check()

                # Set to true to deselect box after making move
                box_deselect = True

                if chess.get_turn() == 1:

                    chess.set_turn(2)

                else:

                    chess.set_turn(1)

            else:

                print("Cant move there")

        # Else piece lands on another piece
        else:

            pass
            # print("Is none")



    # Checks if the new box cords is different from the last, if it is, sets the last box cords to normal color
    if chess.get_highlighted_box() != box_cords and chess.get_highlighted_box() != (-1, -1):

        print(chess.get_highlighted_box())

        print(f"Un-highlighting {chess.get_highlighted_box()} and highlighting {box_cords}")

        # This makes it so you cant draw with the boxes
        highlight_box(chess.get_highlighted_box(), None, None)

        # if box_deselect is True, it deselects the box after a user makes a move
        if not box_deselect:
            chess.set_highlighted_box(box_cords)

        highlight_box(box_cords, None, None)

    # Checks if user is selecting the highlighted box to unselect it
    if chess.get_highlighted_box() == box_cords:

        # moves, captures = chess_rules.check_valid_move(
        #     chess.get_chess_board().get(chess.get_highlighted_box()).get_name(), box_cords, "",
        #     chess.get_chess_board())
        #
        # highlight_all_possible_moves(moves, captures, False)

        if (box_cords[1] % 2) == 0:

            if (box_cords[0] % 2) == 0:

                pygame.draw.rect(screen, chess.get_chessboard_color1(), pygame.Rect(x_pos, y_pos, 100, 100))
                chess.set_highlighted_box((-1, -1))

            else:

                pygame.draw.rect(screen, chess.get_chessboard_color2(), pygame.Rect(x_pos, y_pos, 100, 100))
                chess.set_highlighted_box((-1, -1))

        else:

            if (box_cords[0] % 2) == 0:

                pygame.draw.rect(screen, chess.get_chessboard_color2(), pygame.Rect(x_pos, y_pos, 100, 100))
                chess.set_highlighted_box((-1, -1))

            else:

                pygame.draw.rect(screen, chess.get_chessboard_color1(), pygame.Rect(x_pos, y_pos, 100, 100))
                chess.set_highlighted_box((-1, -1))

        # _, moves, captures = chess_rules.check_valid_move(chess.get_chess_board().get(box_cords).get_name(), box_cords, "",
        #                                                chess.get_chess_board())
        #
        # highlight_all_possible_moves(moves, captures, False)



    # else the user selects a different box that is not already selected
    else:

        # Setting the box to selected
        pygame.draw.rect(screen, (166, 166, 166), pygame.Rect(x_pos, y_pos, 100, 100))

        chess.set_highlighted_box(box_cords)

        chess_piece = ""

        # Not sure if I want to use chess_rules.check_valid_move or call each piece individually

        # if chess.get_chess_board().get(box_cords) is not None:
        #
        #     chess_piece = chess.get_chess_board().get(box_cords).get_name()
        #
        # if chess_piece == "White Pawn" or chess_piece == "Black Pawn":
        #
        #     moves, captures = chess_rules.pawn_calculate_all_possible_moves(box_cords, chess.get_chess_board())
        #
        #     highlight_all_possible_moves(moves, captures)
        #
        # if chess_piece == "Black Knight" or chess_piece == "White Knight":
        #
        #     moves, captures = chess_rules.knight_calculate_all_possible_moves(box_cords, chess.get_chess_board())
        #
        #     highlight_all_possible_moves(moves, captures)

        # _, moves, captures = chess_rules.check_valid_move(chess.get_chess_board().get(box_cords).get_name(), box_cords, "",
        #                                                chess.get_chess_board())
        #
        # highlight_all_possible_moves(moves, captures, True)



    #print(x_pos, y_pos)

    return box_cords

    #except:

    #    print("No value")


# Checks if the king is in check
def check_for_check():

    # Check all pieces and see if king is in check, need to get all possible moves/captures for all pieces

    all_possible_moves_white = []
    all_possible_captures_white = []

    all_possible_moves_black = []
    all_possible_captures_black = []

    # This breaks sometimes, not sure why
    def get_kings_pos():

        black_king_pos = (-1, -1)
        white_king_pos = (-1, -1)

        for game_piece in chess.get_chess_board():

            if chess.get_chess_board().get(game_piece) is not None:

                # Sets the positions of the kings
                if chess.get_chess_board().get(game_piece).get_name() == "Black King":

                    black_king_pos = (game_piece[0], game_piece[1])

                elif chess.get_chess_board().get(game_piece).get_name() == "White King":

                    white_king_pos = (game_piece[0], game_piece[1])

        print(black_king_pos, white_king_pos)

        return black_king_pos, white_king_pos

    black_king_pos, white_king_pos = get_kings_pos()

    # This checks for checkmate
    def check_for_checkmate():

        if chess.get_turn() == 1:

            _, white_king_moves, white_king_captures = chess_rules.check_valid_move(
                "White King", white_king_pos, "", chess.get_chess_board())

            if len(white_king_moves) == 0 and len(white_king_captures) == 0:

                print("WHITE CHECKMATE, No Moves")

                return True

            else:

                for i in white_king_moves:

                    # if i in all_possible_moves_black or i in all_possible_captures_black:
                    if i in all_possible_captures_black:

                        print(f"WHITE CHECKMATE")


                        # if i in all_possible_moves_black:
                        #
                        #     for _ in range(len(all_possible_moves_black)):
                        #
                        #         print(f"WHITE CHECKMATE by {chess.get_chess_board().get(i).get_name()}")
                        #
                        # if i in all_possible_captures_black:
                        #
                        #     for _ in range(len(all_possible_captures_black)):
                        #
                        #         print(f"WHITE CHECKMATE by {chess.get_chess_board().get(i).get_name()}")

                    else:
                        return None

                print(f"White King moves: {white_king_moves}")

                # End game
                return True

        else:

            _, black_king_moves, black_king_captures = chess_rules.check_valid_move(
                "Black King", black_king_pos, "", chess.get_chess_board())

            # print(f"Black king moves: {black_king_moves}")
            # print(captures)
            # print(moves)

            if len(black_king_moves) == 0 and len(captures) == 0:

                print("BLACK CHECKMATE, No Moves")

                return True

            else:

                for i in black_king_moves:

                    #if i in all_possible_moves_white or i in all_possible_captures_black:
                    if i in all_possible_captures_black:

                        print("BLACK CHECKMATE")

                        # if i in all_possible_moves_white:
                        #
                        #     for _ in range(len(all_possible_moves_white)):
                        #         print(f"BLACK CHECKMATE by {chess.get_chess_board().get(i).get_name()}")
                        #
                        # if i in all_possible_captures_white:
                        #
                        #     for _ in range(len(all_possible_captures_white)):
                        #         print(f"BLACK CHECKMATE by {chess.get_chess_board().get(i).get_name()}")

                    else:

                        return None

                print(f"Black King moves: {black_king_moves}")

                # End game
                return True

    for game_piece in chess.get_chess_board():

        if chess.get_chess_board().get(game_piece) is not None:

            #print(f"Chess Position: {game_piece} | Chess Name: {chess.get_chess_board().get(game_piece).get_name()}")

            is_valid_move, moves, captures = chess_rules.check_valid_move(
                chess.get_chess_board()[game_piece].get_name(),
                game_piece, "", chess.get_chess_board())

            # If player is white
            if chess.get_chess_board().get(game_piece).get_player_side() == 1:

                all_possible_moves_white.extend(moves)
                all_possible_captures_white.extend(captures)

            # If player is black
            else:

                all_possible_moves_black.extend(moves)
                all_possible_captures_black.extend(captures)

            #print(captures)

            if black_king_pos in captures or white_king_pos in captures:

                # Check for checkmate at this point
                print("CHECK")

                if check_for_checkmate():
                    end_game()

                return True





    #print(f"Black King is at: {black_king_pos}")
    #print(f"White King is at: {white_king_pos}")


def highlight_all_possible_moves(moves, captures, is_highlight):

    print(f"Moves: {moves}")
    print(F"Captures: {captures}")

    def reset_box_color(box_type, x_pos, y_pos):

        if (box_type[1] % 2) == 0:

            if (box_type[0] % 2) == 0:

                pygame.draw.rect(screen, chess.get_chessboard_color1(), pygame.Rect(x_pos, y_pos, 100, 100))
                # chess.set_highlighted_box((-1, -1))

            else:

                pygame.draw.rect(screen, chess.get_chessboard_color2(), pygame.Rect(x_pos, y_pos, 100, 100))
                # chess.set_highlighted_box((-1, -1))

        else:

            if (box_type[0] % 2) == 0:

                pygame.draw.rect(screen, chess.get_chessboard_color2(), pygame.Rect(x_pos, y_pos, 100, 100))
                # chess.set_highlighted_box((-1, -1))

            else:

                pygame.draw.rect(screen, chess.get_chessboard_color1(), pygame.Rect(x_pos, y_pos, 100, 100))
                # chess.set_highlighted_box((-1, -1))

        update_board(pygame.display.get_surface())

    for move in moves:

        # print(move[0] * 100)
        # print(move[1] * 100)

        x_pos = move[0] * 100
        y_pos = move[1] * 100

        if is_highlight:

            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x_pos, y_pos, 100, 100))

        else:

            reset_box_color(move, x_pos, y_pos)

    for capture in captures:

        x_pos = capture[0] * 100
        y_pos = capture[1] * 100

        if is_highlight:

            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x_pos, y_pos, 100, 100))
            update_board(pygame.display.get_surface())

        else:

            reset_box_color(capture, x_pos, y_pos)


def check_bounds(mouse_pos, screen):

    # chess_bounds is a list of dictionaries.
    # The keys are start_pos of x, end_pos of x, start_pos of y and end_pos of y

    # (x_start, x_end, y_start, y_end): (position_name, (location_on_board))

    chess_bounds = [{(0, 99, 0, 99): ("A 8", (0, 0)), (101, 199, 0, 99): ("B 8", (1, 0)),
                     (201, 299, 0, 99): ("C 8", (2, 0)), (301, 399, 0, 99): ("D 8", (3, 0)),
                     (401, 499, 0, 99): ("E 8", (4, 0)), (501, 599, 0, 99): ("F 8", (5, 0)),
                     (601, 699, 0, 99): ("G 8", (6, 0)), (701, 800, 0, 99): ("H 8", (7, 0)),

                     (0, 99, 101, 199): ("A 7", (0, 1)), (101, 199, 101, 199): ("B 7", (1, 1)),
                     (201, 299, 101, 199): ("C 7", (2, 1)), (301, 399, 101, 199): ("D 7", (3, 1)),
                     (401, 499, 101, 199): ("E 7", (4, 1)), (501, 599, 101, 199): ("F 7", (5, 1)),
                     (601, 699, 101, 199): ("G 7", (6, 1)), (701, 799, 101, 199): ("H 7", (7, 1)),

                     (0, 99, 201, 299): ("A 6", (0, 2)), (101, 199, 201, 299): ("B 6", (1, 2)),
                     (201, 299, 201, 299): ("C 6", (2, 2)), (301, 399, 201, 299): ("D 6", (3, 2)),
                     (401, 499, 201, 299): ("E 6", (4, 2)), (501, 599, 201, 299): ("F 6", (5, 2)),
                     (601, 699, 201, 299): ("G 6", (6, 2)), (701, 799, 201, 299): ("H 6", (7, 2)),

                     (0, 99, 301, 399): ("A 5", (0, 3)), (101, 199, 301, 399): ("B 5", (1, 3)),
                     (201, 299, 301, 399): ("C 5", (2, 3)), (301, 399, 301, 399): ("D 5", (3, 3)),
                     (401, 499, 301, 399): ("E 5", (4, 3)), (501, 599, 301, 399): ("F 5", (5, 3)),
                     (601, 699, 301, 399): ("G 5", (6, 3)), (701, 799, 301, 399): ("H 5", (7, 3)),

                     (0, 99, 401, 499): ("A 4", (0, 4)), (101, 199, 401, 499): ("B 4", (1, 4)),
                     (201, 299, 401, 499): ("C 4", (2, 4)), (301, 399, 401, 499): ("D 4", (3, 4)),
                     (401, 499, 401, 499): ("E 4", (4, 4)), (501, 599, 401, 499): ("F 4", (5, 4)),
                     (601, 699, 401, 499): ("G 4", (6, 4)), (701, 799, 401, 499): ("H 4", (7, 4)),

                     (0, 99, 501, 599): ("A 3", (0, 5)), (101, 199, 501, 599): ("B 3", (1, 5)),
                     (201, 299, 501, 599): ("C 3", (2, 5)), (301, 399, 501, 599): ("D 3", (3, 5)),
                     (401, 499, 501, 599): ("E 3", (4, 5)), (501, 599, 501, 599): ("F 3", (5, 5)),
                     (601, 699, 501, 599): ("G 3", (6, 5)), (701, 799, 501, 599): ("H 3", (7, 5)),

                     (0, 99, 601, 699): ("A 2", (0, 6)), (101, 199, 601, 699): ("B 2", (1, 6)),
                     (201, 299, 601, 699): ("C 2", (2, 6)), (301, 399, 601, 699): ("D 2", (3, 6)),
                     (401, 499, 601, 699): ("E 2", (4, 6)), (501, 599, 601, 699): ("F 2", (5, 6)),
                     (601, 699, 601, 699): ("G 2", (6, 6)), (701, 799, 601, 699): ("H 2", (7, 6)),

                     (0, 99, 701, 799): ("A 1", (0, 7)), (101, 199, 701, 799): ("B 1", (1, 7)),
                     (201, 299, 701, 799): ("C 1", (2, 7)), (301, 399, 701, 799): ("D 1", (3, 7)),
                     (401, 499, 701, 799): ("E 1", (4, 7)), (501, 599, 701, 799): ("F 1", (5, 7)),
                     (601, 699, 701, 799): ("G 1", (6, 7)), (701, 799, 701, 799): ("H 1", (7, 7))
                     }]

    for bounds_dict in chess_bounds:

        for bounds in bounds_dict.keys():

            if bounds[0] < mouse_pos[0] < bounds[1] and bounds[2] < mouse_pos[1] < bounds[3]:

                white = (255, 255, 255)
                black = (0, 0, 0)

                # Fills the screen with black to reset the previous text display
                screen.fill(black, rect=(801, 0, 199, 800))

                font = pygame.font.Font('freesansbold.ttf', 30)

                text = font.render(bounds_dict[bounds][0], True, white)

                screen.blit(text, (800, 0))

                print("We are in", bounds_dict[bounds][0])

                return bounds_dict[bounds][1]

        #print(item)


def end_game():

    black = (0, 0, 0)

    font = pygame.font.Font('freesansbold.ttf', 50)

    end_game_text = font.render("GAME OVER", True, black)

    pygame.display.get_surface().blit(end_game_text, ((800 / 2), (800 / 2)))


    chess.end_game()

# init_board()
