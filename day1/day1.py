"""Solution to day 1 of Advent of Code 2022"""
from pathlib import Path

with open(Path.cwd()/'day1/input.txt', 'r', encoding='utf-8') as f:
    elf_packs = f.read().replace('\n', ' ').split('  ')

elf_calories = [pack.strip().split(' ') for pack in elf_packs]
elf_calories = map(lambda calories: [int(cal) for cal in calories], elf_calories)
calories_by_pack = [sum(pack) for pack in elf_calories]
calories_by_pack.sort(reverse=True)
most_calories = max(calories_by_pack)
top3_total_calories = sum(calories_by_pack[:3])

print(f'Find the Elf carrying the most Calories. How many total Calories is that Elf carrying? {most_calories}')
print(f'Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total? {top3_total_calories}')