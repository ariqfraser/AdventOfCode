import re
from os import path
from typing import List


class Sorter():
    __rules = []
    __ordering_rules_obj = {}
    __patterns = []

    def gen_patterns(self):
        for key in self.__ordering_rules_obj.keys():
            regex = '.*(?='
            for i in range(len(self.__ordering_rules_obj[key])):
                regex += f'{self.__ordering_rules_obj[key][i]}{'|' if i < len(self.__ordering_rules_obj[key]) - 1 else ''}'
            regex += f').*{key}'
            self.__patterns.append(regex)

    def add_rule(self, before: int, after: int):
        self.__rules.append((before, after))
        try:
            self.__ordering_rules_obj[before].append(after)
        except:
            self.__ordering_rules_obj[before] = [after]
        
        self.gen_patterns()

    def test(self, string) -> bool:
        invalid = False
        for regex in self.__patterns:
            if invalid := re.match(regex, string) is not None:
                break
        return not invalid
    
    def __get_index(self, arr, value):
        i = None
        try:
            i = arr.index(value)
        except:
            pass
        return i

    def sort(self, num_arr: List[int]) -> List[int]:
        print('Sorting', num_arr)
        is_valid = True
        sorted_rules = []
        while not self.test(','.join(map(str, num_arr))):
            print('still invalid')
            break
        return sorted_rules

valid_sum = 0
invalid_updates = []
sorter = Sorter()
for line in open(path.join(path.dirname(path.abspath(__file__)), 'sample.txt'), 'r'):
    if line == '\n':
        continue
    if match := re.findall('(\\d+)\\|(\\d+)', line):
        num1, num2 = match[0][0], match[0][1]
        sorter.add_rule(num1, num2)
    else:
        line = line.replace('\n', '')
        page_nums = line.split(',')
        is_valid = sorter.test(line)
        if is_valid:
            valid_sum += int(page_nums[(len(page_nums) - 1) // 2])
            continue
        invalid_updates.append(page_nums)


print(f'valid middle page sum = {valid_sum}')
print(f'Invalid updates {invalid_updates}')
sorter.sort(invalid_updates[0])