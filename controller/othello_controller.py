import sys
import re

sys.path.append('..')

from model.othello import OneDivOthello, ErrorCodeTryPut
from view import othello_view


def _will_continue():
    while 1:
        othello_view.continue_msg()
        rcv = input()
        if rcv in ('y', 'Y'):
            return True
        elif rcv in ('n', 'N'):
            return False
        else:
            othello_view.invalid_input_msg()


def _input_possition(game):
    size = len(game.get_board())
    while 1:
        othello_view.put_msg(game)
        rcv = input()
        if re.match('[0-9]+', rcv) and 1 <= int(rcv) <= size:
            break
        else:
            othello_view.invalid_input_msg()
    return int(rcv) - 1


def run():
    game = OneDivOthello()
    while 1:
        othello_view.print_board(game)
        while 1:
            rcv = _input_possition(game)
            error_code = game.try_put(rcv)
            if error_code == ErrorCodeTryPut.SUCCESSFUL:
                break
            if error_code == ErrorCodeTryPut.FAILED:
                othello_view.failed_put_msg(game, rcv)
            if error_code == ErrorCodeTryPut.GAME_END:
                othello_view.max_mistake_failed_put_msg(game)
                if _will_continue():
                    game.reset()
                    break
                else:
                    othello_view.goodbye_msg()
                    sys.exit(0)

        if game.is_filled_board():
            othello_view.win_msg(game)
            if _will_continue():
                game.reset()
            else:
                othello_view.goodbye_msg()
                sys.exit(0)
