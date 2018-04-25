class CellState:
    WHITE = 1
    SPACE = 0
    BLACK = -1


class ErrorCodeTryPut:
    SUCCESSFUL = 0
    FAILED = 1
    GAME_END = 2


class OneDivOthello(object):
    def __init__(self, size=16, max_mistake=3):
        self.SIZE = size
        self.MAX_MISTAKE = max_mistake
        self.board = [CellState.SPACE for _ in range(self.SIZE)]
        self.cnt_mistake = 0
        self.current_move = CellState.WHITE
        self.n_white = 0
        self.n_black = 0
        self.winner = None

    def _count(self):
        self.n_white = 0
        self.n_black = 0
        for dat in self.board:
            if dat == CellState.WHITE:
                self.n_white += 1
            if dat == CellState.BLACK:
                self.n_black += 1

    def _reverse(self, put_i):
        left_i = None
        for i_board in range(put_i - 1, -1, -1):
            if self.board[i_board] == self.current_move:
                left_i = i_board
                break
            if self.board[i_board] == CellState.SPACE:
                break

        if left_i is not None:
            for i_board in range(left_i + 1, put_i):
                self.board[i_board] *= -1

        right_i = None
        for i_board in range(put_i + 1, self.SIZE):
            if self.board[i_board] == self.current_move:
                right_i = i_board
                break
            if self.board[i_board] == CellState.SPACE:
                break

        if right_i is not None:
            for i_board in range(put_i + 1, right_i):
                self.board[i_board] *= -1

        self._count()
        self.current_move *= -1

    def try_put(self, i_board):
        if self.board[i_board] == CellState.SPACE:
            self.cnt_mistake = 0
            self.board[i_board] = self.current_move
            self._reverse(i_board)
            return ErrorCodeTryPut.SUCCESSFUL
        else:
            self.cnt_mistake += 1
            if self.cnt_mistake == self.MAX_MISTAKE:
                self.winner = self.current_move * -1
                return ErrorCodeTryPut.GAME_END
            else:
                return ErrorCodeTryPut.FAILED

    def get_board(self):
        return self.board[:]

    def get_winner(self):
        return self.winner

    def get_current_move(self):
        return self.current_move

    def reset(self):
        for i_board in range(self.SIZE):
            self.board[i_board] = CellState.SPACE
        self.current_move = CellState.WHITE
        self.n_white = 0
        self.n_black = 0
        self.cnt_mistake = 0
        self.winner = None

    def judge_winner(self):
        if self.n_white > self.n_black:
            self.winner = CellState.WHITE
        if self.n_white == self.n_black:
            self.winner = None
        if self.n_white < self.n_black:
            self.winner = CellState.BLACK

    def is_filled_board(self):
        if CellState.SPACE not in self.board:
            return True
        else:
            return False
