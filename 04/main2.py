def main (filepath):
    file = open(filepath, "r")
    sum = 0
    card_nums = [1] * 215
    for line in file:
        str_card, str_arrays = line.split(": ")
        _, str_card_num = str_card.split()
        card_num = int(str_card_num)
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
            for i in range(points):
                card_nums[card_num + i] = card_nums[card_num + i] + card_nums[card_num - 1]
    for num in card_nums:
        sum = sum + num     
    print("REsult: " + str(sum))

if __name__ == "__main__":
    main("./input1.txt") 
