import pygame, sys


class Chess(object):

    highlighted_box = (-1, -1)

    # global black_rook
    # global black_knight
    # global black_bishop
    # global black_king
    # global black_queen
    # global black_pawn

    black_rook = pygame.image.load('blackRook.png')
    black_knight = pygame.image.load('blackKnight.png')
    black_bishop = pygame.image.load('blackBishop.png')
    black_king = pygame.image.load('blackKing.png')
    black_queen = pygame.image.load('blackQueen.png')
    black_pawn = pygame.image.load('blackPawn.png')

    black_pieces = [black_rook, black_knight, black_bishop, black_queen, black_king, black_pawn]

    chess_board = {(0, 0): black_rook, (1, 0): black_knight, (2, 0): black_bishop, (3, 0): black_queen,
                   (4,  0): black_king, (5, 0): black_bishop, (6, 0): black_knight, (7, 0): black_rook,
                   (0, 1): black_pawn, (1, 1): black_pawn, (2, 1): black_pawn, (3, 1): black_pawn, (4, 1): black_pawn,
                   (5, 1): black_pawn, (6, 1): black_pawn, (7, 1): black_pawn}

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

    def draw_black_rook(self, pos):

        screen.blit(self.black_rook, (pos[0] + 25, pos[1] + 25))


