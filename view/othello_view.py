import sys
sys.path.append('..')

from model.othello import OneDivOthello, CellState

WHITE_FIG = '白'
BLACK_FIG = '黒'
SPACE_FIG = '　'

def _convert(player):
    if player == CellState.WHITE:
        return WHITE_FIG
    if player == CellState.BLACK:
        return BLACK_FIG
    if player == CellState.SPACE:
        return SPACE_FIG

def _draw_line(dat, n):
    for _ in range(n):
        print(dat, end='')

def print_board(game):
    board = game.get_board()
    size = len(board)
    for i in range(size):
        print('|%2d' % (i+1), end='')
    print('|')

    for _ in range(size):
        print('-ー', end='')
    print('-')

    for color in board:
        print('|' + _convert(color), end='')
    print('|')

    for _ in range(size):
        print('-ー', end='')
    print('-')

def put_msg(game):
    print('{}の番です。どこにコマを置きますか？: '.format(_convert(game.get_current_move())), end='')

def win_msg(game):
    print_board(game)
    if game.winner is not None:
        print('{}の勝利です！'.format(_convert(game.get_winner())))
    else:
        print('引き分けです！')

def failed_put_msg(game, rcv):
    board = game.get_board()
    print('既に{}が配置されています。再入力してください。'.format(_convert(board[rcv])))

def max_mistake_failed_put_msg(game):
    print('3回連続配置に失敗したので、{}は失格とみなします。'.format(_convert(game.get_current_move())))
    win_msg(game)

def continue_msg():
    print('ゲームを続けますか?(Y:YES  N:NO): ', end='')

def invalid_input_msg():
    print('不正な入力です。')

def goodbye_msg():
    print('またのご利用をお待ちしております^o^')
