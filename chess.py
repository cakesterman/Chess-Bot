import pygame, sys
import chess_rules

class Chess(object):

    class Chess_Pieces(object):

        # self.image = ''

        def __init__(self, image, name, id, player):

            self.image = image
            self.name = name
            self.id = id
            self.is_first_move = True
            self.player = player

        def get_image(self):

            return self.image

        def get_name(self):

            return self.name

        def get_is_first_move(self):

            return self.is_first_move

        def set_first_move_false(self):

            self.is_first_move = False

        def get_player_side(self):

            return self.player

    black_rook1 = Chess_Pieces(pygame.image.load('blackRook.png'), "Black Rook", 1, 2)
    black_rook2 = Chess_Pieces(pygame.image.load('blackRook.png'), "Black Rook", 2, 2)
    black_knight1 = Chess_Pieces(pygame.image.load('blackKnight.png'), "Black Knight", 1, 2)
    black_knight2 = Chess_Pieces(pygame.image.load('blackKnight.png'), "Black Knight", 2, 2)
    black_bishop1 = Chess_Pieces(pygame.image.load('blackBishop.png'), "Black Bishop", 1, 2)
    black_bishop2 = Chess_Pieces(pygame.image.load('blackBishop.png'), "Black Bishop", 2, 2)
    black_king1 = Chess_Pieces(pygame.image.load('blackKing.png'), "Black King", 1, 2)
    black_queen1 = Chess_Pieces(pygame.image.load('blackQueen.png'), "Black Queen", 1, 2)
    black_pawn1 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 1, 2)
    black_pawn2 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 2, 2)
    black_pawn3 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 3, 2)
    black_pawn4 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 4, 2)
    black_pawn5 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 5, 2)
    black_pawn6 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 6, 2)
    black_pawn7 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 7, 2)
    black_pawn8 = Chess_Pieces(pygame.image.load('blackPawn.png'), "Black Pawn", 8, 2)

    white_rook1 = Chess_Pieces(pygame.image.load('whiteRook.png'), "White Rook", 1, 1)
    white_rook2 = Chess_Pieces(pygame.image.load('whiteRook.png'), "White Rook", 2, 1)
    white_knight1 = Chess_Pieces(pygame.image.load('whiteKnight.png'), "White Knight", 1, 1)
    white_knight2 = Chess_Pieces(pygame.image.load('whiteKnight.png'), "White Knight", 2, 1)
    white_bishop1 = Chess_Pieces(pygame.image.load('whiteBishop.png'), "White Bishop", 1, 1)
    white_bishop2 = Chess_Pieces(pygame.image.load('whiteBishop.png'), "White Bishop", 2, 1)
    white_king1 = Chess_Pieces(pygame.image.load('whiteKing.png'), "White King", 1, 1)
    white_queen1 = Chess_Pieces(pygame.image.load('whiteQueen.png'), "White Queen", 1, 1)
    white_pawn1 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 1, 1)
    white_pawn2 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 2, 1)
    white_pawn3 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 3, 1)
    white_pawn4 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 4, 1)
    white_pawn5 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 5, 1)
    white_pawn6 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 6, 1)
    white_pawn7 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 7, 1)
    white_pawn8 = Chess_Pieces(pygame.image.load('whitePawn.png'), "White Pawn", 8, 1)

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

    # chess_board = {(0, 0): black_rook, (1, 0): black_knight, (2, 0): black_bishop, (3, 0): black_queen,
    #                (4,  0): black_king, (5, 0): black_bishop, (6, 0): black_knight, (7, 0): black_rook,
    #                (0, 1): black_pawn1, (1, 1): black_pawn, (2, 1): black_pawn, (3, 1): black_pawn, (4, 1): black_pawn,
    #                (5, 1): black_pawn, (6, 1): black_pawn, (7, 1): black_pawn,
    #
    #                (0, 6): white_pawn, (1, 6): white_pawn, (2, 6): white_pawn, (3, 6): white_pawn, (4, 6): white_pawn,
    #                (5, 6): white_pawn, (6, 6): white_pawn, (7, 6): white_pawn, (0, 7): white_rook, (1, 7): white_knight,
    #                (2, 7): white_bishop, (3, 7): white_queen, (4, 7): white_king, (5, 7): white_bishop,
    #                (6, 7): white_knight, (7, 7): white_rook}

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


