#!/usr/bin/python3

from pathlib import Path

content = Path(Path(__file__).parent.resolve() / 'input.txt').read_text()

sum_p1 = 0

scratchcards = []
winner_price = {}

for idx, line in enumerate(content.splitlines()):
    card = line.split(': ')[1].split(' | ')
    wining_numbers = card[0].split(' ')
    your_numbers = card[1].split(' ')
    price = 0
    wins = 0
    for n in wining_numbers:
        if n in your_numbers and n.isnumeric():
            price = 1 if price == 0 else price * 2
            wins += 1
    new_cards = []
    for w in range(wins):
        new_cards.append(idx + 1 + w + 1)
    winner_price[idx + 1] = new_cards
    scratchcards.append(idx + 1)
    sum_p1 += price

print(f'Part 1: {sum_p1}')

idx = 0
while idx != len(scratchcards):
    wins = winner_price[scratchcards[idx]]
    for i, w in enumerate(wins):
        scratchcards.insert(idx + 1 + i, w)
    idx += 1

print(f'Part 2: {len(scratchcards)}')
