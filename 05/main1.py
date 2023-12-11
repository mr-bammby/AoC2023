def main(filepath):
    file = open(filepath, "r")
    state = 0
    num_data = []
    changed_num = []
    for line in file:
        if (state == 0):
            _, str_seed_data = line.split(": ")
            str_arr_seed_data = str_seed_data.split()
            for str_num in str_arr_seed_data:
                num_data.append(int(str_num))
            state = 1
        else:
            test = False
            str_data = line.split()
            if (type(str_data is list)):
                if (len(str_data) == 3):
                    test = True
                elif(len(str_data) == 2):
                    changed_num = [False] * len(num_data)
            if (test):
                range_data = []
                for str_num in str_data:
                    range_data.append(int(str_num))
                for num, i, changed in zip(num_data, range(len(num_data)), changed_num):
                    if (num >= range_data[1] and num < (range_data[1] + range_data[2]) and changed == False):
                        num_data[i] = (num - range_data[1]) + range_data[0]
                        changed_num[i] = True
    print("Result: " + str(min(num_data)))

if (__name__ == "__main__"):
    main("./05/input1.txt")