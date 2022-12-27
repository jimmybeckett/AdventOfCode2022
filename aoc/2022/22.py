import re


class Part1Board:
    def __init__(self, board):
        self.board = board
        self.board_height = len(board)
        self.board_width = len(board[0])
        self.row = 0
        self.col = board[0].index('.')
        self.facing = 0

    def move_right(self):
        if self.col + 1 < self.board_width and self.board[self.row][self.col + 1] == '.':
            self.col += 1
        elif self.col + 1 >= self.board_width or self.board[self.row][self.col + 1] == ' ':
            for i in range(self.board_width):
                if self.board[self.row][i] == '.':
                    self.col = i
                    break
                if self.board[self.row][i] == '#':
                    break

    def move_left(self):
        if self.col - 1 >= 0 and self.board[self.row][self.col - 1] == '.':
            self.col -= 1
        elif self.col - 1 < 0 or self.board[self.row][self.col - 1] == ' ':
            for i in reversed(range(self.board_width)):
                if self.board[self.row][i] == '.':
                    self.col = i
                    break
                if self.board[self.row][i] == '#':
                    break

    def move_up(self):
        if self.row - 1 >= 0 and self.board[self.row - 1][self.col] == '.':
            self.row -= 1
        elif self.row - 1 < 0 or self.board[self.row - 1][self.col] == ' ':
            for i in reversed(range(self.board_height)):
                if self.board[i][self.col] == '.':
                    self.row = i
                    break
                if self.board[i][self.col] == '#':
                    break

    def move_down(self):
        if self.row + 1 < self.board_height and self.board[self.row + 1][self.col] == '.':
            self.row += 1
        elif self.row + 1 >= self.board_height or self.board[self.row + 1][self.col] == ' ':
            for i in range(self.board_height):
                if self.board[i][self.col] == '.':
                    self.row = i
                    break
                if self.board[i][self.col] == '#':
                    break

    def move(self, n):
        for _ in range(n):
            match self.facing:
                case 0:
                    self.move_right()
                case 1:
                    self.move_down()
                case 2:
                    self.move_left()
                case 3:
                    self.move_up()

    def turn_right(self):
        self.facing = (self.facing + 1) % 4

    def turn_left(self):
        self.facing = (self.facing - 1) % 4


class Part2Board:
    def __init__(self, board):
        self.board = board
        self.board_height = len(board)
        self.board_width = len(board[0])
        self.row = 0
        self.col = board[0].index('.')
        self.facing = 0

    def move_right(self):
        pass

    def move_left(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move(self, n):
        for _ in range(n):
            match self.facing:
                case 0:
                    self.move_right()
                case 1:
                    self.move_down()
                case 2:
                    self.move_left()
                case 3:
                    self.move_up()

    def turn_right(self):
        self.facing = (self.facing + 1) % 4

    def turn_left(self):
        self.facing = (self.facing - 1) % 4


def walk(board, path):
    for command in path:
        if type(command) == int:
            board.move(command)
        else:
            match command:
                case 'L':
                    board.turn_left()
                case 'R':
                    board.turn_right()
    return board.row, board.col, board.facing


def password(row, col, facing):
    return 1000 * (row + 1) + 4 * (col + 1) + facing


with open('scratch.txt') as f:
    board = []
    it = iter(f)
    while (line := next(it)) != '\n':
        if line != '\n':
            board.append([c if c == '.' or c == '#' else ' ' for c in line if c != '\n'])
    path = [int(c) if c[0].isdigit() else c for c in re.findall(r'\d+|[RL]', next(it))]
    board_width = max(len(row) for row in board)
    for row in board:
        row += [' '] * (board_width - len(row))

    print(password(*walk(Part1Board(board), path)))  # Part 1
    print(password(*walk(Part2Board(board), path)))  # Part 2