def init_board():

    global chess

    chess = Chess()

    pygame.init()

    size = width, height = 800, 800

    global screen

    screen = pygame.display.set_mode(size)

    board = [[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]

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

        screen.blit(black_pieces_list[0], (25, 25))
        screen.blit(black_pieces_list[1], (125, 25))
        screen.blit(black_pieces_list[2], (225, 25))
        screen.blit(black_pieces_list[3], (325, 25))
        screen.blit(black_pieces_list[4], (425, 25))
        screen.blit(black_pieces_list[2], (525, 25))
        screen.blit(black_pieces_list[1], (625, 25))
        screen.blit(black_pieces_list[0], (725, 25))

        black_pawn_x_pos = 25
        for x in range(8):

            screen.blit(black_pieces_list[5], (black_pawn_x_pos, 125))
            black_pawn_x_pos += 100

    def draw_game_pieces():

        #print(chess.get_chess_board())

        for pieces in chess.get_chess_board():

            screen.blit(chess.get_chess_board()[pieces], (pieces[0] * 100 + 25, pieces[1] * 100 + 25))

            #print(chess.get_chess_board()[pieces])



    #draw_lines()
    draw_boxes()
    init_game_pieces()



    def update_board():

        draw_game_pieces()

    # Game loop
    while 1:

        for event in pygame.event.get():

            if event.type == pygame.QUIT: sys.exit()

            if (1, 0, 0) == pygame.mouse.get_pressed():

                #print(pygame.mouse.get_pressed())

                mouse_pos = pygame.mouse.get_pos()

                #print(check_bounds(mouse_pos))
                highlight_box(check_bounds(mouse_pos))
                update_board()

        pygame.display.flip()


def highlight_box(box_cords):

    # Need error conditioning

    # Will break if the user selects a pixel such as 100, 200, 300, 400...
    x_pos = box_cords[0] * 100
    y_pos = box_cords[1] * 100

    # Checks if the new box cords is different from the last, if it is, sets the last box cords to normal color
    if chess.get_highlighted_box() != box_cords:

        # This makes it so you cant draw with the boxes
        highlight_box(chess.get_highlighted_box())

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

    else:

        pygame.draw.rect(screen, (166, 166, 166), pygame.Rect(x_pos, y_pos, 100, 100))

        chess.set_highlighted_box(box_cords)

    print(x_pos, y_pos)

    return box_cords





def check_bounds(mouse_pos):

    # chess_bounds is a list of dictionaries.
    # The keys are start_pos of x, end_pos of x, start_pos of y and end_pos of y

    # (x_start, x_end, y_start, y_end): (position_name, (location_on_board))

    chess_bounds = [{(0, 99, 0, 99): ("Alpha 8", (0, 0)), (101, 199, 0, 99): ("Bravo 8", (1, 0)),
                     (201, 299, 0, 99): ("Charlie 8", (2, 0)), (301, 399, 0, 99): ("Delta 8", (3, 0)),
                     (401, 499, 0, 99): ("Echo 8", (4, 0)), (501, 599, 0, 99): ("Foxtrot 8", (5, 0)),
                     (601, 699, 0, 99): ("Golf 8", (6, 0)), (701, 800, 0, 99): ("Hotel 8", (7, 0)),

                     (0, 99, 101, 199): ("Alpha 7", (0, 1)), (101, 199, 101, 199): ("Bravo 7", (1, 1)),
                     (201, 299, 101, 199): ("Charlie 7", (2, 1)), (301, 399, 101, 199): ("Delta 7", (3, 1)),
                     (401, 499, 101, 199): ("Echo 7", (4, 1)), (501, 599, 101, 199): ("Foxtrot 7", (5, 1)),
                     (601, 699, 101, 199): ("Golf 7", (6, 1)), (701, 799, 101, 199): ("Hotel 7", (7, 1)),

                     (0, 99, 201, 299): ("Alpha 6", (0, 2)), (101, 199, 201, 299): ("Bravo 6", (1, 2)),
                     (201, 299, 201, 299): ("Charlie 6", (2, 2)), (301, 399, 201, 299): ("Delta 6", (3, 2)),
                     (401, 499, 201, 299): ("Echo 6", (4, 2)), (501, 599, 201, 299): ("Foxtrot", (5, 2)),
                     (601, 699, 201, 299): ("Golf 6", (6, 2)), (701, 799, 201, 299): ("Hotel 6", (7, 2)),

                     (0, 99, 301, 399): ("Alpha 5", (0, 3)), (101, 199, 301, 399): ("Bravo 5", (1, 3)),
                     (201, 299, 301, 399): ("Charlie 5", (2, 3)), (301, 399, 301, 399): ("Delta 5", (3, 3)),
                     (401, 499, 301, 399): ("Echo 5", (4, 3)), (501, 599, 301, 399): ("Foxtrot 5", (5, 3)),
                     (601, 699, 301, 399): ("Golf 5", (6, 3)), (701, 799, 301, 399): ("Hotel 5", (7, 3)),

                     (0, 99, 401, 499): ("Alpha 4", (0, 4)), (101, 199, 401, 499): ("Bravo 4", (1, 4)),
                     (201, 299, 401, 499): ("Charlie 4", (2, 4)), (301, 399, 401, 499): ("Delta 4", (3, 4)),
                     (401, 499, 401, 499): ("Echo 4", (4, 4)), (501, 599, 401, 499): ("Foxtrot 4", (5, 4)),
                     (601, 699, 401, 499): ("Golf 4", (6, 4)), (701, 799, 401, 499): ("Hotel 4", (7, 4)),

                     (0, 99, 501, 599): ("Alpha 3", (0, 5)), (101, 199, 501, 599): ("Bravo 3", (1, 5)),
                     (201, 299, 501, 599): ("Charlie 3", (2, 5)), (301, 399, 501, 599): ("Delta 3", (3, 5)),
                     (401, 499, 501, 599): ("Echo 3", (4, 5)), (501, 599, 501, 599): ("Foxtrot 3", (5, 5)),
                     (601, 699, 501, 599): ("Golf 3", (6, 5)), (701, 799, 501, 599): ("Hotel 3", (7, 5)),

                     (0, 99, 601, 699): ("Alpha 2", (0, 6)), (101, 199, 601, 699): ("Bravo 2", (1, 6)),
                     (201, 299, 601, 699): ("Charlie 2", (2, 6)), (301, 399, 601, 699): ("Delta 2", (3, 6)),
                     (401, 499, 601, 699): ("Echo 2", (4, 6)), (501, 599, 601, 699): ("Foxtrot 2", (5, 6)),
                     (601, 699, 601, 699): ("Golf 2", (6, 6)), (701, 799, 601, 699): ("Hotel 2", (7, 6)),

                     (0, 99, 701, 799): ("Alpha 1", (0, 7)), (101, 199, 701, 799): ("Bravo 1", (1, 7)),
                     (201, 299, 701, 799): ("Charlie 1", (2, 7)), (301, 399, 701, 799): ("Delta 1", (3, 7)),
                     (401, 499, 701, 799): ("Echo 1", (4, 7)), (501, 599, 701, 799): ("Foxtrot 1", (5, 7)),
                     (601, 699, 701, 799): ("Golf 1", (6, 7)), (701, 799, 701, 799): ("Hotel 1", (7, 7))
                     }]

    for bounds_dict in chess_bounds:

        for bounds in bounds_dict.keys():

            if bounds[0] < mouse_pos[0] < bounds[1] and bounds[2] < mouse_pos[1] < bounds[3]:

                print("We are in", bounds_dict[bounds])

                return bounds_dict[bounds][1]

        #print(item)


init_board()
