import chess as chess
import chess_rules
import computer as cp
import pygame



times_to_run = 100
for game_count in range(times_to_run):

    print(f"GAME COUNT {game_count}")

    player1 = cp.computer("White")
    player2 = cp.computer("Black")

    chess.init_game(player1, player2)





    # del chess

