import sys
import re

sys.path.append('..')

from model.othello import OneDivOthello
from view import othello_view

def _will_continue(rcv):
    if rcv in ('n', 'N'):
        return False
    else:
        return True

def _input_possition(game):
    size = len(game.get_board())
    while 1:
        othello_view.put_msg(game)
        rcv = input()
        if re.match('[0-9]+', rcv) and 1 <= int(rcv) <= size:
            break
        else:
            othello_view.invalid_input_msg()
    return int(rcv)

# TODO:putをさらにカプセル化したメソッドtry_putをつくる

def run():
    game = OneDivOthello()
    while 1:
        othello_view.print_board(game)
        while 1:
            rcv = _input_possition(game)
            if game.can_put(rcv-1):
                game.put(rcv-1)
                break
            else:
                othello_view.failed_put_msg(game, rcv-1)
                if game.dose_arrive_max_mistake():
                    othello_view.max_mistake_failed_put_msg(game)
                    othello_view.continue_msg()
                    rcv = input()
                    if _will_continue(rcv):
                        game.reset()
                        break
                    else:
                        othello_view.goodbye_msg()
                        sys.exit(0)

        if game.is_filled_board():
            game.judge_winner()
            othello_view.win_msg(game)
            othello_view.continue_msg()
            rcv = input()
            if _will_continue(rcv):
                game.reset()
            else:
                othello_view.goodbye_msg()
                sys.exit(0)
