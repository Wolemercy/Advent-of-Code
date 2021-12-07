from typing import List
import numpy as np

def get_input(file: str) -> List[int]:

    with open(file, 'r') as f:
        content = f.readlines()
        numbers = [int(n) for n in content[0].split(',')]
        board_list = [[int(n) for n in b.split()] for b in content[2:] if b != '\n']
        num_boards = len(board_list) // 5
        boards = np.array(board_list).reshape(num_boards, 5, 5)

    return (numbers, boards)

class GiantSquid:

    def __init__(self, numbers, boards, first=True):
        self.boards = boards
        self.numbers = numbers
        self.first = first
        
    def giant_squid(self):
        final_score = 0
        for number in self.numbers:
            for board in self.boards:
                res = self.mark_number(board, number)
                if res and self.not_won(board) and self.check_win(board, res[0], res[1]):
                    if self.first:
                        total_unmarked = self.sum_unmarked(board)
                        final_score = total_unmarked * number
                        print(f'Part One: {final_score}')
                        return final_score
                    else:
                        total_unmarked = self.sum_unmarked(board)
                        final_score = total_unmarked * number
                        board[0][0] = -2
        
        print(f'Part Two: {final_score}')
        return final_score

    def not_won(self, board):
        if board[0][0] != -2:
            return True

    def check_win(self, board, row, col):        
        if sum(board[row]) == -5:
            return True
        
        for r in range(5):
            if board[r][col] != -1:
                return False
        return True

    def mark_number(self, board, number):
        for r in range(5):
            for c in range(5):
                if board[r][c] == number:
                    board[r][c] = -1
                    return (r, c)
        return False

    def sum_unmarked(self, board):
        result = 0
        for r in range(5):
            for c in range(5):
                if board[r][c] != -1:
                    result += board[r][c]
        return result
    

if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    part_one = GiantSquid(puzzle_input[0], puzzle_input[1], first=True)
    part_one.giant_squid()
    part_two = GiantSquid(puzzle_input[0], puzzle_input[1], first=False)
    part_two.giant_squid()
