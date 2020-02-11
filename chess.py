import pygame, sys

def init_board():

    pygame.init()

    size = width, height = 800, 800

    screen = pygame.display.set_mode(size)

    board = [[1, 2, 3, 4, 5, 6, 7, 8],[1, 2, 3, 4, 5, 6, 7, 8]]

    def draw_lines():

        x_line = 100
        y_line = 100

        for x in range(7):

            pygame.draw.line(screen, (255, 255, 255), (x_line, 0), (x_line, height))

            x_line += 100

        for y in range(7):

            pygame.draw.line(screen, (255, 255, 255), (0, y_line), (width, y_line))

            y_line += 100

    draw_lines()

    while 1:

        for event in pygame.event.get():

            if event.type == pygame.QUIT: sys.exit()

            if (1, 0, 0) == pygame.mouse.get_pressed():

                print(pygame.mouse.get_pressed())

                mouse_pos = pygame.mouse.get_pos()

                print(check_bounds(mouse_pos))

        pygame.display.flip()


def check_bounds(mouse_pos):

    # chess_bounds is a list of dictionaries.
    # The keys are start_pos of x, end_pos of x, start_pos of y and end_pos of y

    # (x_start, x_end, y_start, y_end): (position_name, (location_on_board))

    chess_bounds = [{(0, 99, 0, 99): ("Alpha 8", (0, 0)), (101, 199, 0, 99): ("Bravo 8", (1, 0)),
                     (201, 299, 0, 99): ("Charlie 8", (2, 0)), (301, 399, 0, 99): ("Delta 8", (3, 0)),
                     (401, 499, 0, 99): ("Echo 8", (4, 0)), (501, 599, 0, 99): ("Foxtrot 8", (5, 0)),
                     (601, 699, 0, 99): ("Golf 8", (6, 0)), (701, 800, 0, 99): ("Hotel 8", (7, 0)),

                     (0, 99, 101, 199): "Alpha 7", (101, 199, 101, 199): "Bravo 7", (201, 299, 101, 199): "Charlie 7",
                     (301, 399, 101, 199): "Delta 7", (401, 499, 101, 199): "Echo 7", (501, 699, 101, 199): "Foxtrot 7",
                     (601, 699, 101, 199): "Golf 7", (701, 799, 101, 199): "Hotel 7"}]

    for bounds_dict in chess_bounds:

        for bounds in bounds_dict.keys():

            if bounds[0] < mouse_pos[0] < bounds[1] and bounds[2] < mouse_pos[1] < bounds[3]:

                print("We are in", bounds_dict[bounds])

                return bounds_dict[bounds][1]

        #print(item)


init_board()