import copy 

def main(filepath):
    file = open(filepath, "r")
    state = 0
    num_pairs = []
    changed_num = []
    for line in file:
        if (state == 0):
            _, str_seed_data = line.split(": ")
            str_arr_seed_data = str_seed_data.split()
            num_data = []
            for str_num in str_arr_seed_data:
                num_data.append(int(str_num))
            for i in range(0, len(num_data), 2):
                num_pairs.append([num_data[i], num_data[i + 1], False])
            state = 1
        else:
            test = False
            str_data = line.split()
            if (type(str_data is list)):
                if (len(str_data) == 3):
                    test = True
                elif(len(str_data) == 2):
                    for pair in num_pairs:
                        pair[2] = False
            if (test):
                range_data = []
                for str_num in str_data:
                    range_data.append(int(str_num))
                cpy_pairs = copy.deepcopy(num_pairs)    #important make to deep copy
                for pair, i in zip(num_pairs, range(len(num_data))):
                    if (pair[2] == False):
                        if (pair[0] >= range_data[1] and pair[0] < (range_data[1] + range_data[2])):                # in case searched range starts inside map range
                            if ((pair[0] + pair[1]) > (range_data[1] + range_data[2])):                             # if searche range ends outside of map range
                                cpy_pairs[i][1] = (range_data[1] + range_data[2]) - pair[0]
                                cpy_pairs.append([range_data[1] + range_data[2], pair[1] - cpy_pairs[i][1], False])
                            cpy_pairs[i][2] = True                                                                   # in case of map range fully covering searcerd range no additional changes needed
                            cpy_pairs[i][0] = (pair[0] - range_data[1]) + range_data[0]
                        elif (pair[0] < range_data[1] and (pair[0] + pair[1]) > range_data[1]):                      # if searched range starts before map range
                            cpy_pairs.append([pair[0], range_data[1] - pair[0], False])                              # part before map range
                            if ((pair[0] + pair[1]) > (range_data[1] + range_data[2])):                              # if searched range fully covers map range
                                cpy_pairs[i][1] = range_data[2]
                                cpy_pairs.append([range_data[1] + range_data[2], ((pair[0] + pair[1]) - (range_data[1] + range_data[2])) , False]) # part after map range
                            else:
                                cpy_pairs[i][1] = (pair[0] + pair[1]) - range_data[1]                                # handling end inside a mapped range
                            cpy_pairs[i][2] = True                                                                   # part inside the mapped range
                            cpy_pairs[i][0] = range_data[0]
                num_pairs = cpy_pairs                                                                                # no other option of crossesction of two ranges
    result_list = []
    for pair in num_pairs:
        result_list.append(pair[0])
    print("Result: " + str(min(result_list)))


if (__name__ == "__main__"):
    main("./05/input1.txt")