def init_board():

    global chess

    chess = Chess()

    pygame.init()

    size = width, height = 1000, 800

    global screen

    screen = pygame.display.set_mode(size)

    #board = [[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]

    # Lines are pointless after drawing boxes now, will remove later
    def draw_lines():

        x_line = 100
        y_line = 100

        for x in range(7):

            pygame.draw.line(screen, (255, 255, 255), (x_line, 0), (x_line, height))

            x_line += 100

        for y in range(7):

            pygame.draw.line(screen, (255, 255, 255), (0, y_line), (width, y_line))

            y_line += 100

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

    def init_game_pieces():

        black_pieces_list = chess.get_black_game_pieces()

        screen.blit(black_pieces_list[0][0], (25, 25))
        screen.blit(black_pieces_list[1][0], (125, 25))
        screen.blit(black_pieces_list[2][0], (225, 25))
        screen.blit(black_pieces_list[3][0], (325, 25))
        screen.blit(black_pieces_list[4][0], (425, 25))
        screen.blit(black_pieces_list[2][0], (525, 25))
        screen.blit(black_pieces_list[1][0], (625, 25))
        screen.blit(black_pieces_list[0][0], (725, 25))

        # screen.blit(black_pieces_list[6].get_image(), (25, 125))
        # screen.blit(black_pieces_list[7].get_image(), (25, 125))
        # screen.blit(black_pieces_list[6].get_image(), (25, 125))
        # screen.blit(black_pieces_list[6].get_image(), (25, 125))
        # screen.blit(black_pieces_list[6].get_image(), (25, 125))
        # screen.blit(black_pieces_list[6].get_image(), (25, 125))
        # screen.blit(black_pieces_list[6].get_image(), (25, 125))
        # screen.blit(black_pieces_list[6].get_image(), (25, 125))


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



    # Game loop
    while 1:

        # Turns

        # White goes first, then once white makes a move, black makes a move

        if chess.get_turn() == 1:

            update_turn(screen, "White's Turn")

        elif chess.get_turn() == 2:

            update_turn(screen, "Black's Turn")

        for event in pygame.event.get():

            if event.type == pygame.QUIT: sys.exit()

            if (1, 0, 0) == pygame.mouse.get_pressed():

                #print(pygame.mouse.get_pressed())

                mouse_pos = pygame.mouse.get_pos()

                board_pos = check_bounds(mouse_pos, screen)

                # if board_pos not in chess.get_chess_board().keys() or \
                #         chess.get_chess_board()[board_pos].get_player_side() == chess.get_turn():
                #
                #     print(2)
                #
                #     # print(check_bounds(mouse_pos))
                #     highlight_box(board_pos)
                #     update_board(screen)

                # if board_pos not in chess.get_chess_board().keys() :
                #
                #     print(2)
                #
                #     # print(check_bounds(mouse_pos))
                #     highlight_box(board_pos)
                #     update_board(screen)

                highlight_box(board_pos)
                update_board(screen)

        pygame.display.flip()


def update_board(screen):

    draw_game_pieces(screen)


def draw_game_pieces(screen):

    #print(chess.get_chess_board())

    for pieces in chess.get_chess_board():

        if chess.get_chess_board()[pieces] is not None:

            screen.blit(chess.get_chess_board()[pieces].get_image(), (pieces[0] * 100 + 25, pieces[1] * 100 + 25))


def update_turn(screen, player):

    WHITE = (255, 255, 255)

    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render(player, True, WHITE)

    screen.blit(text, (800, 400))


def highlight_box(box_cords):

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

        print("No pos found")

        # Breaks out of function
        return None

    # Checks if the last highlighted box is in the chess_board keys
    if chess.get_highlighted_box() in chess.get_chess_board().keys():

        # Checks if the last highlighted box value in chess_board is not None
        if chess.get_chess_board()[chess.get_highlighted_box()] is not None:

            print("Not none")

            if chess.get_chess_board()[chess.get_highlighted_box()].get_name()[0:5] == "White" and chess.get_turn() == 2:

                print("Capture White piece")

            elif chess.get_chess_board()[chess.get_highlighted_box()].get_name()[0:5] == "Black" and chess.get_turn() == 1:

                print("Capture Black piece")

            # Checks if that game piece can make that move and that it is the correct piece turn
            if chess_rules.check_valid_move(chess.get_chess_board()[chess.get_highlighted_box()].get_name(),
                                            chess.get_highlighted_box(), box_cords, chess.get_chess_board()) and \
                    chess.get_chess_board()[chess.get_highlighted_box()].get_player_side() == chess.get_turn():

                temp = chess.get_chess_board()[chess.get_highlighted_box()]

                # Sets the previous box to None
                chess.update_game_piece(chess.get_highlighted_box(), None)
                # Sets the new box to whichever piece was moving
                chess.update_game_piece(box_cords, temp)

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

            print("Is none")



    # Checks if the new box cords is different from the last, if it is, sets the last box cords to normal color
    if chess.get_highlighted_box() != box_cords and chess.get_highlighted_box() != (-1, -1):

        print(f"Un-highlighting {chess.get_highlighted_box()} and highlighting {box_cords}")

        # This makes it so you cant draw with the boxes
        highlight_box(chess.get_highlighted_box())

        # if box_deselect is True, it deselects the box after a user makes a move
        if not box_deselect:
            chess.set_highlighted_box(box_cords)

        highlight_box(box_cords)

    # Checks if user is selecting the highlighted box to unselect it
    if chess.get_highlighted_box() == box_cords:

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

    # else the user selects a different box that is not already selected
    else:

        # Setting the box to selected
        pygame.draw.rect(screen, (166, 166, 166), pygame.Rect(x_pos, y_pos, 100, 100))

        chess.set_highlighted_box(box_cords)

    #print(x_pos, y_pos)

    return box_cords

    #except:

    #    print("No value")


def check_bounds(mouse_pos, screen):

    # chess_bounds is a list of dictionaries.
    # The keys are start_pos of x, end_pos of x, start_pos of y and end_pos of y

    # (x_start, x_end, y_start, y_end): (position_name, (location_on_board))

    chess_bounds = [{(0, 99, 0, 99): ("A 8", (0, 0)), (101, 199, 0, 99): ("B 8", (1, 0)),
                     (201, 299, 0, 99): ("C 8", (2, 0)), (301, 399, 0, 99): ("D 8", (3, 0)),
                     (401, 499, 0, 99): ("E 8", (4, 0)), (501, 599, 0, 99): ("F 8", (5, 0)),
                     (601, 699, 0, 99): ("G 8", (6, 0)), (701, 800, 0, 99): ("H 8", (7, 0)),

                     (0, 99, 101, 199): ("A 7", (0, 1)), (101, 199, 101, 199): ("B 7", (1, 1)),
                     (201, 299, 101, 199): ("C 7", (2, 1)), (301, 399, 101, 199): ("Delta 7", (3, 1)),
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


init_board()
