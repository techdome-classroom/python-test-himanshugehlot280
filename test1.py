import unittest  
from program1 import Solution


class Solution:
    def explore_island(self, grid, row, col, visited):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited[row][col] = True
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 'L' and not visited[r][c]:
                self.explore_island(grid, r, c, visited)

    def getTotalIsles(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L' and not visited[i][j]:
                    self.explore_island(grid, i, j, visited)
                    island_count += 1
        return island_count



class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        result = self.solution.getTotalIsles([["L","L","L","L","W"],["L","L","W","L","W"],["L","L","W","W","W"],["W","W","W","W","W"]])
        self.assertEqual(result, 1)

    def test_case2(self):
        result = self.solution.getTotalIsles([["L","L","W","W","W"],["L","L","W","W","W"],["W","W","L","W","W"],["W","W","W","L","L"]])
        self.assertEqual(result, 3)

    def test_case3(self):
        result = self.solution.getTotalIsles([["W", "W", "W", "W"], ["W", "L", "L", "W"], ["W", "L", "L", "W"], ["W", "W", "W", "W"]])
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
