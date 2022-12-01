"""Solution to day 1 of Advent of Code 2022"""
from pathlib import Path

with open(Path.cwd()/'day1/input.txt', 'r', encoding='utf-8') as f:
    # Take input and break the packs up according to newline characters.
    # Two newline characters in a row indicate a delimiter between packs
    elf_packs = f.read().replace('\n', ' ').split('  ')
# Convert text to int
elf_calories = [pack.strip().split(' ') for pack in elf_packs]
elf_calories = map(lambda calories: [int(cal) for cal in calories], elf_calories)
# Find the total calories in each pack and sort in reverse order to find the packs
# with the most calories
calories_by_pack = [sum(pack) for pack in elf_calories]
calories_by_pack.sort(reverse=True)
# Answer questions 1 & 2
most_calories = max(calories_by_pack)
top3_total_calories = sum(calories_by_pack[:3])

print(f'Find the Elf carrying the most Calories. How many total Calories is that Elf carrying? {most_calories}')
print(f'Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total? {top3_total_calories}')