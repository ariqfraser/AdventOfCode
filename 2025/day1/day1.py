import re



# # 3
# with open('./example.txt', 'r') as f:
#     lines = f.readlines()

def part1():
    with open('./part1.txt', 'r') as f:
        lines = f.readlines()
    position = 50
    zero_count = 0

    for line in lines:
        match = re.match(r'([LR])(\d+)', line.strip())
        if match:
            op, num = match.groups()
            delta = int(num) if op == 'R' else -int(num)
            position = (position + delta) % 100
            if position == 0:
                zero_count += 1

    print(f'part1: {zero_count}')

def part2():
    dial = [i for i in range(100)]
    zero_count = 0
    pos = 50
    with open('./part1.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        match = re.match(r'([LR])(\d+)', line.strip())
        if match:
            op, num = match.groups()
            steps = int(num)
            
            for _ in range(steps):
                if op == 'R':
                    pos = (pos + 1)
                    if pos == 100:
                        pos = 0
                        
                if op == 'L':
                    pos = (pos - 1)
                    if pos == -1:
                        pos = 99
                
                if pos == 0:
                    zero_count += 1
            
    print(f'part2: {zero_count}')


if __name__ == '__main__':
    part1()
    part2()