import sys

def count_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    print(f'Rows={rows}, Cols={cols}')
    word_len = len(word)
    xmas_locs = {}

    # Directions: (dx, dy) for right, down, left, up, diagonals
    directions = [
        (1, -1), # down-left
        (-1, 1), # up-right
        (1, 1),  # down-right
        (-1, -1) # up-left
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols-1):
            x = -1
            y = -1
            for dx, dy in directions:
                found = True
                for k in range(word_len):
                    nr, nc = r + k * dx, c + k * dy
                    if k == 1:
                        x = nr
                        y = nc
                    if not (is_valid(nr, nc) and grid[nr][nc] == word[k]):
                        found = False
                        break
                if found:
                    loc = f'x={x},y={y}'
                    z = xmas_locs.get(loc, 0)
                    xmas_locs[loc] = z + 1

    return xmas_locs

grid = []
# Word to find
word = "MAS"

with open(sys.argv[1], 'r') as infile:
    grid = infile.readlines()

xmas_locs = count_word(grid, word)
print(f"The word '{word}' appears {len(xmas_locs)} times.")

count = 0
for xmas in xmas_locs.values():
    if xmas < 2:
        continue
    if xmas == 2:
        count += 1
    else:
        print(f'unexpected value: {xmas}')
print(f'X-MAS appears {count} times')