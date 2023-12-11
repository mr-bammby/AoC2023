EMPTY_DISTANCE = 1000000

def print_map(map):
    for line in map:
        print_map_line(line)

def print_map_line(line):
    str_line = ""
    for char in line:
        str_line += char
    print(str_line)

def calc_distance(point1, point2, empty_column_list, empty_row_list):
    expansion_factor = 0
    for num in empty_column_list:
        if point1[0] > point2[0]:
            if num in range(point2[0], point1[0]):
                expansion_factor +=1
        elif point1[0] < point2[0]:
           if num in range(point1[0], point2[0]):
                expansion_factor +=1
    for num in empty_row_list:
        if point1[1] > point2[1]:
            if num in range(point2[1], point1[1]):
                expansion_factor +=1
        elif point1[1] < point2[1]:
           if num in range(point1[1], point2[1]):
                expansion_factor +=1
    expansion_factor = expansion_factor * EMPTY_DISTANCE - expansion_factor
    return(abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) + expansion_factor)

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
            result += calc_distance(coordinates[i], coordinates[j], empty_column_list, empty_row_list)
    print("Result: " + str(result))

if (__name__ == "__main__"):
    main("./11/input1.txt")