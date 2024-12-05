import sys

def count_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    print(f'Rows={rows}, Cols={cols}')
    word_len = len(word)
    count = 0

    # Directions: (dx, dy) for right, down, left, up, diagonals
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (0, -1), # left
        (-1, 0), # up
        (1, 1),  # down-right
        (1, -1), # down-left
        (-1, 1), # up-right
        (-1, -1) # up-left
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                found = True
                for k in range(word_len):
                    nr, nc = r + k * dx, c + k * dy
                    if not (is_valid(nr, nc) and grid[nr][nc] == word[k]):
                        found = False
                        break
                if found:
                    count += 1
    return count

grid = []

# Word to find
word = "XMAS"

with open(sys.argv[1], 'r') as infile:
    grid = infile.readlines()

result = count_word(grid, word)
print(f"The word '{word}' appears {result} times.")
