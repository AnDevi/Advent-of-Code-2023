#!/usr/bin/python3

from pathlib import Path
import re

content = Path(Path(__file__).parent.resolve() / 'input.txt').read_text()

lines = content.splitlines()
digit_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

sum_p1, sum_p2 = 0, 0
for line in lines:
	first = int(re.search(r'[0-9]', line).group())
	last = int(re.findall(r'(?s:.*)([0-9])', line)[0])
	sum_p1 += first * 10 + last

	first = re.search(r'[0-9]|one|two|three|four|five|six|seven|eight|nine', line).group()
	last = re.findall(r'(?s:.*)([0-9]|one|two|three|four|five|six|seven|eight|nine)', line)[0]
	sum_p2 += (int(first) if len(first) == 1 else digit_dict[first]) * 10 + (int(last) if len(last) == 1 else digit_dict[last])

print(f'Part 1: {sum_p1}')		
print(f'Part 2: {sum_p2}')
