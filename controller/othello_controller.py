import sys
sys.path.append('..')

from model.othello import OneDivOthello, WHITE, BLACK, SUCCESSFUL
from view import othello_view

MAX_MISS_TIMES = 3

def _will_continue(game):
    while 1:
        othello_view.continue_msg()
        rcv = input()
        if rcv in ('y', 'Y'):
            break
        elif rcv in ('n', 'N'):
            othello_view.goodbye_msg()
            sys.exit()
        else:
            othello_view.invalid_input_msg()
    game.reset()

def run():
    game = OneDivOthello()

    # **** main loop ****
    while 1:
        board = game.get_board()
        othello_view.print_board(board)

        cnt_failed_putting = 0
        while 1:
            current_move = game.get_current_move()
            is_invalid = True
            while is_invalid:
                othello_view.put_msg(current_move)
                try:
                    rcv = int(input()) - 1
                    assert 0 <= rcv < len(board)
                except:
                    othello_view.invalid_input_msg()
                else:
                    is_invalid = False
            if game.put(rcv) == SUCCESSFUL:
                break
            else:
                cnt_failed_putting += 1
                if cnt_failed_putting == MAX_MISS_TIMES:
                    othello_view.three_times_failed_put_msg()
                    othello_view.print_board(board)
                    if current_move == WHITE:
                        othello_view.win_msg(BLACK)
                    else:
                        othello_view.win_msg(WHITE)
                    _will_continue(game)
                    break
                else:
                    othello_view.failed_put_msg(board[rcv])

        if cnt_failed_putting < MAX_MISS_TIMES:
            game.reverse(rcv)
            if game.check_full():
                winner = game.who_is_winner()
                if winner in (WHITE, BLACK):
                    othello_view.print_board(game.get_board())
                    othello_view.win_msg(winner)
                else:
                    othello_view.draw_msg()
                _will_continue(game)
