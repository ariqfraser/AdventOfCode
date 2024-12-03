import re

def multiply(a: str, b:str) -> int:
    return int(a) * int(b)

def part1():
    input = open('part1.txt', 'r').read()
    matches = re.findall('mul\\((\\d+),(\\d+)\\)', input)
    sum_of_mul = 0
    for num1, num2 in matches:
        sum_of_mul += multiply(num1, num2)
    print(sum_of_mul)

def part2():
    input = open('part2.txt', 'r').read()
    matches = re.findall('(do)\\(\\)|(don\'t)\\(\\)|mul\\((\\d+),(\\d+)\\)', input)
    isEnabled = True
    sum_of_mul = 0
    for do, dont, num1, num2 in matches:
        if do == 'do':
            isEnabled = True
            continue
        if dont == "don't":
            isEnabled = False
            continue
        if num1 == '' or num2 == '':
            continue
        if isEnabled:
            sum_of_mul += multiply(num1, num2)
    print(sum_of_mul)  


part2()