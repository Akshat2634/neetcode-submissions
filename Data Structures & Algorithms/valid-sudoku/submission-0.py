class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num==".":
                    continue
                
                # Check for duplicates in row, column, or box
                if num in rows[i] or num in cols[j] or num in boxes[(i//3,j//3)]:
                    return False
                
                # Add the number to row, column, and box sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i // 3, j // 3)].add(num)
        return True
        