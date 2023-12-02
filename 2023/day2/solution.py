import sys
import aocd
import re

DAY = 2
YEAR = 2023

def parse_line(line):
    game_id, data = line.split(':')
    game_id = int(game_id.split()[1])
    sets = data.split(';')
    cubes = [set.strip().split(', ') for set in sets]
    return game_id, cubes

def is_game_possible(cubes, red_cubes, green_cubes, blue_cubes):
    for comb in cubes:
        red, green, blue = 0, 0, 0
        for cube in comb:
            number, color = cube.split()
            if color == 'red':
                red += int(number)
            elif color == 'green':
                green += int(number)
            elif color == 'blue':
                blue += int(number)
        
        if red > red_cubes or green > green_cubes or blue > blue_cubes:
            return False
    return True

def calc_power(cubes):
    red, green, blue = 0, 0, 0
    for comb in cubes:
        for cube in comb:
            number, color = cube.split()
            if color == 'red':
                red = max(red, int(number))
            elif color == 'green':
                green = max(green, int(number))
            elif color == 'blue':
                blue = max(blue, int(number))
    return red * blue * green

def part_a(input_data):
    possible_games_sum = 0
    lines = input_data.split('\n')

    for line in lines:
        game_id, cubes = parse_line(line)
        if is_game_possible(cubes, 12, 13, 14):
            possible_games_sum += game_id

    return possible_games_sum
    pass

def part_b(input_data):
    power_of_games = 0
    lines = input_data.split('\n')

    for line in lines:
        _, cubes = parse_line(line)
        power_of_games += calc_power(cubes)

    return power_of_games
    pass

def submit(answer, part):
    # Submit using aocd
    aocd.submit(answer, day=DAY, year=YEAR, part=part)

if __name__ == '__main__':
    input_data = open('input.txt').read()

    if len(sys.argv) > 1:
        part_to_run = sys.argv[1]
    else:
        part_to_run = 'a'  # Default to Part A if no argument is provided

    if part_to_run == 'a':
        # Solve Part A
        answer_a = part_a(input_data)
        print("Part A:", answer_a)
        submit(answer_a, 'a')

    elif part_to_run == 'b':
        # Solve Part B
        answer_b = part_b(input_data)
        print("Part B:", answer_b)
        submit(answer_b, 'b')
