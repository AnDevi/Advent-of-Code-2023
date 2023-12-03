#!/usr/bin/python3

from pathlib import Path
import re

def isPossible(colors: {}):
	return  True if colors['red'] <= 12 and colors['green'] <= 13 and colors['blue'] <= 14 else False

content = Path(Path(__file__).parent.resolve() / 'input.txt').read_text()

lines = content.splitlines()

sum_p1 = 0
sum_p2 = 0
for idx, line in enumerate(lines):
	turns = line.split(':')[1].split(';')
	passible = True
	min_bag_colors = {'red': 0, 'green': 0, 'blue': 0}
	for turn in turns:
		colors = {'red': 0, 'green': 0, 'blue': 0}
		for color in turn.split(','):
			number_color = color[1:].split(' ')
			colors[number_color[1]] += int(number_color[0])
			min_bag_colors[number_color[1]] = max(int(number_color[0]), min_bag_colors[number_color[1]])
		if not isPossible(colors):
			passible = False
	if passible:
		sum_p1 += idx + 1
	sum_p2 += min_bag_colors['red'] * min_bag_colors['green'] * min_bag_colors['blue']
			
print(f'Part 1: {sum_p1}')		
print(f'Part 2: {sum_p2}')
