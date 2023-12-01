import sys
import aocd
import re

DAY = 1
YEAR = 2023

def convert_to_numbers(s):

    words_to_numbers = {
        'one': 'one1one',
        'two': 'two2two',
        'three': 'three3three',
        'four': 'four4four',
        'five': 'five5five',
        'six': 'six6six',
        'seven': 'seven7seven',
        'eight': 'eight8eight',
        'nine': 'nine9nine',
        'zero': 'zero0zero'
    }
 
    for key, val in words_to_numbers.items():
        s = s.replace(key, val)

    return s

def part_a(input_data):
    lines = input_data.split()
    res = 0
    for line in lines:
        num = ''
        for i in line:
            if i.isdigit():
                num += i
                break

        for i in line[::-1]:
            if i.isdigit():
                num += i
                break
        # print(num)
        res += int(num)
    return res
    

def part_b(input_data):
    input_data = convert_to_numbers(input_data)
    # print(input_data)
    return part_a(input_data)


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
