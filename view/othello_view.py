import sys
sys.path.append('..')

from model.othello import OneDivOthello, WHITE, BLACK, SPACE

WHITE_FIG = '白'
BLACK_FIG = '黒'
SPACE_FIG = '　'

def _convert(color):
    if color == WHITE:
        return WHITE_FIG
    if color == BLACK:
        return BLACK_FIG
    if color == SPACE:
        return SPACE_FIG

def _draw_line(dat, n):
    for _ in range(n):
        print(dat, end='')

def print_board(board):
    size = len(board)

    for i in range(len(board)):
        print('|%2d' % (i+1), end='')
    print('|')

    for _ in range(len(board)):
        print('-ー', end='')
    print('-')

    for color in board:
        print('|' + _convert(color), end='')
    print('|')

    for _ in range(len(board)):
        print('-ー', end='')
    print('-')

def win_msg(color):
    print('{}の勝利です！'.format(_convert(color)))

def draw_msg():
    print('引き分けです！')

def put_msg(color):
    print('{}の番です。どこにコマを置きますか？: '.format(_convert(color)), end='')

def failed_put_msg(color):
    print('既に{}が配置されています。再入力してください。'.format(_convert(color)))

def three_times_failed_put_msg():
    print('3回連続配置に失敗したので、失格とみなします。')

def continue_msg():
    print('ゲームを続けますか?(Y:YES  N:NO): ', end='')

def invalid_input_msg():
    print('不正な入力です。')

def goodbye_msg():
    print('またのご利用をお待ちしております^o^')
