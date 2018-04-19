WHITE = 1
SPACE = 0
BLACK = -1

SUCCESSFUL = 1
FAILED = 0

class OneDivOthello(object):
    def __init__(self, size=16):
        self.size = size
        self.board = [SPACE for _ in range(self.size)]
        self.current_move = WHITE
        self.n_white = 0
        self.n_black = 0

    def get_board(self):
        return self.board[:]

    def get_current_move(self):
        return self.current_move

    def reset(self):
        for i_board in range(self.size):
            self.board[i_board] = SPACE
        self.current_move = WHITE
        self.n_white = 0
        self.n_black = 0

    def put(self, i_board):
        if self.board[i_board] == SPACE:
            self.board[i_board] = self.current_move
            return SUCCESSFUL
        else:
            return FAILED

    def _count(self):
        self.n_white = 0
        self.n_black = 0
        for dat in self.board:
            if dat == WHITE:
                self.n_white += 1
            if dat == BLACK:
                self.n_black += 1

    def who_is_winner(self):
        if self.n_white > self.n_black:
            return WHITE
        if self.n_white < self.n_black:
            return BLACK

    def reverse(self, put_i):
        # ***** reverse *****
        left_i = None
        for i_board in range(put_i - 1, -1, -1):
            if self.board[i_board] == self.current_move:
                left_i = i_board
                break
            if self.board[i_board] == SPACE:
                break

        if left_i is not None:
            for i_board in range(left_i + 1, put_i):
                self.board[i_board] *= -1

        right_i = None
        for i_board in range(put_i + 1, self.size):
            if self.board[i_board] == self.current_move:
                right_i = i_board
                break
            if self.board[i_board] == SPACE:
                break

        if right_i is not None:
            for i_board in range(put_i + 1, right_i):
                self.board[i_board] *= -1

        self._count()
        self.current_move *= -1

    def check_full(self):
        # ***** is full? *****
        if SPACE not in self.board:
            return True
        else:
            return False
