def print_map(map):
    for line in map:
        print_map_line(line)

def print_map_line(line):
    str_line = ""
    for char in line:
        str_line += char
    print(str_line)

def insert_empty_row(map, index, empty_char = "."):
    length = len(map[0])
    new_map = map[:index] + ([[empty_char] * length]) + map[index:]
    return(new_map)

def insert_empty_column(map, index, empty_char = "."):
    new_map = []
    for line in map:
        new_map.append(line[:index] + [empty_char] + line[index:])
    return(new_map)

def calc_distance(point1, point2):
    return(abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))

def main(filepath):
    file = open(filepath, "r")
    result = 0
    map = []
    first_line = True
    empty_column_list = []
    empty_row_list = []
    cnt = 0
    for line in file:
        if (first_line):
            first_line = False
            for i in range(len(line) - 1):
                empty_column_list.append(i)
        list_line = list(line)
        if (list_line[-1] == "\n"):
            line = line[:-1]
        map.append(list(line))
        if ("#" in list_line):
            real_index = -1
            while("#" in list_line):
                index = list_line.index("#")
                if (real_index == -1):
                    real_index = index
                else:
                    real_index = index + real_index + 1
                if (real_index in empty_column_list):
                    place = empty_column_list.index(real_index)
                    empty_column_list = empty_column_list[:place] + empty_column_list[place+1:]
                list_line = list_line[index + 1:]
        else:
            empty_row_list.append(cnt)
        cnt += 1
    for index in reversed(empty_column_list):
        map = insert_empty_column(map, index)
    for index in reversed(empty_row_list):
        map = insert_empty_row(map,index)
    coordinates = []
    for line, i in zip(map, range(len(map))):
        if ("#" in line):
            real_index = -1
            while("#" in line):
                index = line.index("#")
                if (real_index == -1):
                    real_index = index
                else:
                    real_index = index + real_index + 1
                coordinates.append((real_index, i))
                line = line[index + 1:]
    result = 0
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            result += calc_distance(coordinates[i], coordinates[j])
    print("Result: " + str(result))

if (__name__ == "__main__"):
    main("./11/input1.txt")