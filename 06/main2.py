import math

def main(filepath):
    file = open(filepath, "r")
    time_data = []
    distance_data = []
    result = 1
    temp_str_time = ""
    temp_str_distance = ""
    for line in file:
        data_name, str_data = line.split(": ")
        str_arr_data = str_data.split()

        for data in str_arr_data:
            if (data_name == "Time"):
                temp_str_time += data
            else:
                temp_str_distance += data
    time_data.append(float(temp_str_time))
    distance_data.append(float(temp_str_distance))
    for time, distance in zip(time_data, distance_data):
        det = (time ** 2) - (4 * distance)
        if (det > 0):
            upp_border = (time + math.sqrt(det)) / 2
            low_border = (time - math.sqrt(det)) / 2
            upp_border = math.floor(upp_border)
            low_border = math.ceil(low_border)
            if (low_border < 1):
                low_border = 1
            if (upp_border > (time - 1)):
                upp_border = int(time - 1)
            result *= upp_border - low_border + 1
        elif (det < 0):
            result = 0
    print("Result: " + str(result))

if (__name__ == "__main__"):
    main("./06/input1.txt")