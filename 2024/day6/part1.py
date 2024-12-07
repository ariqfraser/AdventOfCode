from os import path

class PathFinder():
    __pos = None
    __starting_map = []
    __map = []
    __offsets = { "N": (0, -1), "W": (-1, 0), "E": (1, 0), "S": (0, 1) }
    __direction = "N"
    __max = {"x": 0, "y": 0}

    def __init__(self, filename):
        data = open(path.join(path.dirname(path.abspath(__file__)), filename), 'r')
        self.__map = [list(line.replace('\n','')) for line in data.readlines()]
        self.__starting_map = [row.copy() for row in self.__map]

        for y in range(len(self.__map)):
            if self.__pos is not None:
                break
            for x in range(len(self.__map[y])): 
                if self.__map[y][x] == '^':
                    self.__pos = {'x': x, 'y': y}
                    self.__map[y][x] = '.'
                    break

        self.__max['x'] = len(self.__map[0]) - 1
        self.__max['y'] = len(self.__map) - 1
        self.__print(self.__starting_map)
    
    def __print(self, map_data):
        for row in map_data:
            print(''.join(row))
        print('\n')
    
    def __change_direction(self):
        directions = ['N', 'E', 'S', 'W']
        i = directions.index(self.__direction)
        new_i = i + 1
        if new_i >= len(directions):
            new_i = 0
        self.__direction = directions[new_i]
        # print(f'Changing Direction {directions[i]} > {self.__direction}')

    def __move_forward(self):
        ahead_x = self.__pos['x'] + self.__offsets[self.__direction][0]
        ahead_y = self.__pos['y'] + self.__offsets[self.__direction][1]

        if self.__map[ahead_y][ahead_x] == '#':
            self.__change_direction()
        self.__pos['x'] += self.__offsets[self.__direction][0]
        self.__pos['y'] += self.__offsets[self.__direction][1]
        # print(self.__pos)

    def __can_move(self):
        if self.__direction == 'N' and self.__pos['y'] <= 0:
            return False
        if self.__direction == 'E' and self.__pos['x'] >= self.__max['x']:
            return False
        if self.__direction == 'S' and self.__pos['y'] >= self.__max['y']:
            return False
        if self.__direction == 'W' and self.__pos['x'] <= 0:
            return False
        return True

    def calculate(self):
        while self.__can_move():
            self.__map[self.__pos['y']][self.__pos['x']] = 'X'
            self.__move_forward()
        self.__map[self.__pos['y']][self.__pos['x']] = 'X'
        self.__print(self.__map)
        self.__count_moves()
    
    def __count_moves(self):
        flattened_map = [char for row in self.__map for char in row]
        print(f'{flattened_map.count('X')} moves made')

path_finder = PathFinder('input.txt')
path_finder.calculate()