#!/usr/bin/python3

from pathlib import Path

dir_x = [1, -1,  0,  0, -1, -1, 1,  1]
dir_y = [0,  0,  1, -1,  1, -1, 1, -1]

def grid_print(grid):
	w, h = len(grid[0]), len(grid)
	for y in range(h):
		print(''.join([str(grid[y][x]) for x in range(w)]))
	print()

def find_number(grid, x, y):
    numbers = set()
    w, h = len(grid[0]), len(grid)
    for dx, dy, in zip(dir_x, dir_y):
        cx, cy = x + dx, y + dy
        if cx < 0 or cy < 0 or cx >= w or cy >= h:
            break
        else:
            if grid[cy][cx].isdigit():
                nx = cx
                while(nx != 0 and grid[cy][nx - 1].isdigit()):
                    nx -= 1
                number = ''
                while(nx != w and grid[cy][nx].isdigit()):
                    number += grid[cy][nx]
                    nx += 1
                numbers.add((nx, int(number)))
    return list(numbers)

content = Path(Path(__file__).parent.resolve() / 'input.txt').read_text()

grid = [[num for num in line.strip()] for line in content.splitlines()]

sum_p1 = 0
sum_p2 = 0
w, h = len(grid[0]), len(grid)
for y in range(0, h - 1):
    for x in range(0, w - 1):
        if not grid[y][x].isdigit() and grid[y][x] != '.':
            numbers = find_number(grid, x, y) 
            for n in numbers:
                sum_p1 += n[1]
            if grid[y][x] == '*' and len(numbers) == 2:
                sum_p2 += numbers[0][1] * numbers[1][1]

print(f'Part 1: {sum_p1}')
print(f'Part 2: {sum_p2}')
