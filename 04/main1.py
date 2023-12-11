def main (filepath):
    file = open(filepath, "r")
    sum = 0
    for line in file:
        _, str_arrays = line.split(": ")
        str_winning_arr, str_your_arr = str_arrays.split(" | ")
        winning_arr = str_winning_arr.split()
        your_arr = str_your_arr.split()
        winning_nums = []
        points = 0
        for str_num in winning_arr:
            winning_nums.append(int(str_num))
        for str_num in your_arr:
            my_num = int(str_num)
            for num in winning_nums:
                if (my_num == num):
                    points = points + 1
                    break
        if (points != 0):
            sum = sum + (1 << (points - 1))
    print("REsult: " + str(sum))

if __name__ == "__main__":
    main("./input1.txt") 
