import sys
import aocd

DAY = {{DAY}}
YEAR = {{YEAR}}

def part_a(input_data):
    # Your solution for Part A
    pass

def part_b(input_data):
    # Your solution for Part B
    pass

def submit(answer, part):
    # Submit using aocd
    aocd.submit(answer, day=DAY, year=YEAR, part=part)

if __name__ == '__main__':
    input_data = aocd.get_data(day=DAY, year=YEAR).strip()

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
