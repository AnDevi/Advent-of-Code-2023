#!/usr/bin/python3

from pathlib import Path

def find_locations_for_seeds(seeds: dict()):
    locations = []
    for seed in seeds:
        key = seed
        for m in maps:
            t = None
            for idx in range(len(m)):
                if idx == 0 and key < m[idx][1]:
                    t = m[idx]
                    break
                if idx == len(m) - 1:
                    t = m[idx]
                    break
                elif key >= m[idx][1] and key < m[idx + 1][1]:
                    t = m[idx]
                    break
            key += t[0] - t[1] if t[1] + t[2] > key and t[1] <= key else 0
        locations.append(key)
    return locations

def find_lowest_locations_for_seeds_ranges(seeds_ranges: dict()):
    min_ranges = []
    for r in seeds_ranges:
        ranges = [r]
        for single_map in maps:
            mapped_ranges = []
            for map_part in single_map:
                dest, src, size = map_part[0], map_part[1], map_part[2]
                diff = src - dest
                src_end = src + size         
                egde_ranges = []
                while ranges:
                    r_start, r_end = ranges.pop()

                    if max(r_start, src) < min(src_end, r_end):
                        mapped_ranges.append((max(r_start, src) - diff, min(src_end, r_end) - diff))
                        
                    if r_start < min(r_end, src):
                        egde_ranges.append((r_start, min(r_end, src)))
                    if max(src_end, r_start) < r_end:
                        egde_ranges.append((max(src_end, r_start), r_end))
                        
                ranges = egde_ranges
            ranges = mapped_ranges + ranges
        min_ranges.append(min(ranges)[0])
    return min_ranges
    

content = Path(Path(__file__).parent.resolve() / 'input.txt').read_text().split('\n\n')
seeds = [int(n) for n in content[0].split(': ')[1].split(' ')]
maps = []
for idx, a_map in enumerate(content):
    if idx == 0:
        continue
    maps.append(sorted([[int(n) for n in line.split(' ')] for line in a_map.split(':\n')[1].split('\n')], key=lambda n: int(n[1])))

seeds_ranges = list([(seeds[idx], seeds[idx] + seeds[idx + 1] - 1) for idx in range(0, len(seeds), 2)])

p1_locations = find_locations_for_seeds(seeds)
p2_ranges = find_lowest_locations_for_seeds_ranges(seeds_ranges)

print(f'Part 1: {min(p1_locations)}')
print(f'Part 2: {min(p2_ranges)}')
